
userinfo_header_filter = {
    "@base": "//header",
    "?header_img": "div/div/a/i/@style",
    "?header_other_name": "div/div/div/div/h1",
    "?header_people_name": "div/div/div/div/h3",
}
header_userinfo_filter = {
    "@base": "header|div/header",
    "?user_icon": "div[1]/div/a/i//@style",
    "?header_href": "div/div/a/@href",
    "?user_name": "div/div/div/div/h3",
    "?user_name1": "div/div/div/div/h1",
    "?real_info": {
        "@base": "div/div/div/div/div",
        "@value": "string()",
    },
    "?meta_type": "div/div/div/div/div/span/span/i/@class",
    "?add_friend": "div/div/div/div/div/div/div/a/@href",
    "?friend_data_store": "div/div/div/div/div/div/div/a/@data-store",
    "?like_data_store": "div/div/div/div/div/div/@data-store",
    "?friend_cancle_data_store": "div/div/div/div/div/div/a/@data-store",
}

single_img_filter = {
    "@base": "div/div/a[@class='_39pi']|div/div/div/a[@class='_39pi']",
    "?img": "div/div/i/@style",
    "?url": "@href",
    "?style": "div/div/@style",
}

footer_filter1 = {
    "@base": "footer|div/footer",
    "?shares_lists": {
        "@base": "div/div/a/div/div[2]",
        "?comments": "span[1]/text()",
        "?shares": "span[2]/text()",
    },
    "?comment_url": "div/div/div[2]/a[@class='_15kq _5a-2']/@href",
    "?likecount": "/div/div/a/div/div/div/text()",
    "?fb_dtsg": "//input[@name='fb_dtsg']/@value",
    "?sharecount": "//span[2]/text()",
    "?after_zan": "div/div/a/div/div/div/text()",
    "?aria_pressed": "div/div/div/a/@aria-pressed",
    "?like_data_uri": "div/div/div/a[@data-sigil='touchable ufi-inline-like like-reaction-flyout']/@href",
    "?share_url": "div/div/div[3]/a[@class='_15kr _5a-2']/@href",
    "?share_write_post_url": "div/div/div[3]/a/@href",
    "?share_data_store": "div/div/div[3]/a/@data-store",
    "?like_data_store": "div/div/div/a[@data-sigil='touchable ufi-inline-like like-reaction-flyout']/@data-store"
}
footer_filter = {
    "@base": "footer|div/footer",
    "?shares_lists": {
        "@base": "div/div/a/div/div[2]",
        "?comments": "span[1]/text()",
        "?shares": "span[2]/text()",
    },

    "?likecount": "/div/div/a/div/div/div/text()",
    "?fb_dtsg": "//input[@name='fb_dtsg']/@value",
    "?sharecount": "//span[2]/text()",
    "?after_zan": "div/div/a/div/div/div/text()",
    "?aria_pressed": "div/div/div/a/@aria-pressed",
    "?comment_url": "div/div/div/a[@data-sigil='feed-ufi-focus feed-ufi-trigger ufiCommentLink mufi-composer-focus']/@href",
    "?like_data_uri": "div/div/div/a[@data-sigil='touchable ufi-inline-like like-reaction-flyout']/@href",
    "?share_url": "div/div/div/a[@data-sigil='share-popup']/@href",
    "?like_data_uri1": "div/div/div[1]/a/@data-uri",
    "?share_write_post_url": "div/div/div/a[@data-sigil='share-popup']/@href",
    "?share_data_store": "div/div/div/a[@data-sigil='share-popup']/@data-store",
    "?like_data_store": "div/div/div/a[@data-sigil='touchable ufi-inline-like like-reaction-flyout']/@data-store"
}
article_filter = {
             "?header_title":{
                    "@base":"header",
                     "?title":"div/div/div/div/h1",
                     "?title1": "div/div/div/div/h3",
                     "?title2": "text()",
                },
                "?header_title1": "div/div/div/div/div/div//div[@class='_5qfd']/text()",

                "?card_user_header": {
                    "@base": "div",
                    "@value": header_userinfo_filter,
                },
                "?one_nest": {
                    "@base": "div/div/article/div/div",
                    "?header": header_userinfo_filter,
                    "?nest_content_img": {
                        "@base": "div/div/a",
                         "?href":"@href",
                         "?url": "div/div/i/@style",
                         "?style":"div/div/@style"
                    },
                },

                "?content_img": {
                    "@base": "div",
                    "@value": single_img_filter,
                },
                "?content_imgs": {
                    "@base": "div/div/div/div/a",
                    "@list": {
                        "?img_style": "@style",
                        "?img_href": "@href",
                        "?img_url": "div/i/@style",
                    }
                },
                "?content": "div/div/span/p|div/div/div/span/p",
                "?share_info": {
                    "@base": "div/div/section",
                    "@list": {
                        "?share_portrait": "div/div/i/@style",
                        "?share_title": "div/div/div/header/h3/text()",
                        "?share_intro": "div/div/div/header/h4/text()",
                        "?share_title1": "div/div/header/h3/text()",
                        "?share_intro1": "div/div/header/h4/text()",
                        "?share_title2": "div/div/header/h1[1]/text()",
                        "?share_intro2": "div/div/header/h1[2]/text()",
                        "?share_from": "div/div/div/div/text() |div/div/div/text() ",

                        "?share_content_href": "a/@href",
                        "?share_content": "/div/div//p/text()",
                        "?share_image": "div/div[@class='_5s61 _4ogd _5yki _4prr']//i/@style",
                        "?share_image1": "div[@class='_5s61 _4ogd _5yki _4prr _4o5i']//i/@style",
                        "?share_image_play": "div/div[@class='_5s61 _4ogd _5yki _4prr']//i[2]/@style",
                        "?share_button": "div/div/div/a/button/span/text()",
                    },
                },

                "?video_card": {
                    "@base": "div/div/div/div/div",
                    "@list": {
                        "?data-store": "@data-store",
                        "?video-src": "video/@src",
                        "?video-image": "i/@style",
                        "?width": "video/@width",
                        "?height": "video/@height",
                    }
                },
                "?slice_card": {
                    "@base": "div/div/div/div/div",
                    "@list": {
                        "?like_this": "div/div[@class='_5qfd']/text()",
                        "?user_header_href": "div/div/a/@href",
                        "?user_header_img": "div/div/a/i/@style",
                        "?user_name": "div/div/div/a/span",
                        "?user_name_href": "div/div/div/a/@href",
                        "?content": "div/a/div/text()",
                        "?content_img": "div/div/a/div/i/@style",
                        "?info": "div/div/div/div[@class='_5qfr']/text()",
                        "?down_img_content": "div/div/div/div/a/div/header/div/span/text()",
                        "?down_img_content2": "div/div/div/div/a/div/header/div[@class='_5qfq']/text()"
                    },
                },
                "?footer": footer_filter,
            }

