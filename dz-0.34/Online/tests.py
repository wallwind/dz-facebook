from django.test import TestCase

# Create your tests here.

# import requests
# import json
#
# header_str = """Connection: keep-alive
# Pragma: no-cache
# Cache-Control: no-cache
# Accept: application/json
# X-Pagelets: list.items"""
#
#
# header_list = header_str.splitlines()
# headers = {}
# for h in header_list:
#     k, v = h.split(": ")
#     headers[k] = v
#
# req = requests.get("http://www.huntnews.id/w/list/headlines?_fetch_more=1&size=20&chncat=tags_indonesian&_fetch_type=pos&channel=headlines&renderarg=&_pos=1458808020015&uc_param_str=dnfrpfbivesscpgimibtbmntnisieijblauputoggdnw&_pagelets=list.items&_t=0.6513744375655894",
#                    headers=headers)
# print json.loads(req.text)["html"]["list.items"]


s = "\u00e3\u0080\u008c\u00e9\u0080\u0099\u00e5\u00b0\u00b1\u00e5\u0083\u008f\u00e5\u008f\u00ab\u00e4\u00b8\u0080\u00e5\u0080\u008b\u00e5\u00b0\u008f\u00e5\u00ad\u00a9\u00e8\u00ae\u0080\u00e6\u009b\u00b8\u00e4\u00b8\u0080\u00e6\u00a8\u00a3\u00ef\u00bc\u008c\u00e5\u00b9\u00b3\u00e6\u0099\u0082\u00e6\u0094\u00be\u00e4\u00ba\u0094\u00e5\u00a4\u00a9\u00e5\u0081\u0087\u00ef\u00bc\u008c\u00e5\u0091\u00a8\u00e5\u0085\u00ad\u00e5\u0091\u00a8\u00e6\u0097\u00a5\u00e5\u0086\u008d\u00e4\u00be\u0086\u00e5\u00bf\u00b5\u00e6\u009b\u00b8\u00ef\u00bc\u008c\u00e5\u00ae\u00b6\u00e4\u00b8\u00ad\u00e7\u009a\u0084\u00e5\u00b0\u008f\u00e5\u00ad\u00a9\u00e6\u009c\u0083\u00e6\u009c\u0089\u00e5\u0087\u00ba\u00e6\u0081\u00af\u00e5\u0097\u008e\u00ef\u00bc\u009f\u00e3\u0080\u008d"
print s.decode("utf-8")
