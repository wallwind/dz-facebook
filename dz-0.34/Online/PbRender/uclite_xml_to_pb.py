# coding=utf-8

import uclite_pb2
import logging

name_pb_type_dic = {'page': uclite_pb2.ComPageType,
                    'toolbar': uclite_pb2.ComToolbarType,
                    'tabbar': uclite_pb2.ComTabbarType,
                    'card': uclite_pb2.ComCardType,
                    'news': uclite_pb2.ComNewsType,
                    'flexbox': uclite_pb2.ComFlexboxType,
                    'list': uclite_pb2.ComListType,
                    'button': uclite_pb2.ComButtonType,
                    'text': uclite_pb2.ComTextType,
                    'image': uclite_pb2.ComImageType,
                    'info': uclite_pb2.ComInfoType,
                    'nav': uclite_pb2.ComNavType,
                    'h': uclite_pb2.ComHType,
                    'web': uclite_pb2.ComWebType,
                    'footer': uclite_pb2.ComFooterType,
                    'input': uclite_pb2.ComInputType,
                    'checkbox': uclite_pb2.ComCheckboxType,
                    'readmore': uclite_pb2.ComReadmoreType,
                    'style': uclite_pb2.ComStyleType,
                    'fbcard': uclite_pb2.ComFBCardType,
                    'item': uclite_pb2.ComItemType,
                    }


# 遍历节点
def traverse_node(node, pb):
    pb.type = uclite_pb2.ComTextType
    if node is None:
        return

    # 标签名字
    if node.tag not in name_pb_type_dic:
        logging.warning("not support node '%s'" % node.tag)
        return False
    pb.type = name_pb_type_dic[node.tag]

    # 标签属性
    for key, value in node.attrib.iteritems():
        attr = pb.attrs.add()
        attr.key = key
        attr.value = value

    for sub_node in node:
        if sub_node.tag not in name_pb_type_dic:
            logging.warning("not support node '%s'" % node.tag)
            continue
        sub_pb = pb.children.add()
        traverse_node(sub_node, sub_pb)

    # 标签的值
    if node.text is not None:
        pb.inner_text = node.text


def xml2pb(node, cmd, node_id, msg):
    result = uclite_pb2.Result()
    action = result.actions.add()
    action.cmd = cmd
    action.target = node_id
    action.msg = msg
    component = action.data.add()
    if node is not None:
        traverse_node(node, component)
    else:
        component.type = uclite_pb2.ComTextType
    return result.SerializeToString()
