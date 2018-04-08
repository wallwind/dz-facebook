# coding=utf-8
from django.http import HttpResponse
from Utils import net_client
from Utils.extra_info_engine import run_html
from HuntnewsId import templates
import time
from lxml import etree
import random
import urlparse
from PbRender.uclite_xml_to_pb import xml2pb
from HuntnewsId import Filters
import json
from django.views.decorators.csrf import csrf_exempt
import logging
from django.views.decorators.gzip import gzip_page
from Uclite.settings import content_page_cache_seconds
from Uclite.settings import site_degrade
import datetime
import socket
import json
from FaceBook import Filters as FbFilters
from FaceBook import templates as FbTemplates
import requests
from urllib import quote
import re
# original website cookie
org_cookie_prefix = "org_"
uclite_cookie_prefix = "uclite_"
org_index_url = "http://www.huntnews.id"
fb_org_index_url = "https://www.facebook.com"


logging.getLogger("requests").setLevel(logging.WARNING)


class UcliteException(Exception):
    """
    Uclite自定义异常
    """
    def __init__(self, *args, **kwargs):
        super(UcliteException, self).__init__()
        self.__code = kwargs.get("code", 500)
        self.message = kwargs.get("message", "")

    @property
    def status_code(self):
        return self.__code


def view_exception_handle(func):
    def __wrap(*args, **kwargs):
        if len(args) > 0:
            ctx = fetch_context(args[0])
            if "ext_stat" not in ctx:
                ctx["ext_stat"] = dict()
        else:
            ctx = {"ext_stat": {}}
        try:
            # for test
            if len(args) > 0 and hasattr(args[0], "GET") and isinstance(args[0].GET, dict):
                if args[0].GET.get("uclite") == "site_degrade":
                    ctx["ext_stat"]["result"] = "site_degrade"
                    return HttpResponse(status=301, content="")  # 整站降级
                if args[0].GET.get("uclite") == "page_degrade":
                    raise UcliteException(code=501, message="for test")
            # end for test

            # 整站降级
            if site_degrade:
                ctx["ext_stat"]["result"] = "site_degrade"
                return HttpResponse(status=301, content="")
            rsp = func(*args, **kwargs)
            ctx["ext_stat"]["result"] = "entered"
        except UcliteException as e:
            ctx["ext_stat"]["result"] = "page_degrade"
            ctx["ext_stat"]["e_code"] = e.status_code
            ctx["ext_stat"]["e_msg"] = e.message
            rsp = uclite_web_view_view(*args, **kwargs)
        except Exception as e:
            ctx["ext_stat"]["result"] = "page_degrade"
            ctx["ext_stat"]["e_code"] = "0"
            ctx["ext_stat"]["e_msg"] = e.message
            rsp = uclite_web_view_view(*args, **kwargs)
        return rsp
    return __wrap


def view_fb_exception_handle(func):
    def __wrap(*args, **kwargs):
        if len(args) > 0:
            ctx = fetch_context(args[0])
            if "ext_stat" not in ctx:
                ctx["ext_stat"] = dict()
        else:
            ctx = {"ext_stat": {}}
        try:
            # for test
            if len(args) > 0 and hasattr(args[0], "GET") and isinstance(args[0].GET, dict):
                if args[0].GET.get("uclite") == "site_degrade":
                    ctx["ext_stat"]["result"] = "site_degrade"
                    return HttpResponse(status=301, content="")  # 整站降级
                if args[0].GET.get("uclite") == "page_degrade":
                    raise UcliteException(code=501, message="for test")
            # end for test

            # 整站降级
            if site_degrade:
                ctx["ext_stat"]["result"] = "site_degrade"
                return HttpResponse(status=301, content="")
            rsp = func(*args, **kwargs)
            ctx["ext_stat"]["result"] = "entered"
        except UcliteException as e:
            ctx["ext_stat"]["result"] = "page_degrade"
            ctx["ext_stat"]["e_code"] = e.status_code
            ctx["ext_stat"]["e_msg"] = e.message
            rsp = uclite_web_login_view(*args, **kwargs)
        except Exception as e:
            ctx["ext_stat"]["result"] = "page_degrade"
            ctx["ext_stat"]["e_code"] = "0"
            ctx["ext_stat"]["e_msg"] = e.message
            rsp = uclite_web_fb_view(*args, **kwargs)
        return rsp
    return __wrap

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_original_cookie(request):
    ret = dict()
    for k, v in request.COOKIES.iteritems():
        if k and k.startswith(org_cookie_prefix):
            ret[k[len(org_cookie_prefix):]] = v
    return ret


def set_original_cookie(response, cookie):
    for k, v in cookie.iteritems():
        response.set_cookie(org_cookie_prefix + k, v)

def set_other_cookie(response, cookie):
    for k, v in cookie.items():
        response.set_cookie(uclite_cookie_prefix + k, v)

def fetch_context(request):
    if hasattr(request, "uclite_ctx"):
        return request.uclite_ctx
    else:
        return dict()


