from lxml import etree
import logging
from urlparse import urljoin


def abs_url(context, url):
    if isinstance(url, (list, tuple)):
        for i, x in enumerate(url):
            url[i] = urljoin(context.context_node.base, x)
    return url


def strip(context, text):
    if isinstance(text, (list, tuple)):
        for i, x in enumerate(text):
            text[i] = x.strip()
    elif isinstance(text, (unicode, str)):
        text = text.strip()
    return text


def run(filter_data, node):
    ns = etree.FunctionNamespace(None)
    if "url" not in ns:
        ns['url'] = abs_url
        ns['strip'] = strip

    is_list = '@list' in filter_data
    node_list = list()
    if '@base' in filter_data:
        base_xpath = filter_data['@base']
        node_list = node.xpath(base_xpath)
        if not is_list and len(node_list) > 0:
            node_list = [node_list[0]]
    elif not is_list:
        node_list.append(node)
    else:
        logging.warning("filter defined error. %s" % repr(filter_data))

    ret_list = list()
    for node in node_list:
        ret_list_item = dict()
        name_list = filter_data.keys()
        name_list.sort()
        for name in name_list:
            ret_item_value = None
            is_list_item = name == "@list"
            is_ret_value = name == "@value"
            if name.startswith("#"):
                continue
            if name.startswith("@") and not is_list_item and not is_ret_value:
                continue
            if name == "?share_from":
                pass
            filter_item_value = filter_data.get(name, None)
            if filter_item_value is None:
                continue
            if isinstance(filter_item_value, dict):
                ret_item_value = run(filter_item_value, node)
            elif isinstance(filter_item_value, (str, unicode)):
                if isinstance(node, (unicode, str)):
                    node = etree.fromstring("<p>%s</p>" % node)

                xpath_ret = node.xpath(filter_item_value)
                if isinstance(xpath_ret, (tuple, list)):
                    for x_item in xpath_ret:
                        if hasattr(x_item, "is_attribute") and x_item.is_attribute:
                            ret_item_value = unicode(x_item)
                        elif hasattr(x_item, "is_text") and x_item.is_text:
                            ret_item_value = unicode(x_item)
                        elif isinstance(x_item, etree._ElementStringResult):
                            ret_item_value = unicode(x_item)
                        else:
                            ret_item_value = etree.tostring(x_item)
                        if len(xpath_ret) > 1:
                            logging.debug("ignore more than one result named: %s" % xpath_ret[0])
                        break
                else:
                    ret_item_value = xpath_ret
            else:
                logging.warning("unspported object: %s" % repr(filter_item_value))

            if is_ret_value:
                return ret_item_value
            if ret_item_value is not None and (not isinstance(ret_item_value, list) or len(ret_item_value) > 0):
                if is_list_item:
                    ret_list_item = ret_item_value
                elif name.startswith("?"):
                    ret_list_item[name[1:]] = ret_item_value
                else:
                    ret_list_item[name] = ret_item_value
            elif not name.startswith("?"):
                ret_list_item = list()
                break
        if ret_list_item:
            ret_list.append(ret_list_item)

    if is_list:
        return ret_list
    elif isinstance(ret_list, list) and len(ret_list) > 0:
        return ret_list[0]
    else:
        return None


def run_html(filter_data, html, base_url):
    try:
        node = etree.HTML(html, base_url=base_url)
    except:
        node = etree.XML(html, base_url=base_url)
    ret = run(filter_data, node)
    if ret is None:
        ret = dict()
    return ret


