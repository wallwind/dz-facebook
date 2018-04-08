import os
import re
from jinja2 import FileSystemLoader
from jinja2.environment import Environment, Undefined
env = Environment()
template_path = os.path.dirname(os.path.abspath(__file__)) + "/../../templates/"
env.loader = FileSystemLoader(template_path)
from urllib import quote
import Filters as FbFilters
import  json
def url_img_filter(text=""):
    match = FbFilters.filter_image_url_reg.match(text)
    if match:
        return match.groupdict().get("url")
    return text
def add_facebook_domain(text=""):
    return "https://m.facebook.com"+text

def spilt_share(href=""):
    hlist = href.split('?')
    if len(hlist) == 2:
        return hlist[1]
    return href


def get_share_id(data_store=""):
    json_data = json.loads(data_store)
    if json_data.has_key('share_id'):
        return json_data['share_id']
    return ""

def get_video_src(data_store=""):
    json_data = json.loads(data_store)
    if json_data.has_key('src'):
        return json_data['src']
    return ""
def internal_preview_image_id(data_store=""):
    json_data = json.loads(data_store)
    if json_data.has_key('internal_preview_image_id'):
        return json_data['internal_preview_image_id']
    return " "

def get_feedback_target(data_store=""):
    json_data = json.loads(data_store)
    if json_data.has_key('feedbackTarget'):
        return json_data['feedbackTarget']
    return " "

def get_like_btn_url(data_store=""):
    json_data = json.loads(data_store)
    if json_data.has_key('url'):
        return json_data['url']
    return " "

def get_fan_like_url(data_store=""):
    json_data = json.loads(data_store)
    if json_data.has_key('url'):
        return json_data['url']
    return " "

def data_store_to_str(data_store=""):
    if data_store:
        json_data = json.loads(data_store)
        if json_data:
            list_data = list()
            for key in json_data:
                if key == 'el':
                    continue
                list_data.append("%s=%s" % (key, json_data[key]))
            ret_data = '&'.join(list_data)
            return ret_data
    return ''

def cancel_data_store_to_str(data_store=""):
    if data_store:
        json_data = json.loads(data_store)
        if json_data:
            list_data = list()
            for key in json_data:
                if key == 'id':
                    list_data.append("%s=%s" % ("subject_id", json_data[key]))
                    continue
                list_data.append("%s=%s" % (key, json_data[key]))
            ret_data = '&'.join(list_data)
            return ret_data
    return ''

def url_encode(data=""):
    return quote(data)


def get_img_width(data=""):
    if data:
        str = data.replace(':',';')
        str_list = str.split(';')
        return str_list[1]
    return "0px"

def get_img_height(data=""):
    if data:
        str = data.replace(':',';')
        str_list = str.split(';')
        return str_list[3]
    return "0px"


def get_imgs_top(data=""):
    if data:
        str = data.replace(':',';')
        str_list = str.split(';')
        return str_list[1]
    return "0px"

def get_imgs_left(data=""):
    if data:
        str = data.replace(':',';')
        str_list = str.split(';')
        return str_list[3]
    return "0px"

def get_imgs_width(data=""):
    if data:
        str = data.replace(':',';')
        str_list = str.split(';')
        return str_list[5]
    return "0px"

def get_imgs_height(data=""):
    if data:
        str = data.replace(':',';')
        str_list = str.split(';')
        return str_list[7]
    return "0px"

def get_imgs_height(data=""):
    if data:
        str = data.replace(':',';')
        str_list = str.split(';')
        return str_list[7]
    return "0px"

def share_url_img_width_filter(text=""):
    match = FbFilters.filter_share_width_img_reg.match(text)
    if match:
        return match.groupdict().get("width")
    return "0px"
def share_url_img_height_filter(text=""):
    match = FbFilters.filter_share_height_img_reg.match(text)
    if match:
        return match.groupdict().get("height")
    return "0px"

def fb_str_strip(text=""):
    return text.strip()

env.filters['get_video_src'] = get_video_src
env.filters['get_like_btn_url'] = get_like_btn_url
env.filters['get_fan_like_url'] = get_fan_like_url
env.filters['data_store_to_str'] = data_store_to_str
env.filters['cancel_data_store_to_str'] = cancel_data_store_to_str
env.filters['get_feedback_target'] = get_feedback_target
env.filters['fb_str_strip'] = fb_str_strip

env.filters['share_url_img_width_filter'] = share_url_img_width_filter
env.filters['share_url_img_height_filter'] = share_url_img_height_filter

env.filters['get_imgs_height'] = get_imgs_height
env.filters['get_imgs_width'] = get_imgs_width
env.filters['get_imgs_left'] = get_imgs_left
env.filters['get_imgs_top'] = get_imgs_top
env.filters['get_img_width'] = get_img_width
env.filters['get_img_height'] = get_img_height
env.filters['url_encode'] = url_encode
env.filters['internal_preview_image_id'] = internal_preview_image_id
env.filters['get_share_id'] = get_share_id
env.filters['url_img_filter'] = url_img_filter
env.filters['add_facebook_domain'] = add_facebook_domain
env.filters['spilt_share'] = spilt_share

time_line_template = env.get_template("./fb_time_line.xml")
time_line_interaction = env.get_template("./facebook_interaction.xml")
time_line_login = env.get_template("./facebook_login.xml")
time_line_more = env.get_template("./fb_time_line_more.xml")