def statistics(func):
    def __wrap(*args, **kwargs):
        ctx = dict()
        ctx["enter_time"] = time.time()
        req = args[0]
        ctx["req_id"] = "%u%s" % (time.time() * 1000, id(req))
        logging.info("type=accept`req_id=%s`hostname=%s`client_ip=%s`url=%s" % (ctx["req_id"], socket.gethostname(), get_client_ip(req), req.build_absolute_uri()))
        req.__dict__["uclite_ctx"] = ctx
        rsp = func(*args, **kwargs)
        ctx["size"] = len(rsp.content)
        ctx["exit_time"] = time.time()
        __output_stat_info(ctx)
        return rsp
    return __wrap


def handle_request(request, ctx, json_data, fetch_html=True, cache_enable=False):
    # <-- begin of debug
    # print "<-- begin -->"
    # print "1.", request.build_absolute_uri() + "&uclite=debug"
    # print "2.", request.build_absolute_uri() + "&uclite=json"
    # print "3.", request.build_absolute_uri() + "&uclite=html"
    # print "4.", request.GET.get("url", None)
    # print "cookies:", get_original_cookie(request)
    # print "<-- end -->"
    # end of debug -->
    req_url = request.GET.get("url", org_index_url)
    req_cookie = get_original_cookie(request)
    parsed = urlparse.urlparse(req_url)
    req_url_params = urlparse.parse_qs(parsed.query)
    ctx["req_url_params"]           = dict()
    ctx["req_params"]               = dict()
    ctx["url"]                      = request.build_absolute_uri()
    ctx["req_url"]                  = req_url
    ctx["req_cookie"]               = req_cookie
    ctx["client_ip"]                = get_client_ip(request)
    for k, v in req_url_params.iteritems():
        ctx["req_url_params"][k] = v[0]
    for k, v in request.GET.iteritems():
        ctx["req_params"][k] = v
    if fetch_html:
        ctx["fetch_html_begin_time"]    = time.time()
        rsp_url, rsp_html, rsp_cookie   = net_client.get_html(req_url, cookies=req_cookie, cache_enable=cache_enable)
        ctx["fetch_html_end_time"]      = time.time()
        ctx["rsp_url"]                  = rsp_url
        ctx["rsp_html"]                 = rsp_html
        ctx["rsp_cookie"]               = rsp_cookie
        json_data["url"]                = rsp_url
    else:
        json_data["url"]                = req_url
    # json data for rendering
    json_data["uclite_host"]        = request.get_host()
    json_data["random_time"]        = random.random()


def handle_fb_request(request, ctx, json_data, fetch_html=True, cache_enable=False):
    # <-- begin of debug
    # print "<-- begin -->"
    # print "1.", request.build_absolute_uri() + "&uclite=debug"
    # print "2.", request.build_absolute_uri() + "&uclite=json"
    # print "3.", request.build_absolute_uri() + "&uclite=html"
    # print "4.", request.GET.get("url", None)
    # print "cookies:", get_original_cookie(request)
    # print "<-- end -->"
    # end of debug -->
    req_url = request.GET.get("url", fb_org_index_url)
    req_cookie = get_original_cookie(request)
    parsed = urlparse.urlparse(req_url)
    req_url_params = urlparse.parse_qs(parsed.query)
    ctx["req_url_params"]           = dict()
    ctx["req_params"]               = dict()
    ctx["url"]                      = request.build_absolute_uri()
    ctx["req_url"]                  = req_url
    ctx["req_cookie"]               = req_cookie
    ctx["client_ip"]                = get_client_ip(request)
    for k, v in req_url_params.iteritems():
        ctx["req_url_params"][k] = v[0]
    for k, v in request.GET.iteritems():
        ctx["req_params"][k] = v
    if fetch_html:
        ctx["fetch_html_begin_time"]    = time.time()
        rsp_url, rsp_html, rsp_cookie   = net_client.get_fb_html(req_url, cookies=req_cookie, cache_enable=cache_enable)
        ctx["fetch_html_end_time"]      = time.time()
        ctx["rsp_url"]                  = rsp_url
        ctx["rsp_html"]                 = rsp_html
        ctx["rsp_cookie"]               = rsp_cookie
        json_data["url"]                = rsp_url
    else:
        json_data["url"]                = req_url
    # json data for rendering
    json_data["uclite_host"]        = request.get_host()
    if request.is_secure():
        json_data["uclite_scheme"]  ="https"
        ctx["uclite_scheme"] = "https"
    else:
        json_data["uclite_scheme"] = "http"
        ctx["uclite_scheme"] = "http"
    json_data["random_time"]        = random.random()


def __output_stat_info(ctx):
    stat                = dict()
    stat["total_time"]  = ctx["exit_time"] - ctx["enter_time"]
    stat["io_time"]     = ctx.get("fetch_html_end_time", time.time()) - ctx.get("fetch_html_begin_time", time.time())
    stat["custom_time"] = stat.get("total_time", 0) - stat.get("io_time", 0)
    stat["url"]         = ctx.get("url", "")
    stat["src_url"]     = ctx.get("rsp_url", "")
    stat["size"]        = ctx.get("size", 0)
    stat["client_ip"]   = ctx.get("client_ip", 0)
    stat["req_id"]      = ctx.get("req_id", "0")
    stat["hostname"]    = socket.gethostname()
    if "error" in ctx:
        stat["error"]   = ctx["error"]
    items = list()
    for k, v in stat.iteritems():
        items.append("%s=%s" % (k, v))
    if "ext_stat" in ctx:
        for k, v in ctx["ext_stat"].iteritems():
            items.append("%s=%s" % (k, v))
    logging.info("`".join(items))


