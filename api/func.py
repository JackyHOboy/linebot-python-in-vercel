from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, CarouselColumn,
                            CarouselTemplate, MessageAction, URIAction, ImageCarouselColumn, ImageCarouselTemplate,
                            ImageSendMessage, FlexSendMessage)

def reservation(event):
    if event == 'reservation':
        flex_button = {
        "type":"bubble",
        "body":{
            "type":"box",
            "layout":"vertical",
            "contents":[
                {
                    "type":"text",
                    "weight":"bold",
                    "size":"xl",
                    "text":"預約課程",
                    "align":"center"
                },
                {
                    "type":"box",
                    "layout":"vertical",
                    "margin":"lg",
                    "spacing":"sm",
                    "contents":[
                    {
                        "type":"text",
                        "text":"歡迎預約課程！請選擇指定教練或不指定教練",
                        "wrap":True,
                        "offsetStart": "sm"
                    }
                    ]
                }
            ]
        },
        "footer":{
            "type":"box",
            "layout":"vertical",
            "spacing":"sm",
            "contents":[
                {
                    "type":"button",
                    "height":"sm",
                    "action":{
                    "type":"message",
                    "label":"多頁",
                    "text":"多頁"
                    }
                },
                {
                    "type":"button",
                    "style":"link",
                    "height":"sm",
                    "action":{
                    "type":"message",
                    "label":"不指定教練",
                    "text":"不指定教練"
                    }
                },
                {
                    "type":"box",
                    "layout":"vertical",
                    "contents":[
                    
                    ],
                    "margin":"sm"
                }
            ],
            "flex":0
        }
        }
        
        flex_message = FlexSendMessage(alt_text='課程預約', contents=flex_button)
        return flex_message
    elif event == 'specify':
        flex_specify = {
        "type":"bubble",
        "body":{
            "type":"box",
            "layout":"vertical",
            "contents":[
                {
                    "type":"text",
                    "weight":"bold",
                    "size":"xl",
                    "text":"指定教練",
                    "align":"center"
                },
                {
                    "type":"box",
                    "layout":"vertical",
                    "margin":"lg",
                    "spacing":"sm",
                    "contents":[
                    {
                        "type":"text",
                        "text":"請留下指定的教練與您的電話和方便預約的時間，小編會盡速為您安排！",
                        "wrap":True,
                        "offsetStart":"xs"
                    },
                    {
                        "type":"text",
                        "text":"none",
                        "color":"#FFFFFF"
                    },
                    {
                        "type":"text",
                        "text":"教練："
                    },
                    {
                        "type":"text",
                        "text":"手機："
                    },
                    {
                        "type":"text",
                        "text":"預約日期與時段："
                    }
                    ]
                }
            ]
        }
        }
        flex_message = FlexSendMessage(alt_text='指定教練', contents=flex_specify)
        return flex_message
    elif event == 'not specify':
        flex_notspecify = {
        "type":"bubble",
        "body":{
            "type":"box",
            "layout":"vertical",
            "contents":[
                {
                    "type":"text",
                    "weight":"bold",
                    "size":"xl",
                    "text":"不指定教練",
                    "align":"center"
                },
                {
                    "type":"box",
                    "layout":"vertical",
                    "margin":"lg",
                    "spacing":"sm",
                    "contents":[
                    {
                        "type":"text",
                        "text":"請留下您的電話和方便預約的時間，小編會盡速為您安排！",
                        "wrap":True,
                        "offsetStart":"xs"
                    },
                    {
                        "type":"text",
                        "text":"none",
                        "color":"#FFFFFF"
                    },
                    {
                        "type":"text",
                        "text":"手機："
                    },
                    {
                        "type":"text",
                        "text":"預約日期與時段："
                    }
                    ]
                }
            ]
        }
        }
        flex_message = FlexSendMessage(alt_text='不指定教練', contents=flex_notspecify)
        return flex_message
    