time_line_filter = {
    "?org_title": "//title/text()",
    "?input_list": {
        "@base": "//div[@id='page']/div/div",
        "?action": "//form/@action",
        "?image": "//form//i[@class='img profpic']/@style",
        "?head_img": "//form/div/div/label/div/div/a/i/@style",
        "?head_href": "//form/div/div/label/div/div/a/@href",
        "?fb_dtsg": "//form/input[@name='fb_dtsg']/@value",
        "?privacyx": "//form/input[@name='privacyx']/@value",
        "?target": "//form/input[@name='target']/@value",
        "?c_src": "//form/input[@name='c_src']/@value",
        "?cwevent": "//form/input[@name='cwevent']/@value",
        "?referrer": "//form/input[@name='referrer']/@value",
        "?ctype": "//form/input[@name='ctype']/@value",
        "?cver": "//form/input[@name='cver']/@value",
        "?rst_icv": "//form/input[@name='rst_icv']/@value",
        "?add_photo": "//form/div/div/div/span/button[1]/@value",
        "?location": "//form/div/div/div/span/button[2]/@value",
        "?overview": "//form/div/div/div/span/button[3]/@value",
        "?privacy": "//form/div/div/div/button/span/span/i[1]/@style",
    },

    "?friend_card_list": {
        "@base": "//div[@id='page']/div/div/article",
        "?header": "header/div/h3/text()",
        "?add_friend_list": {
            "@base": "div/div/div/div",
            "@list": {
                "?image": "i/@style",
                "?name": "div/div/h3/a/text()|div/div/h1/a/text()",
                "?href": "div/div/h3/a/@href|div/div/h1/a/@href",
                "?tips": "div/div/div/div/div/text()",
                "?add_friend_href": "div/div/div/div/div/a/@href",
                "?add_friend_data_store": "div/div/div/div/div/a/@data-store",
                "?cancel_friend": "div/div/div/div/a/@data-store",
                "?xout": "a/@href",
                "?button_text": "div/div/a/button/span/text() |div/div/div/div/a/button/span/text()",
            }
        },
        "?more": "//article[@data-sigil='story-div']/footer//a/@href",
        "?morename": "//article[@data-sigil='story-div']/footer//a/text()",
    },
    "?aftercursor": "//div[@id='page']/div/div/div[@class ='_5v-l fullwidthMore apl']/@id",
    "?fb_dtsg": "//input[@name='fb_dtsg']/@value",
    "?privacyx": "//input[@name='privacyx']/@value",
    "?section_list": {
        "@base": "//div[@id='page']/div/div/section",
        "@list": {
            "?card_list": {
                "@base": "article",
                "@list": {
                    "?header_title": {
                        "@base": "header[@class='_4g33 _ung _5qc1']|div/header[@class='_4g33 _ung _5qc1']",
                        "?title": "div/div/div/div/h1",
                        "?title1": "div/div/div/div[@class='_4g34']/h3",
                        "?title2": "text()",
                    },

                    "?header_title1": "div/div/div/div/div/div//div[@class='_5qfd']/text()",
                    "?card_user_header": {
                        "@base": "div",
                        "@value": header_userinfo_filter,
                    },
                    "?one_nest": {
                        "@base": "div/div/article/div/div |div/div/div/article/div/div",
                        "?header": header_userinfo_filter,
                        "?nest_content_img": {
                            "@base": "div/div/a|div/div/div/a",
                            "?href": "@href",
                            "?url": "div/div/i/@style",
                            "?style": "div/div/@style"
                        },
                        "?nest_card": {
                            "?content": "div/span",
                            "?imgurl": "div/section/div/div/i/@style",
                            "?title": "div/section/div/div/header/h1[1]/text()",
                            "?desc": "div/section/div/div/header/h1[1]/text()",
                            "?time": "div/section/div/div/div/text()",
                            "?vido_url": "div/div/div/div/i/@style",
                            "?vido_datastore": "div/div/div/div/@data-store",

                        },
                        "?nest_content_mutil_imgs": {
                            "@base": "div/div/div/a",
                            "@list": {
                                "?url": "div/i/@style",
                                "?style": "div/@style",
                                "?href": "@href",
                                "?a_style": "@style",
                            },
                        },
                        "?content": "div/span|div/div/span",
                    },

                    "?content_img": {
                        "@base": "div",
                        "@value": single_img_filter,
                    },
                    "?content_imgs": {
                        "@base": "div/div[@class='_5rgu']/div/div/a | div/div/div[@class='_5rgu']/div/div/a",
                        "@list": {
                            "?img_style": "@style",
                            "?img_href": "@href",
                            "?img_url": "div/i/@style",
                        }
                    },
                    "?content": "div/div/span |div/span|span|div/div/div/span",
                    "?focus_card": {
                        "@base": "div/section",
                        "?img": "div/i/@style",
                        "?role_img": "div/div/i/@style",
                        "?role_name": "div/div/header/h1[1]/text()",
                        "?role_desc": "div/div/header/h1[2]/text()",
                        "?role_like": {
                            "@base": "div/div/div/span",
                            "@value": "string()",
                        },
                        "?like_button": "div/div/div/div/@data-store",
                        "?add_friend_href": "div/div/div/div/div/a/@href",
                        "?add_friend_store": "div/div/div/div/div/a/@data-store",
                        "?cancel_friend_store": "div/div/div/div/a/@data-store",
                        "?card_href": "a/@href"
                    },
                    "?share_info": {
                        "@base": "div/div/section",
                        "?share_portrait": "div/div/i/@style",
                        "?share_title": "div/div/div/header/h3/text() |div/div/div/header/h1/text()",
                        "?share_intro": "div/div/div/header/h4/text()",
                        "?share_title1": "div/div/header/h3/text()",
                        "?share_intro1": "div/div/header/h4/text()",
                        "?share_title2": "div/div/header/h1[1]/text()",
                        "?share_intro2": {
                            "@base": "div/div/header/h1[2] ",
                            "@value": "string()",
                        },
                        "?share_title3": "div/header/h1/text()",
                        "?share_title5": "div/div/div/header/h1/text()",
                        "?share_from": "div/div/text()|div/div/div/text()|div/div/div/div/text()",
                        "?share_content_href": "a/@href",
                        "?share_content": "/div/div//p/text()",
                        "?share_image": "div/div[@class='_5s61 _4ogd _5yki _4prr']//i/@style",
                        "?share_image1": "div[@class='_5s61 _4ogd _5yki _4prr _4o5i']//i/@style|div/i/@style",
                        "?share_image_play": "div/div[@class='_5s61 _4ogd _5yki _4prr']//i[2]/@style",
                        "?share_button": "div/div/div/a/button/span/text()",
                        "?share_person": {
                            "@base": "div",
                            "?header_img": "div/i/@style",
                            "?header_name": "div/header/h3/text()",
                            "?info": "div/span",
                            "?friend_store": "div/div/div/div/a/@data-store",
                            "?friend_href": "div/div/div/div/a/@href",
                        }
                    },

                    "?video_card": {
                        "@base": "div/div/div/div|div/div/div/div/div",
                        "?data_store": "div/@data-store",
                        "?src": "video/@src",
                        "?image": "div/i/@style",
                        "?width": "video/@width",
                        "?height": "video/@height",
                        "?focus_info": {
                            "?header": "div/div/a/div/header",
                            "?like": "div/div/a/div/text()",
                        },
                        "?button": "div/div/@data-store",
                    },
                    "?slice_card": {
                        "@base": "div/div/div/div/div",
                        "@list": {
                            "?like_this": "div/div[@class='_5qfd']",
                            "?user_header_href": "div/div/a/@href",
                            "?user_header_img": "div/div/a/i/@style",
                            "?user_name": "div/div/div/a/span",
                            "?user_name_href": "div/div/div/a/@href",
                            "?content": "div/a/div/text()",
                            "?content_img": "div/div/a/div/i/@style",
                            "?info": "div/div/div/div[@class='_5qfj']/text()",
                            "?down_img_content": "div/div/div/div/a/div/header/div/span/text()",
                            "?down_img_content2": "div/div/div/div/a/div/header/div[@class='_5qfq']/text()",
                            "?like_data_store": "div/div/div/div/@data-store",
                            "?like_info": "div/div/div/div/a/div/text()"

                        },
                    },
                    "?friend_card_list": {
                        "?header": "header/div/h3/text()",
                        "?add_friend_list": {
                            "@base": "div/div/div/div/div/div/div/div",
                            "@list": {
                                "?image": "i/@style",
                                "?name": "div/div/h3/a/text()|div/div/h1/a/text()|div/div/div/h3/a/text()|div/div/div/h1/a/text()",
                                "?href": "div/div/h3/a/@href|div/div/h1/a/@href|div/div/div/h3/a/@href|div/div/div/h1/a/@href",
                                "?tips": "div/div/div/div/div/text()",
                                "?add_friend_href": "div/div/div/div/div/a/@href |div/div/div/a/@href",
                                "?add_friend_data_store": "div/div/div/div/div/a/@data-store |div/div/div/a/@data-store",
                                "?cancel_friend": "div/div/div/div/a/@data-store|div/div/div/div/div/a/@data-store",
                                "?button_text": "div/div/a/button/span/text()|div/div/div/a/button/span/text()",
                            }
                        },
                        "?more": "//article[@data-sigil='story-div']/footer//a/@href",
                        "?morename": "//article[@data-sigil='story-div']/footer//a/text()",
                    },
                    "?footer": footer_filter,
                },
            }
        }
    }

}