def gen_response(request, ctx):
    result_type = request.GET.get("uclite", "")
    if result_type == "xml" or result_type == "debug":
        content = ctx.get("xml_data", "<xml_data>N/A</xml_data>")
        content_type = "text/xml"
    elif result_type == "json":
        content = json.dumps(ctx.get("json_data", {"json_data": "N/A"}))
        content_type = "application/json"
    elif result_type == "html":
        content = ctx.get("rsp_html", "N/A")
        content_type = "text/html"
    else:
        content = ctx["pb_data"]
        content_type = "application/octet-stream"
    if ctx.has_key('location'):
        rsp = HttpResponse(content, content_type=content_type,status=302)
        rsp["location"] =ctx["location"]
    else:
        rsp = HttpResponse(content, content_type=content_type)
    set_original_cookie(rsp, ctx["rsp_cookie"])
    if ctx.has_key('pri_cookies'):
        set_other_cookie(rsp, ctx["pri_cookies"])
    return rsp


def uclite_not_found_page(request):
    from django.http import HttpResponseNotFound
    return HttpResponseNotFound()


def uclite_monitor_view(request):
    return HttpResponse(content="uclite monitor @ %s" % datetime.datetime.now())


@statistics
@gzip_page
@view_exception_handle
def uclite_list_page_view(request):
    ctx = fetch_context(request)
    json_data = dict()
    handle_request(request, ctx, json_data)
    json_data.update(run_html(Filters.list_page_filter, ctx["rsp_html"], ctx["rsp_url"]))
    json_data["list_id"] = "page_list"
    max_index = int(ctx["req_params"].get("index", "0"))
    if 'items' in json_data:
        for i, item in enumerate(json_data['items']):
            json_data['items'][i]['index'] = int(json_data['items'][i]['index']) + max_index + 1
        json_data['max_index'] = max_index + len(json_data['items'])

    # 有序号的页面刷新,需要清除,防止编号重复
    if ctx["req_url_params"].get("cat", "") == "topics":
        json_data["first_pos"] = ""
    ctx["json_data"]    = json_data
    ctx["xml_data"]     = templates.list_page_template.render(ctx["json_data"]).encode("utf-8")
    xml_node            = etree.XML(ctx["xml_data"])
    ctx["pb_data"]      = xml2pb(xml_node, "replace", "0", "Ok")
    return gen_response(request, ctx)


@statistics
@gzip_page
@view_exception_handle
def uclite_list_cmd_view(request, cmd):
    ctx = fetch_context(request)
    json_data = dict()
    handle_request(request, ctx, json_data)
    json_data.update(run_html(Filters.list_node_filter, ctx["rsp_html"], ctx["rsp_url"]))

    max_index = int(ctx["req_params"].get("index", "0"))
    json_data["list_chncat"]    = ctx["req_url_params"].get("chncat", "0")
    json_data["list_key"]       = ctx["req_url"][ctx["req_url"].find('/list/') + 6: ctx["req_url"].find('?')]
    json_data["list_id"]        = request.GET.get("id", "-1")
    has_index                   = json_data["list_key"] == "topics"
    if 'items' in json_data:
        for i, item in enumerate(json_data['items']):
            json_data['items'][i]['index'] = int(json_data['items'][i].get('index', '0')) + max_index + 1
        json_data['max_index'] = max_index + len(json_data['items'])

    if has_index:
        json_data["first_pos"] = ""
        if cmd == "prepend":
            cmd = "replace"

    ctx["json_data"]    = json_data
    ctx["xml_data"]     = templates.list_node_template.render(ctx["json_data"]).encode("utf-8")
    xml_node            = etree.XML(ctx["xml_data"])
    ctx["pb_data"]      = xml2pb(xml_node, cmd, request.GET.get("id", "N/A"), "Ok")
    return gen_response(request, ctx)


@statistics
@gzip_page
@view_exception_handle
def uclite_simple_list_page_view(request):
    ctx = fetch_context(request)
    json_data = dict()
    handle_request(request, ctx, json_data)
    json_data.update(run_html(Filters.simple_list_page_filter, ctx["rsp_html"], ctx["rsp_url"]))
    json_data["list_id"] = "page_list"
    json_data["disable_refresh"] = True
    max_index = int(ctx["req_params"].get("index", "0"))
    if 'items' in json_data:
        for i, item in enumerate(json_data['items']):
            json_data['items'][i]['index'] = int(json_data['items'][i]['index']) + max_index + 1
        json_data['max_index'] = max_index + len(json_data['items'])

    ctx["json_data"]    = json_data
    ctx["xml_data"]     = templates.simple_list_page_template.render(ctx["json_data"]).encode("utf-8")
    xml_node            = etree.XML(ctx["xml_data"])
    ctx["pb_data"]      = xml2pb(xml_node, "replace", "0", "Ok")
    return gen_response(request, ctx)


