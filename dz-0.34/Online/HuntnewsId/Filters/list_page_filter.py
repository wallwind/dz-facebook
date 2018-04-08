list_item_filter = {
    "text": "a/div/h3/text()|a/h3/text()|a/div[@class='w-list-topic-title']/text()",
    "href": "url(a/@href)",
    "data_offset": "@data-offset",
    "?img": "url(a/div/img/@src)",
    "?time": "a/div/div/span[@class='w-list-time']/text()|a/div/span[@class='w-list-time']/text()",
    "?views": "a/div/div/span[@class='w-list-view']/text()|a/div/span[@class='w-list-view']/text()",
    "?tag": "a/div/div/span[contains(@class, 'w-list-symbol')]/text()",
    "?index": "@data-index",
    "?img_list": {
        "@base": "a/ul/li",
        "@list": {
            "@value": "url(img/@data-src)"
        }
    }
}

list_page_filter = {"?org_title": "//title/text()",
                    "tabs": {"@base": "//div[@class='tab-table']/div[@class='tab-row']/a",
                             "@list": {
                                 "text": "span/text()",
                                 "href": "url(@href)",
                                 "?focus": "contains(@class, 'focus')"}
                             },
                    "items": {
                        "@base": "//div[@class='p-index-list']/div/div/section",
                        "@list": list_item_filter
                    },
                    "list_key": "//a[contains(@class, 'focus')]/@data-key",
                    "first_pos": "//div/@first-pos",
                    "last_pos": "//div/@last-pos",
                    "list_chncat": "//div/@data-chncat"
                    }

list_node_filter = {
    "items": {
        "@base": "//div[@data-pagelet='list.items']/div/section",
        "@list": list_item_filter
    },
    "first_pos": "//div/@first-pos",
    "last_pos": "//div/@last-pos"
}

simple_list_page_filter = {"?org_title": "//title/text()",
                           "items": {
                               "@base": "//div[@class='p-list-list']/div/div/section",
                               "@list": list_item_filter
                           },
                           "first_pos": "//div/@first-pos",
                           "last_pos": "//div/@last-pos",
                           "list_chncat": "//div/@data-chncat",
                           "list_key": "//div/@data-channel",
                           "?title": "//span[@class='w-nav-title']/text()",
                           "?subtitle": "//div[@class='p-list-title']/h2/text()"
                           }
