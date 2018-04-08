# coding=utf-8
import requests
from Uclite.settings import proxies
from requests.exceptions import ConnectionError
from urlparse import urlparse
import json
import re
import logging

no_cache_headers = {"Pragma": "no-cache",
                    "Cache-Control": "no-cache"}

fb_headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"
    #"X-UCBrowser-UA": "dv(Nexus 4);pr(UCBrowser/10.1.0.527);ov(Android 4.2.2);ss(360*640);pi(768*1184);bt(UC);pm(0);bv(0);nm(0);im(0);sr(0);nt(2);dn(14428870263-d38c07e8);ai(720089404747345);"
    #"User-Agent": "Mozilla/5.0 (Linux; U; Android 4.3; en-US; C6833 Build/14.2.A.0.290) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.9.8.770 U3/0.8.0 Mobile Safari/534.30"
}


def get_html(url, cookies=None, cache_enable=False):
    from Online.views import UcliteException
    if cache_enable:
        headers = None
    else:
        headers = no_cache_headers
    if cookies is None:
        cookies = dict()
    try:
        req = requests.request("GET", url, headers=headers, proxies=proxies, cookies=cookies)
    except ConnectionError as _:
        if proxies:
            try:
                req = requests.request("GET", url, headers=headers, proxies=None, cookies=cookies)
            except Exception as e:
                raise UcliteException(code=501, message=e.message)
    except Exception as e:
        raise UcliteException(code=501, message=e.message)
    if req and req.text and 200 <= req.status_code < 400:
        # 临时处理,非huntnews.id降级
        if not urlparse(req.url).netloc.endswith("huntnews.id"):
            raise UcliteException(code=501, message="NOT in huntnews.id")
        return req.url, req.text, req.cookies
    else:
        raise UcliteException(code=req.status_code >= 400 and req.status_code or 501, message=req.reason)


def post_data(url, data, cookies=None):
    from Online.views import UcliteException
    if cookies is None:
        cookies = dict()
    try:
        req = requests.request("POST", url, headers=no_cache_headers, data=data, cookies=cookies)
    except Exception as e:
        raise UcliteException(code=501, message=e.message)
    if req and req.status_code == 200:
        return req.url, req.text, req.cookies
    else:
        raise UcliteException(code=req.status_code >= 400 and req.status_code or 501, message=req.reason)


def get_fb_html(url, cookies=None, cache_enable=False):
    from Online.views import UcliteException
    if cache_enable:
        headers = None
    else:
        headers = fb_headers
    if cookies is None:
        cookies = dict()
    try:
       #req = requests.request("get", url, cookies=cookies, verify=True)
       # e_url = "https://m.facebook.com/login/async/?next=https%3A%2F%2Fm.facebook.com%2Fhome.php%3Fsoft%3Dbookmarks&refsrc=https%3A%2F%2Fm.facebook.com%2F&lwv=100"
       # e_data = "email=+8618627905091&pass=fjdlj111."
       # pst_r = requests.request("POST", e_url, headers=fb_headers, data=e_data)
       # cookies =pst_r.cookies
       #headers = {
       #   "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"}

       #loginText = pst_r.text
       ##open("./home.html", "w+").write(loginText[9:].encode("utf-8"))
       #reJson = handle_facebook_json("script",loginText)
       #open("./code.html", "w+").write(reJson.encode("utf-8"))
       #print "login_cookies", pst_r.cookies
       #for k,v in pst_r.cookies.iteritems():
       #    print"key:%s = %s",k,v

       get_url = "https://m.facebook.com/stories.php"
       req = requests.request("get", get_url, headers=fb_headers, cookies=cookies, verify=True)
       #all_text = open("./facebook.html", "r").read().decode("utf-8")
       #open("./facebook.html", "w+").write(req.text.encode("utf-8"))

    except ConnectionError as _:
        if proxies:
            try:
                req = requests.request("GET", url, headers=headers, proxies=None, cookies=cookies)
            except Exception as e:
                raise UcliteException(code=501, message=e.message)
    except Exception as e:
        raise UcliteException(code=501, message=e.message)
    if req and req.text and 200 <= req.status_code < 400:
        # 临时处理,非huntnews.id降级
        if not urlparse(req.url).netloc.endswith("facebook.com"):
            raise UcliteException(code=501, message="NOT in facebook.com")
        return req.url,req.text, req.cookies
    else:
        raise UcliteException(code=req.status_code >= 400 and req.status_code or 501, message=req.reason)



def fb_post_data(url, data, cookies=None):
    from Online.views import UcliteException
    if cookies is None:
        cookies = dict()
    try:
        req = requests.request("POST", url, headers=fb_headers, data=data, cookies=cookies)
    except Exception as e:
        raise UcliteException(code=501, message=e.message)
    if req and req.status_code == 200:
        return req.url, req.text, req.cookies
    else:
        raise UcliteException(code=req.status_code >= 400 and req.status_code or 501, message=req.reason)


def facebook_login(urls,param):
    from Online.views import UcliteException
    e_url = "https://m.facebook.com/login/async/?next=https%3A%2F%2Fm.facebook.com%2Fhome.php%3Fsoft%3Dbookmarks&refsrc=https%3A%2F%2Fm.facebook.com%2F&lwv=100"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"}
    params = {
        'email': 'wallwind@qq.com',
        'pass': 'wcl123456'
    }
    try:
        req = requests.request("POST", e_url, headers=headers, data=params)
    except Exception as e:
        raise UcliteException(code=501, message=e.message)
    if req and req.status_code == 200 :
        return req.url,req.text,req.cookies
    else:
        raise UcliteException(code=req.status_code >= 400 and req.status_code or 501, message=req.reason)




if __name__ == '__main__':
    e_url = "http://www.huntnews.id/api/feedback?uc_param_str=dnfrpfbivesscpgimibtbmntnisieijblauputoggdnw&type=index"
    e_data = "reasons=&detail=AAAAAAAAAAAAAAAAAAAAAAAAAAA&url=http%3A%2F%2Fwww.huntnews.id%2Fp%2Fdetail%2F9c7b92533f13c8e16585c4f62c68351a%3Fuc_param_str%3Ddnfrpfbivesscpgimibtbmntnisieijblauputoggdnw%26pos%3D1459491457570%26channel%3Dother%26chncat%3Dcategory_indonesian%26_prefetch%3D1"
    print post_data(e_url, e_data)