@statistics
@gzip_page
@view_exception_handle
def uclite_content_view(request):
    ctx = fetch_context(request)
    json_data = dict()
    handle_request(request, ctx, json_data, cache_enable=True)
    json_data.update(run_html(Filters.content_page_filter, ctx["rsp_html"], ctx["rsp_url"]))
    json_data["list_id"] = "hot_list"
    ctx["json_data"]    = json_data
    ctx["xml_data"]     = templates.content_page_template.render(ctx["json_data"]).encode("utf-8")
    xml_node            = etree.XML(ctx["xml_data"])
    ctx["pb_data"]      = xml2pb(xml_node, "replace", "0", "Ok")
    rsp = gen_response(request, ctx)
    rsp["Cache-Control"] = "max-age=%d" % content_page_cache_seconds
    return rsp


@statistics
@gzip_page
@view_exception_handle
def uclite_content_append_view(request):
    ctx = fetch_context(request)
    json_data = dict()
    handle_request(request, ctx, json_data)
    json_data.update(run_html(Filters.content_page_more_text_filter, ctx["rsp_html"], ctx["rsp_url"]))

    ctx["json_data"]    = json_data
    ctx["xml_data"]     = templates.content_page_more_template.render(ctx["json_data"]).encode("utf-8")
    xml_node            = etree.XML(ctx["xml_data"])
    ctx["pb_data"]      = xml2pb(xml_node, "append", "content_read_more", "Ok")
    return gen_response(request, ctx)


@statistics
@gzip_page
@view_exception_handle
def uclite_content_list_cmd_view(request):
    ctx = fetch_context(request)
    json_data = dict()
    handle_request(request, ctx, json_data)
    json_data.update(run_html(Filters.content_page_hot_list_filter, ctx["rsp_html"], ctx["rsp_url"]))

    json_data["list_chncat"]    = ctx["req_url_params"].get("chncat", 'hotnews_indonesian')
    json_data["list_key"]       = ctx["req_url"][ctx["req_url"].find('/list/') + 6: ctx["req_url"].find('?')]
    json_data["list_id"]        = request.GET.get("id", "-1")
    first_page                  = ctx["req_url_params"].get("firstPage", "")
    page                        = ctx["req_url_params"].get("page", "")

    if not first_page and page:
        page = int(page)
        first_page = page - 1
    elif not page and first_page:
        first_page = int(first_page)
        page = first_page + 1
    elif not first_page and not page:
        first_page = 1
        page = 2
    else:
        first_page = int(first_page)
        page = int(page) + 1
    json_data["first_page"] = first_page
    json_data["page"]       = page
    json_data["load_more"]  = page <= first_page + 5

    ctx["json_data"]    = json_data
    if json_data["list_key"] == 'hotNews':
        ctx["xml_data"] = templates.content_page_hot_list_template.render(json_data).encode("utf-8")
    else:
        ctx["xml_data"] = templates.content_page_next_list_template.render(json_data).encode("utf-8")
    xml_node            = etree.XML(ctx["xml_data"])
    ctx["pb_data"]      = xml2pb(xml_node, "append", request.GET.get("id", "-1"), "Ok")
    return gen_response(request, ctx)


@statistics
@gzip_page
@view_exception_handle
def uclite_feedback_view(request, page_type):
    ctx = fetch_context(request)
    json_data = dict()
    handle_request(request, ctx, json_data)
    json_data["ref_url"] = request.GET.get('ref', "")
    if page_type == 'index':
        json_data.update(run_html(Filters.index_feedback_filter, ctx["rsp_html"], ctx["rsp_url"]))
        ctx["xml_data"] = templates.index_feedback_template.render(json_data).encode("utf-8")
    else:
        json_data.update(run_html(Filters.detail_feedback_filter, ctx["rsp_html"], ctx["rsp_url"]))
        ctx["xml_data"] = templates.detail_feedback_template.render(json_data).encode("utf-8")

    ctx["json_data"]    = json_data
    xml_node            = etree.XML(ctx["xml_data"])
    ctx["pb_data"]      = xml2pb(xml_node, "replace", request.GET.get("id", "0"), "Ok")
    return gen_response(request, ctx)


@csrf_exempt
@statistics
@gzip_page
@view_exception_handle
def uclite_feedback_result_view(request):
    ctx = fetch_context(request)
    json_data = dict()
    handle_request(request, ctx, json_data, fetch_html=False)
    node_id = request.GET.get("id", "N/A")
    pos_data = list()
    for k, v in request.POST.iteritems():
        pos_data.append("%s=%s" % (k, v))

    ctx["fetch_html_begin_time"]    = time.time()
    rsp_url, rsp_html, rsp_cookie = net_client.post_data(ctx["req_url"], '&'.join(pos_data), cookies=ctx["req_cookie"])
    ctx["fetch_html_end_time"]      = time.time()
    ctx["rsp_url"]                  = rsp_url
    ctx["rsp_html"]                 = rsp_html
    ctx["rsp_cookie"]               = rsp_cookie
    json_data["url"]                = rsp_url

    if rsp_html == '{"code":200}':
        ctx["pb_data"] = xml2pb(None, "success", node_id, "Kritik & Saran anda telah terkirim")
    else:
        ctx["pb_data"] = xml2pb(None, "error", node_id, rsp_html)
    ctx["json_data"]    = rsp_html
    return gen_response(request, ctx)


