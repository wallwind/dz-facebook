
index_feedback_filter = {
    "?org_title": "//title/text()",
    "title": "//span[@class='w-nav-title']/text()",
    "desc": "//div[@class='w-report-description']/text()",
    "btn_text": "//a[@data-stat-action='submit']/text()",
    "placeholder": "//div[@class='w-report-detail']/textarea/@placeholder"
}


detail_feedback_filter = {
    "?org_title": "//title/text()",
    "title": "//span[@class='w-nav-title']/text()",
    "report_title": "//div[@class='w-report-title']/text()",
    "btn_text": "//a[@data-stat-action='submit']/text()",
    "placeholder": "//div[@class='w-report-detail']/textarea/@placeholder",
    "sections": {
        "@base": "//ul/li[@class='w-report-reason']",
        "@list": {
            "text": "label/text()",
            "value": "label/input/@data-value"
        }
    }
}