def coach_info():
    image_carousel_columns = [
        ImageCarouselColumn(
            image_url='https://i.imgur.com/DrFIHA1.jpeg',
            action=URIAction(uri='https://i.imgur.com/DrFIHA1.jpeg')
        ),
        ImageCarouselColumn(
            image_url='https://i.imgur.com/jHR50KF.jpeg',
            action=URIAction(uri='https://i.imgur.com/jHR50KF.jpeg')
        ),
        ImageCarouselColumn(
            image_url='https://i.imgur.com/uqLFtAR.jpeg',
            action=URIAction(uri='https://i.imgur.com/uqLFtAR.jpeg')
        ),
        ImageCarouselColumn(
            image_url='https://i.imgur.com/Sy2MTkQ.jpeg',
            action=URIAction(uri='https://i.imgur.com/Sy2MTkQ.jpeg')
        ),
        ImageCarouselColumn(
            image_url='https://i.imgur.com/doKPQdf.jpeg',
            action=URIAction(uri='https://i.imgur.com/doKPQdf.jpeg')
        ),
        ImageCarouselColumn(
            image_url='https://i.imgur.com/rvz8BId.jpeg',
            action=URIAction(uri='https://i.imgur.com/rvz8BId.jpeg')
        ),
        ImageCarouselColumn(
            image_url='https://i.imgur.com/W2n8LN5.jpeg',
            action=URIAction(uri='https://i.imgur.com/W2n8LN5.jpeg')
        ),
        ImageCarouselColumn(
            image_url='https://i.imgur.com/t2svPXe.jpeg',
            action=URIAction(uri='https://i.imgur.com/t2svPXe.jpeg')
        ),
        ImageCarouselColumn(
            image_url='https://i.imgur.com/CHTkxjH.jpeg',
            action=URIAction(uri='https://i.imgur.com/CHTkxjH.jpeg')
        )
    ]

    image_carousel_template = ImageCarouselTemplate(columns=image_carousel_columns)
    template_message = TemplateSendMessage(
        alt_text='教練介紹',
        template=image_carousel_template
        )
    return template_message