@gzip_page
def uclite_web_view_view(request):
    ctx = fetch_context(request)
    json_data = dict()
    handle_request(request, ctx, json_data, fetch_html=False)
    url                             = request.GET.get("url", org_index_url)
    ctx["rsp_url"]                  = url
    ctx["rsp_cookie"]               = ctx["req_cookie"]
    ctx["fetch_html_begin_time"]    = time.time()
    ctx["fetch_html_end_time"]      = ctx["fetch_html_begin_time"]
    ctx["xml_data"]                 = templates.web_view_template.render({"url": url}).encode("utf-8")
    xml_node                        = etree.XML(ctx["xml_data"])
    ctx["pb_data"]                  = xml2pb(xml_node, "replace", "0", "Ok")
    return gen_response(request, ctx)

@gzip_page
def uclite_web_fb_view(request):
    ctx = fetch_context(request)
    json_data = dict()
    handle_request(request, ctx, json_data, fetch_html=False)
    url                             = request.GET.get("url", org_index_url)
    ctx["rsp_url"]                  = url
    ctx["rsp_cookie"]               = ctx["req_cookie"]
    ctx["fetch_html_begin_time"]    = time.time()
    ctx["fetch_html_end_time"]      = ctx["fetch_html_begin_time"]
    json_data["url"]                = url
    if request.is_secure():
        uclite_scheme = "https"
    else:
        uclite_scheme = "http"
    #ctx["xml_data"]                 = FbTemplates.time_line_login.render({"url": url, "uclite_host": request.get_host(), "uclite_scheme": uclite_scheme}).encode("utf-8")
    #xml_node                        = etree.XML(ctx["xml_data"])
    ctx["pb_data"]                  = xml2pb(None, "error", "0", "Error occurred, try again!")
    return gen_response(request, ctx)


@gzip_page
def uclite_web_login_view(request):
    ctx = fetch_context(request)
    json_data = dict()
    handle_request(request, ctx, json_data, fetch_html=False)
    url                             = request.GET.get("url", org_index_url)
    ctx["rsp_url"]                  = url
    ctx["rsp_cookie"]               = ctx["req_cookie"]
    ctx["fetch_html_begin_time"]    = time.time()
    ctx["fetch_html_end_time"]      = ctx["fetch_html_begin_time"]
    json_data["url"]                = url
    if request.is_secure():
        uclite_scheme = "https"
    else:
        uclite_scheme = "http"
    ctx["xml_data"]                 = FbTemplates.time_line_login.render({"url": url, "uclite_host": request.get_host(), "uclite_scheme": uclite_scheme}).encode("utf-8")
    xml_node                        = etree.XML(ctx["xml_data"])
    ctx["pb_data"]                  = xml2pb(xml_node, "error", "0", "system error")
    return gen_response(request, ctx)


def handle_add_friend(text=""):
    fjson = json.loads(text[9:].encode("utf-8"))
    playloadValue = fjson["payload"]
    actionValue = playloadValue["actions"]

    if len(actionValue) == 1:
        return 1
    else:
        return 0
    # for actionItem in actionValue:
    #     if actionItem["cmd"] == "script":
    #         match = FbFilters.filter_handler_json.match(actionItem["code"])
    #         if match:
    #             hjson = json.loads(match.groupdict().get("handler_json"))
    #             instanceJson = hjson['instances']



    pass
def handle_facebook_json(cmd,text=""):
    fjson = json.loads(text[9:].encode("utf-8"))
    playloadValue = fjson["payload"]
    actionValue = playloadValue["actions"]

    for actionItem in actionValue:
        if actionItem["cmd"] == cmd and actionItem["cmd"] == "append":
            return actionItem["html"]
        elif actionItem["cmd"] == cmd and actionItem["cmd"] == "replace":
            return actionItem["html"]
        elif actionItem["cmd"] == "script" and actionItem["cmd"] == cmd:
            return actionItem["code"]
    return

def get_encrypted(text=""):
    match = FbFilters.filter_encrypte_url_reg.match(text.replace('\\"', '"'))
    if match:
        return match.groupdict().get("encrypte")
    return None
def get_handler_json(text=""):
    match = FbFilters.filter_handler_json.match(text)
    if match:
        return match.groupdict().get("handler_json").replace('\\"', '"')
    return None
def get_handler_json1(text=""):
    match = FbFilters.filter_handler_json.match(text)
    if match:
        return match.groupdict().get("handler_json")
    return None
