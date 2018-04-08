content_page_more_text_filter = {
    "?p_list": {
        "@base": "//div[@data-pagelet='article.page']/div/p",
        "@list": {
            "@value": "string()"
        }
    }
}

content_page_hot_list_filter = {
        "item_list": {
            "@base": "//div[@class='w-list-fragment']/section",
            "@list": {
                "text": "a/div/h3/text()|a/h3/text()|a/div[@class='w-list-topic-title']/text()",
                "href": "url(a/@href)",
                "data_offset": "@data-offset",
                "?img": "a/div/img/@src",
                "?time": "a/div/div/span[@class='w-list-time']/text()|a/div/span[@class='w-list-time']/text()",
                "?views": "a/div/div/span[@class='w-list-view']/text()|a/div/span[@class='w-list-view']/text()",
                "?flag": "a/div/div/span[contains(@class, 'w-list-symbol')]/text()",
                "?percent": "a/div/div/span[@class='w-list-percent']/label/text()|a/div/span[@class='w-list-percent']/label/text()",
                "?meta": "a/div/div/span[@class='w-list-percent']/text()|a/div/span[@class='w-list-percent']/text()",
                "?img_list": {
                    "@base": "a/ul/li",
                    "@list": {
                        "@value": "url(img/@data-src)"
                    }
                }
            }
        },
        "?next_page": "//div[@data-nextpage]/@data-nextpage",
        "?first_page": "//div[@data-firstpage]/@data-firstpage",
        "?cat": "//div[@data-hotcategory]/@data-hotcategory",
        "?more_btn_text": "//div[@data-hotcategory]/text()",
        "?first_pos": "//div/@first-pos",
        "?last_pos": "//div/@last-pos",
        "?list_chncat": "//div/@data-chncat",
        "?list_key": "//div/@data-channel"
    }