def store_info():
    flex_storeInfo = {
    "type":"carousel",
    "contents":[
        {
            "type":"bubble",
            "hero":{
                "type":"image",
                "url":"https://i.imgur.com/WJRfiH5.jpeg",
                "size":"full",
                "aspectRatio":"20:13",
                "aspectMode":"cover"
            },
            "body":{
                "type":"box",
                "layout":"vertical",
                "contents":[
                {
                    "type":"text",
                    "text":"石牌門市",
                    "weight":"bold",
                    "size":"xl"
                },
                {
                    "type":"box",
                    "layout":"vertical",
                    "margin":"md",
                    "spacing":"sm",
                    "contents":[
                        {
                            "type":"box",
                            "layout":"baseline",
                            "spacing":"sm",
                            "contents":[
                            {
                                "type":"text",
                                "text":"電話",
                                "color":"#aaaaaa",
                                "size":"sm",
                                "flex":1
                            },
                            {
                                "type":"text",
                                "text":"2828-7313",
                                "color":"#666666",
                                "size":"sm",
                                "flex":5
                            }
                            ]
                        },
                        {
                            "type":"box",
                            "layout":"baseline",
                            "spacing":"sm",
                            "contents":[
                            {
                                "type":"text",
                                "text":"地址",
                                "color":"#aaaaaa",
                                "size":"sm",
                                "flex":1
                            },
                            {
                                "type":"text",
                                "text":"台北市北投區承德路七段223之2號",
                                "color":"#666666",
                                "size":"sm",
                                "flex":5,
                                "adjustMode":"shrink-to-fit",
                                "wrap":True
                            }
                            ]
                        },
                        {
                            "type":"box",
                            "layout":"baseline",
                            "contents":[
                            {
                                "type":"text",
                                "text":"ID",
                                "flex":1,
                                "color":"#aaaaaa",
                                "size":"sm"
                            },
                            {
                                "type":"text",
                                "text":"@278cpcwm",
                                "flex":5,
                                "color":"#666666",
                                "size":"sm"
                            }
                            ]
                        },
                        {
                            "type":"box",
                            "layout":"vertical",
                            "contents":[
                            {
                                "type":"text",
                                "text":"營業時間",
                                "size":"sm",
                                "color":"#aaaaaa",
                                "flex":1
                            },
                            {
                                "type":"text",
                                "text":"週一至週五 08:00-22:00",
                                "size":"sm",
                                "flex":5,
                                "color":"#666666",
                                "offsetStart":"14px"
                            },
                            {
                                "type":"text",
                                "text":"週六、週日 08:00-19:00",
                                "size":"sm",
                                "flex":5,
                                "color":"#666666",
                                "offsetStart":"14px"
                            }
                            ],
                            "spacing":"sm"
                        }
                    ],
                    "paddingEnd":"none"
                }
                ]
            },
            "footer":{
                "type":"box",
                "layout":"vertical",
                "spacing":"sm",
                "contents":[
                {
                    "type":"button",
                    "style":"primary",
                    "height":"sm",
                    "action":{
                        "type":"uri",
                        "label":"電話",
                        "uri":"tel:02-28287313"
                    }
                },
                {
                    "type":"button",
                    "style":"secondary",
                    "height":"sm",
                    "action":{
                        "type":"uri",
                        "label":"官方網站",
                        "uri":"https://jimmy2130.github.io/WestGolf/index.html",
                        "altUri":{
                            "desktop":"https://jimmy2130.github.io/WestGolf/index.html"
                        }
                    }
                }
                ],
                "flex":0
            }
        },
        {
            "type":"bubble",
            "hero":{
                "type":"image",
                "url":"https://i.imgur.com/BGvR9mb.jpeg",
                "size":"full",
                "aspectRatio":"20:13",
                "aspectMode":"cover"
            },
            "body":{
                "type":"box",
                "layout":"vertical",
                "contents":[
                {
                    "type":"text",
                    "text":"碧潭門市",
                    "weight":"bold",
                    "size":"xl"
                },
                {
                    "type":"box",
                    "layout":"vertical",
                    "margin":"md",
                    "spacing":"sm",
                    "contents":[
                        {
                            "type":"box",
                            "layout":"baseline",
                            "spacing":"sm",
                            "contents":[
                            {
                                "type":"text",
                                "text":"電話",
                                "color":"#aaaaaa",
                                "size":"sm",
                                "flex":1
                            },
                            {
                                "type":"text",
                                "text":"2212-6041",
                                "color":"#666666",
                                "size":"sm",
                                "flex":5
                            }
                            ]
                        },
                        {
                            "type":"box",
                            "layout":"baseline",
                            "spacing":"sm",
                            "contents":[
                            {
                                "type":"text",
                                "text":"地址",
                                "color":"#aaaaaa",
                                "size":"sm",
                                "flex":1
                            },
                            {
                                "type":"text",
                                "text":"新北市新店區溪洲路121號",
                                "color":"#666666",
                                "size":"sm",
                                "flex":5,
                                "adjustMode":"shrink-to-fit",
                                "wrap":True
                            }
                            ]
                        },
                        {
                            "type":"box",
                            "layout":"baseline",
                            "contents":[
                            {
                                "type":"text",
                                "text":"ID",
                                "flex":1,
                                "color":"#aaaaaa",
                                "size":"sm"
                            },
                            {
                                "type":"text",
                                "text":"@298yqvcd",
                                "flex":5,
                                "color":"#666666",
                                "size":"sm"
                            }
                            ]
                        },
                        {
                            "type":"box",
                            "layout":"baseline",
                            "contents":[
                            {
                                "type":"text",
                                "text":" ",
                                "flex":1,
                                "size":"sm"
                            }
                            ]
                        },
                        {
                            "type":"box",
                            "layout":"vertical",
                            "contents":[
                            {
                                "type":"text",
                                "text":"營業時間",
                                "size":"sm",
                                "color":"#aaaaaa",
                                "flex":1
                            },
                            {
                                "type":"text",
                                "text":"週一至週五 09:30-22:00",
                                "size":"sm",
                                "flex":5,
                                "color":"#666666",
                                "offsetStart":"14px"
                            },
                            {
                                "type":"text",
                                "text":"週六、週日 08:00-19:00",
                                "size":"sm",
                                "flex":5,
                                "color":"#666666",
                                "offsetStart":"14px"
                            }
                            ],
                            "spacing":"sm"
                        }                    
                    ],
                    "paddingEnd":"none"
                }
                ]
            },
            "footer":{
                "type":"box",
                "layout":"vertical",
                "spacing":"sm",
                "contents":[
                {
                    "type":"button",
                    "style":"primary",
                    "height":"sm",
                    "action":{
                        "type":"uri",
                        "label":"電話",
                        "uri":"tel:02-22126041"
                    }
                },
                {
                    "type":"button",
                    "style":"secondary",
                    "height":"sm",
                    "action":{
                        "type":"uri",
                        "label":"官方網站",
                        "uri":"https://jimmy2130.github.io/WestGolf/index.html",
                        "altUri":{
                            "desktop":"https://jimmy2130.github.io/WestGolf/index.html"
                        }
                    }
                }
                ],
                "flex":0
            }
        }
    ]
    }

    flex_message = FlexSendMessage(alt_text='門市資訊', contents=flex_storeInfo)
    return flex_message