def get_redirect_url(text=""):
    jHandler = json.loads(text.replace('\\"', '"'))
    for item in jHandler["require"]:
        for item2 in item:
            if isinstance(item2, list):
                if len(item2) == 1:
                    return item2[0].replace("\\", "")

def get_after_like_data(jsonstr=""):
    #jHandler = json.loads(jsonstr.replace("\u003C", "<"))
    jHandler = json.loads(jsonstr.replace('\\"', '"'))
    if jHandler:
        for item in jHandler["require"]:
            for item2 in item:
                if isinstance(item2, list) and len(item2):
                    for item3 in item2:
                        if isinstance(item3, dict) and item3.has_key('reactionsentences'):
                            json_data = dict()
                            json_data["current"] = item3["reactionsentences"]["current"]["text"]
                            json_data["alternate"] = item3["reactionsentences"]["alternate"]["text"]
                            json_data["ft_ent_identifier"] = item3["ft_ent_identifier"]
                            json_data["viewerreaction"] = item3["viewerreaction"]
                            return json_data
                    return None
        return None
    return None


def get_aftercursor(text=""):
    jHandler = json.loads(text)
    iWantValue = []
    if jHandler:
        for item in jHandler["require"]:
            for item1 in item:
                if item1 == "InitMMoreItemAutomatic":
                    iWantValue = item
                    break
            continue
        if iWantValue and isinstance(iWantValue, list) and len(iWantValue):
            for item2 in iWantValue:
                if isinstance(item2, list) and len(item2):
                    for item3 in item2:
                        if isinstance(item3,dict) and item3.has_key('id'):
                            return item3['id']
    return None



@csrf_exempt
@statistics
@view_fb_exception_handle
def facebook_login(request):
    ctx = fetch_context(request)
    json_data = dict()
    handle_fb_request(request, ctx, json_data, fetch_html=False)
    node_id = request.GET.get("id", "N/A")
    pos_data = list()
    for k, v in request.POST.iteritems():
        pos_data.append("%s=%s" % (k, v))
    ctx["fetch_html_begin_time"] = time.time()
    pri_cookies = dict()

    req = requests.request("POST", ctx["req_url"], headers=net_client.fb_headers, data='&'.join(pos_data))
    rsp_url = req.url
    rsp_html = req.text
    rsp_cookie = req.cookies
    rsp_status = req.status_code
    ctx["fetch_html_end_time"] = time.time()
    ctx["rsp_url"] = rsp_url
    ctx["rsp_html"] = rsp_html
    json_data["url"] = rsp_url
    ctx["rsp_cookie"] = rsp_cookie
    for k,v in req.cookies.iteritems():
       print k,v
    if req and req.text and 200 <= rsp_status < 400 and req.cookies:
        rejson = get_handler_json(req.text)
        if rejson:
            encrypt = get_encrypted(rsp_html)
            pri_cookies["encrypt"] = encrypt
            ctx["pri_cookies"] = pri_cookies
            redir_url = get_redirect_url(rejson)
            ctx["location"] = ctx["uclite_scheme"]+"://"+request.get_host()+"/uclite/time_line/?url="+redir_url
            ctx["pb_data"] = xml2pb(None, "success", node_id, "login success")

    if "location" not in ctx.keys():
        ctx["xml_data"] = FbTemplates.time_line_login.render(json_data).encode("utf-8")
        xml_node = etree.XML(ctx["xml_data"])
        ctx["pb_data"] = xml2pb(xml_node, "error", node_id, "login error")
    ctx["rsp_cookie"] = rsp_cookie
    ctx["json_data"] = rsp_html
    return gen_response(request, ctx)
@csrf_exempt
@view_fb_exception_handle
def facebook_stories(request):
    ctx = fetch_context(request)
    json_data = dict()
    handle_fb_request(request, ctx, json_data)
    rsp_url = ctx["rsp_url"]
    open("./facebook.html", "w+").write(ctx["rsp_html"].encode("utf-8"))
    html_ret = run_html(FbFilters.time_line_filter, ctx["rsp_html"], ctx["rsp_url"])
    if rsp_url.find("m.facebook.com/login.php") >= 0:
        ctx["xml_data"] = FbTemplates.time_line_login.render(json_data).encode("utf-8")
        logging.error("can not get facebook_stories")
    else:
        json_data.update(html_ret)
        ctx["json_data"] = json_data
        ctx["xml_data"] = FbTemplates.time_line_template.render(json_data).encode("utf-8")
    xml_node = etree.XML(ctx["xml_data"])
    ctx["pb_data"] = xml2pb(xml_node, "replace", "0", "Ok")
    return gen_response(request, ctx)

@view_fb_exception_handle
def facebook_test_stories(request):
    ctx = fetch_context(request)
    json_data = dict()
    handle_fb_request(request, ctx, json_data,False)
    ctx["rsp_cookie"] = ctx["req_cookie"]
    all_text = open("./facebookm.html", "r").read().decode("utf-8")
    html_ret = run_html(FbFilters.time_line_filter, all_text, "")

    json_data.update(html_ret)
    ctx["json_data"] = json_data
    ctx["xml_data"] = FbTemplates.time_line_template.render(json_data).encode("utf-8")
    open("xml_data_test.xml", "w+").write(ctx["xml_data"])
    xml_node = etree.XML(ctx["xml_data"])

    ctx["pb_data"] = xml2pb(xml_node, "replace", "0", "Ok")
    return gen_response(request, ctx)

