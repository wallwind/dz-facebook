import os
from jinja2 import FileSystemLoader
from jinja2.environment import Environment, Undefined
env = Environment()
template_path = os.path.dirname(os.path.abspath(__file__)) + "/../../templates/"
env.loader = FileSystemLoader(template_path)


def img_ratio(width=None, height=None):
    try:
        return float(width) / float(height)
    except:
        return "1.67"


def str_strip(text=""):
    return text.strip()


env.filters['img_ratio'] = img_ratio
env.filters['strip'] = str_strip

list_page_template = env.get_template("./list_page.xml")
simple_list_page_template = env.get_template("./simple_list_page.xml")
content_page_template = env.get_template("./content_page.xml")
content_page_more_template = env.get_template("./content_page_more.xml")
content_page_hot_list_template = env.get_template("./content_page_hot_list.xml")
content_page_next_list_template = env.get_template("./content_page_next_list.xml")
list_node_template = env.get_template("./list_page_list.xml")
index_feedback_template = env.get_template("./index_feedback.xml")
detail_feedback_template = env.get_template("./detail_feedback.xml")
web_view_template = env.get_template("./web_view.xml")