content_page_filter = {
    "?org_title": "//title/text()",
    "news": {
        "@base": "//div[@class='w-article']",
        "title": "h1[@class='w-article-title']/text()",
        "id": "//div[@class='w-article']/@data-id",
        "?time": "div[@class='w-article-meta']/span[@class='w-article-time']/text()",
        "?from": "div[@class='w-article-meta']/a[@class='w-article-from']/text()",
        "?content": {
            "@base": "div[@class='w-article-main']/div[@class='w-article-pages']",
            "?img": {"@base": "section[@class='w-article-content']/div[@class='w-article-cover']/div/img[@src]"
                              + "|section[@class='w-article-content']/div[@class='w-article-image']/img[@src]"
                              + "|section[@class='w-article-content']/resource[@optimalurl]"
                              + "|section[@class='w-article-content']/resource[@originalurl]",
                     "src": "@src|@optimalurl|@originalurl",
                     "?width": "@img-width",
                     "?height": "@img-height"
                     },
            "?p_list": {
                "@base": "section[@class='w-article-content']/p/res-image/@id|section[@class='w-article-content']/p",
                "@list": {
                    "@value": "strip(string())"
                }
            },
            "?p_text": {
                "@base": "section[@class='w-article-content']",
                "@value": "strip(string())"},
            "?ext_content": {
                "more_btn_text": "section[@class='w-article-extcontent']/div[@error]/text()"
            },
            "ss": "string()",
            "?img_list": {
                "@base": "//resource",
                "@list": {
                    "id": "@id",
                    "url": "@optimalurl",
                    "?width": "@optimalwidth",
                    "?height": "@optimalheight"
                }
            },
            "?img_list_key": {
                "@base": "//resource",
                "@list": {
                    "@value": "@id"
                }
            }

        },
        "?prev_btn": {
            "@base": "div[@class='w-article-news-btns']/a[@data-label='prev_article']",
            "text": "text()",
            "href": "url(@href)"
        },
        "?next_btn": {
            "@base": "div[@class='w-article-news-btns']/a[@data-label='next_article']",
            "text": "text()",
            "href": "url(@href)"
        }
    },
    "?more_list": {
        "@base": "//div[@id='related']",
        "text": "div/label/text()",
        "item_list": {
            "@base": "div/div[@class='w-list-fragment']/section",
            "@list": {
                "text": "a/div/h3/text()|a/h3/text()|a/div[@class='w-list-topic-title']/text()",
                "href": "url(a/@href)",
                "?data_offset": "@data-offset",
                "?img": "a/div/img/@src",
                "?time": "a/div/div/span[@class='w-list-time']/text()|a/div/span[@class='w-list-time']/text()",
                "?percent": "a/div/div/span[@class='w-list-percent']/label/text()|a/div/span[@class='w-list-percent']/label/text()",
                "?meta": "a/div/div/span[@class='w-list-percent']/text()|a/div/span[@class='w-list-percent']/text()",
                "?img_list": {
                    "@base": "a/ul/li",
                    "@list": {
                        "@value": "url(img/@data-src)"
                    }
                }
            }
        },
        "?ext_item": {
            "@base": "div/div[@class='p-detail-related-more']",
            "?text": "div[@class='w-more-btn']/text()",
            "?item_list": {
                "@base": "div[@class='p-detail-related-list']/div[@class='w-list-fragment']/section",
                "@list": {
                    "text": "a/div/h3/text()|a/h3/text()|a/div[@class='w-list-topic-title']/text()",
                    "href": "url(a/@href)",
                    "?data_offset": "@data-offset",
                    "?img": "a/div/img/@src",
                    "?time": "a/div/div/span[@class='w-list-time']/text()|a/div/span[@class='w-list-time']/text()",
                    "?percent": "a/div/div/span[@class='w-list-percent']/label/text()|a/div/span[@class='w-list-percent']/label/text()",
                    "?meta": "a/div/div/span[@class='w-list-percent']/text()|a/div/span[@class='w-list-percent']/text()",
                    "?img_list": {
                        "@base": "a/ul/li",
                        "@list": {
                            "@value": "url(img/@data-src)"
                        }
                    }
                }
            }
        }
    },
    "?hot_list": {
        "@base": "//div[@id='hotnews']",
        "text": "div/label/text()",
        "item_list": {
            "@base": "div/div[@class='w-list-fragment']/section",
            "@list": {
                "text": "a/div/h3/text()|a/h3/text()|a/div[@class='w-list-topic-title']/text()",
                "href": "url(a/@href)",
                "data_offset": "@data-offset",
                "?img": "a/div/img/@src",
                "?time": "a/div/div/span[@class='w-list-time']/text()|a/div/span[@class='w-list-time']/text()",
                "?views": "a/div/div/span[@class='w-list-view']/text()|a/div/span[@class='w-list-view']/text()",
                "?flag": "a/div/div/span[contains(@class, 'w-list-symbol')]/text()",
                "?img_list": {
                    "@base": "a/ul/li",
                    "@list": {
                        "@value": "url(img/@data-src)"
                    }
                }
            }
        },
        "next_page": "div[@data-nextpage]/@data-nextpage",
        "first_page": "div[@data-firstpage]/@data-firstpage",
        "cat": "div[@data-hotcategory]/@data-hotcategory",
        "more_btn_text": "div[@data-hotcategory]/text()"
    },
    "?next_list": {
        "@base": "//div[@id='nextnews']",
        "text": "div/label/text()",
        "item_list": {
            "@base": "div/div[@class='w-list-fragment']/section",
            "@list": {
                "text": "a/div/h3/text()|a/h3/text()|a/div[@class='w-list-topic-title']/text()",
                "href": "url(a/@href)",
                "data_offset": "@data-offset",
                "?img": "a/div/img/@src",
                "?time": "a/div/div/span[@class='w-list-time']/text()|a/div/span[@class='w-list-time']/text()",
                "?views": "a/div/div/span[@class='w-list-view']/text()|a/div/span[@class='w-list-view']/text()",
                "?flag": "a/div/div/span[contains(@class, 'w-list-symbol')]/text()",
                "?percent": "a/div/div/span[@class='w-list-percent']/label/text()|a/div/span[@class='w-list-percent']/label/text()",
                "?meta": "a/div/div/span[@class='w-list-percent']/text()|a/div/span[@class='w-list-percent']/text()",
                "?img_list": {
                    "@base": "a/ul/li",
                    "@list": {
                        "@value": "url(img/@data-src)"
                    }
                }
            }
        },
        "first_pos": "//div/@first-pos",
        "last_pos": "//div/@last-pos",
        "list_chncat": "//div/@data-chncat",
        "list_key": "//div/@data-channel",
        "more_btn_text": "div[@data-label='morebtn']/text()"
    },
    "?site_map": {
        "@base": "//div/div[@class='sitemap']/..",
        "title": "div[@class='widget-title']/label/text()",
        "?item_list": {
            "@base": "div[@class='sitemap']//a",
            "@list": {
                "text": "text()",
                "href": "url(@href)"
            }
        }
    },
    "?footer": {
        "@base": "//div[@class='w-footer']",
        "from": {
            "text": "a[1]/text()",
            "href": "url(a[1]/@href)"},
        "feedback": {
            "text": "a[2]/text()",
            "href": "url(a[2]/@href)"},
    }
}