@csrf_exempt
@view_fb_exception_handle
def facebook_stories_more(request):

    ctx = fetch_context(request)
    json_data = dict()
    handle_fb_request(request, ctx, json_data, fetch_html=False)
    node_id = request.GET.get("id", "N/A")
    pos_data = list()
    for key, value in request.POST.iteritems():
        pos_data.append("%s=%s" % (key, value))
        json_data[key] = value
    ctx["fetch_html_begin_time"] = time.time()

    post_data = request.body
    rsp_url, rsp_html, rsp_cookie = net_client.fb_post_data(ctx["req_url"], post_data, cookies=ctx["req_cookie"])
    open("more.html", "w+").write(rsp_html.encode("utf-8"))
    section_html= handle_facebook_json("replace",rsp_html)
    resp_script = handle_facebook_json("script", rsp_html)
    str_json = get_handler_json1(resp_script)
    aftercursor = get_aftercursor(str_json)
    ctx["rsp_url"] = rsp_url
    ctx["rsp_html"] = section_html
    html_ret = run_html(FbFilters.time_line_more_filter, section_html, ctx["rsp_url"])
    ctx["fetch_html_end_time"] = time.time()
    ctx["rsp_cookie"] = ctx["req_cookie"]
    json_data.update(html_ret)
    json_data["aftercursor"] = aftercursor
    ctx["json_data"] = json_data
    ctx["xml_data"] = FbTemplates.time_line_more.render(json_data).encode("utf-8")
    xml_node = etree.XML(ctx["xml_data"])
    ctx["pb_data"] = xml2pb(xml_node, "append", "page_list", "Ok")

    return gen_response(request, ctx)
@view_fb_exception_handle
def facebook_test(request):
    ctx = fetch_context(request)
    json_data = dict()
    handle_fb_request(request, ctx, json_data, fetch_html=False)

    more_html = open("more2.html", "r").read().decode("utf-8")
    section_html = handle_facebook_json("replace", more_html)
    open("test_section_html.html", "w+").write(section_html.encode("utf-8"))
    html_ret = run_html(FbFilters.time_line_more_filter, section_html, "baidu.com")
    ctx["fetch_html_end_time"] = time.time()
    ctx["rsp_cookie"] = ctx["req_cookie"]
    json_data.update(html_ret)
    ctx["json_data"] = json_data
    json.dump(html_ret, open('test_more_json.txt', 'w+'))
    ctx["xml_data"] = FbTemplates.time_line_more.render(json_data).encode("utf-8")
    open("test_xml_data.txt", "w+").write(ctx["xml_data"])
    xml_node = etree.XML(ctx["xml_data"])

    ctx["pb_data"] = xml2pb(xml_node, "append", "page_list", "Ok")
    return gen_response(request, ctx)

@csrf_exempt
@view_fb_exception_handle
def facebook_like(request):
    ctx = fetch_context(request)
    json_data = dict()
    handle_fb_request(request, ctx, json_data, fetch_html=False)
    node_id = request.GET.get("id", "N/A")
    pos_data = list()
    for k, v in request.POST.iteritems():
        pos_data.append("%s=%s" % (k, v))

    ctx["fetch_html_begin_time"] = time.time()
    post_data = request.body
    rsp_url, rsp_html, rsp_cookie = net_client.fb_post_data(ctx["req_url"], post_data,cookies=ctx["req_cookie"])
    #open("like.html" ,"w+").write(rsp_html.encode("utf-8"))
    handler_json = get_handler_json(rsp_html)
    ctx["fetch_html_end_time"] = time.time()
    ctx["rsp_url"] = rsp_url
    ctx["rsp_html"] = rsp_html
    ctx["rsp_cookie"] = ctx["req_cookie"]

    if handler_json:
        json_data = get_after_like_data(handler_json)
        if json_data:
            json_data["code"]= "200"
        else:
            json_data["code"]= "500"
    else:
        json_data["code"] = "500"

    json_data["inter_type"] = "like"
    ctx["xml_data"] = FbTemplates.time_line_interaction.render(json_data).encode("utf-8")

    xml_node = etree.XML(ctx["xml_data"])
    ctx["pb_data"] = xml2pb(xml_node, "replace", "0", rsp_url)

    return gen_response(request, ctx)

@csrf_exempt
@view_fb_exception_handle
def facebook_share(request):
    ctx = fetch_context(request)
    json_data = dict()
    handle_fb_request(request, ctx, json_data, fetch_html=False)
    node_id = request.GET.get("id", "N/A")
    pos_data = list()
    for k, v in request.POST.iteritems():
        pos_data.append("%s=%s" % (k, v))

    ctx["fetch_html_begin_time"] = time.time()
    post_data = request.body
    req = requests.request("POST", ctx["req_url"], headers=net_client.fb_headers, data=post_data, cookies=ctx["req_cookie"])
    #open("share.html", "w+").write(req.text.encode("utf-8"))
    ctx["fetch_html_end_time"] = time.time()
    ctx["rsp_url"] = req.url
    ctx["rsp_html"] = req.text
    ctx["rsp_cookie"] = ctx["req_cookie"]
    if req and req.status_code == 200:
        json_data["code"]= "200"
    else:
        json_data["code"] = "500"
    json_data["inter_type"] = "share"
    ctx["xml_data"] = FbTemplates.time_line_interaction.render(json_data).encode("utf-8")
    xml_node = etree.XML(ctx["xml_data"])
    ctx["pb_data"] = xml2pb(xml_node, "replace", "0", "Ok")
    return gen_response(request, ctx)

@csrf_exempt
@view_fb_exception_handle
def facebook_add_friend(request):
    ctx = fetch_context(request)
    json_data = dict()
    handle_fb_request(request, ctx, json_data, fetch_html=False)
    node_id = request.GET.get("id", "N/A")
    pos_data = list()
    for k, v in request.POST.iteritems():
        pos_data.append("%s=%s" % (k, v))
    ctx["fetch_html_begin_time"] = time.time()
    post_data = request.body
    req = requests.request("POST", ctx["req_url"], headers=net_client.fb_headers, data=post_data, cookies=ctx["req_cookie"])
    #open("addfriend.html", "w+").write(req.text.encode("utf-8"))
    ctx["fetch_html_end_time"] = time.time()
    ctx["rsp_url"] = req.url
    ctx["rsp_html"] = req.text
    ctx["rsp_cookie"] = ctx["req_cookie"]
    rsp_url = req.url
    if rsp_url.find("m.facebook.com/login.php") >= 0:
        json_data["code"] = "500"
    else:
        if req and req.status_code == 200:
            ret = handle_add_friend(req.text)
            if ret == 1:
                json_data["code"] = "200"
            else:
                json_data["code"] = "201"
        else:
            json_data["code"] = "500"
    json_data["inter_type"] = "add_friend"
    ctx["xml_data"] = FbTemplates.time_line_interaction.render(json_data).encode("utf-8")
    xml_node = etree.XML(ctx["xml_data"])
    ctx["pb_data"] = xml2pb(xml_node, "replace", "0", req.text)
    return gen_response(request, ctx)


@csrf_exempt
@view_fb_exception_handle
def facebook_fan_like(request):
    ctx = fetch_context(request)
    json_data = dict()
    handle_fb_request(request, ctx, json_data, fetch_html=False)
    node_id = request.GET.get("id", "N/A")
    pos_data = list()
    for k, v in request.POST.iteritems():
        pos_data.append("%s=%s" % (k, v))
    ctx["fetch_html_begin_time"] = time.time()
    post_data = request.body
    req = requests.request("POST", ctx["req_url"], params=ctx["req_params"], headers=net_client.fb_headers, data=post_data, cookies=ctx["req_cookie"])
    #open("fanlike.html", "w+").write(req.text.encode("utf-8"))
    ctx["fetch_html_end_time"] = time.time()
    ctx["rsp_url"] = req.url
    ctx["rsp_html"] = req.text
    ctx["rsp_cookie"] = ctx["req_cookie"]
    if req and req.status_code == 200:
        json_data["code"]="200"
    else:
        json_data["code"] = "500"
    json_data["inter_type"] = "fan_like"
    ctx["xml_data"] = FbTemplates.time_line_interaction.render(json_data).encode("utf-8")
    xml_node = etree.XML(ctx["xml_data"])
    ctx["pb_data"] = xml2pb(xml_node, "replace", "0", "Ok")
    return gen_response(request, ctx)



@csrf_exempt
@view_fb_exception_handle
def facebook_friend_xout(request):
    ctx = fetch_context(request)
    json_data = dict()
    handle_fb_request(request, ctx, json_data, fetch_html=False)
    node_id = request.GET.get("id", "N/A")
    pos_data = list()
    for k, v in request.POST.iteritems():
        pos_data.append("%s=%s" % (k, v))
    ctx["fetch_html_begin_time"] = time.time()
    post_data = request.body
    req = requests.request("POST", ctx["req_url"], params=ctx["req_params"], headers=net_client.fb_headers, data=post_data, cookies=ctx["req_cookie"])
    open("./xout.html", "w+").write(req.text.encode("utf-8"))
    ctx["fetch_html_end_time"] = time.time()
    ctx["rsp_url"] = req.url
    ctx["rsp_html"] = req.text
    ctx["rsp_cookie"] = ctx["req_cookie"]
    if req and req.status_code == 200:
        json_data["code"]= "200"
    else:
        json_data["code"] = "500"
    #json_data["inter_type"] = "fan_like"
    #ctx["xml_data"] = FbTemplates.time_line_interaction.render(json_data).encode("utf-8")
    #xml_node = etree.XML(ctx["xml_data"])
    ctx["pb_data"] = xml2pb(None, "replace", "0", "Ok")
    return gen_response(request, ctx)