updates = [
    {
        "update_id": 366965026,
        "message": {
            "message_id": 6,
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "chat": {
                "id": 766453001,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "type": "private",
            },
            "date": 1789224767,
            "text": "/start",
        },
    },
    {
        "update_id": 366965025,
        "message": {
            "message_id": 5,
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "chat": {
                "id": 766453001,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "type": "private",
            },
            "date": 1789224767,
            "text": "Test message",
        },
    },
    {
        "update_id": 366965241,
        "message": {
            "message_id": 324,
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "chat": {
                "id": 766453001,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "type": "private",
            },
            "date": 1791381687,
            "text": "Старт",
        },
    },
    {
        "update_id": 366965242,
        "callback_query": {
            "id": "3291890575729639609",
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "message": {
                "message_id": 326,
                "from": {
                    "id": 8669703310,
                    "is_bot": True,
                    "first_name": "Гончаренко Д.І. бот",
                    "username": "hdi_lesson_bot",
                },
                "chat": {
                    "id": 766453001,
                    "first_name": "Дмитро",
                    "last_name": "Гончаренко",
                    "type": "private",
                },
                "date": 1791381687,
                "text": "Будь ласка, оберіть Вашу піцу.",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {"text": "Маргарита", "callback_data": "margherita"},
                            {"text": "Пеппероні", "callback_data": "pepperoni"},
                        ],
                        [
                            {"text": "Чотири сира", "callback_data": "four_cheeses"},
                            {"text": "Гавайська", "callback_data": "hawaiian"},
                        ],
                        [
                            {"text": "Куриця барбекю", "callback_data": "bbq_chicken"},
                            {"text": "М'ясна", "callback_data": "all_meet"},
                        ],
                        [{"text": "Вегетаріанська", "callback_data": "vegetarian"}],
                    ]
                },
            },
            "chat_instance": "-6286455501612302882",
            "data": "four_cheeses",
        },
    },
    {
        "update_id": 366965243,
        "callback_query": {
            "id": "3291890575029957069",
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "message": {
                "message_id": 327,
                "from": {
                    "id": 8669703310,
                    "is_bot": True,
                    "first_name": "Гончаренко Д.І. бот",
                    "username": "hdi_lesson_bot",
                },
                "chat": {
                    "id": 766453001,
                    "first_name": "Дмитро",
                    "last_name": "Гончаренко",
                    "type": "private",
                },
                "date": 1791381690,
                "text": "Будь ласка, оберіть розмір піци.",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {
                                "text": "Маленька (25 см.)",
                                "callback_data": "size_small",
                            },
                            {
                                "text": "Середня (30 см.)",
                                "callback_data": "size_medium",
                            },
                        ],
                        [
                            {"text": "Велика (35 см.)", "callback_data": "size_large"},
                            {
                                "text": "Дуже велика (40 см.)",
                                "callback_data": "size_super",
                            },
                        ],
                    ]
                },
            },
            "chat_instance": "-6286455501612302882",
            "data": "size_medium",
        },
    },
    {
        "update_id": 366965244,
        "callback_query": {
            "id": "3291890573228239496",
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "message": {
                "message_id": 328,
                "from": {
                    "id": 8669703310,
                    "is_bot": True,
                    "first_name": "Гончаренко Д.І. бот",
                    "username": "hdi_lesson_bot",
                },
                "chat": {
                    "id": 766453001,
                    "first_name": "Дмитро",
                    "last_name": "Гончаренко",
                    "type": "private",
                },
                "date": 1791381693,
                "text": "Будь ласка, оберіть напій.",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {"text": "Кока-кола", "callback_data": "coca_cola"},
                            {"text": "Пепсі", "callback_data": "pepsi"},
                        ],
                        [
                            {"text": "Апельсиновий сік", "callback_data": "orange_jus"},
                            {"text": "Яблучний сік", "callback_data": "apple_jus"},
                        ],
                        [{"text": "Без напою", "callback_data": "no_drinks"}],
                    ]
                },
            },
            "chat_instance": "-6286455501612302882",
            "data": "no_drinks",
        },
    },
    {
        "update_id": 366965245,
        "callback_query": {
            "id": "3291890577428697347",
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "message": {
                "message_id": 329,
                "from": {
                    "id": 8669703310,
                    "is_bot": True,
                    "first_name": "Гончаренко Д.І. бот",
                    "username": "hdi_lesson_bot",
                },
                "chat": {
                    "id": 766453001,
                    "first_name": "Дмитро",
                    "last_name": "Гончаренко",
                    "type": "private",
                },
                "date": 1791381696,
                "text": "Ви обрали:\n                піцу - Чотири сира,\n                розмір - Середня (30 см.),\n                напій - Без напою",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {"text": "Підтвердити", "callback_data": "approval"},
                            {"text": "Відмова", "callback_data": "cancel"},
                        ]
                    ]
                },
            },
            "chat_instance": "-6286455501612302882",
            "data": "cancel",
        },
    },
    {
        "update_id": 366965246,
        "message": {
            "message_id": 331,
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "chat": {
                "id": 766453001,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "type": "private",
            },
            "date": 1791381938,
            "text": "Старт",
        },
    },
    {
        "update_id": 366965247,
        "callback_query": {
            "id": "3291890574115718310",
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "message": {
                "message_id": 333,
                "from": {
                    "id": 8669703310,
                    "is_bot": True,
                    "first_name": "Гончаренко Д.І. бот",
                    "username": "hdi_lesson_bot",
                },
                "chat": {
                    "id": 766453001,
                    "first_name": "Дмитро",
                    "last_name": "Гончаренко",
                    "type": "private",
                },
                "date": 1791381939,
                "text": "Будь ласка, оберіть Вашу піцу.",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {"text": "Маргарита", "callback_data": "margherita"},
                            {"text": "Пеппероні", "callback_data": "pepperoni"},
                        ],
                        [
                            {"text": "Чотири сира", "callback_data": "four_cheeses"},
                            {"text": "Гавайська", "callback_data": "hawaiian"},
                        ],
                        [
                            {"text": "Куриця барбекю", "callback_data": "bbq_chicken"},
                            {"text": "М'ясна", "callback_data": "all_meet"},
                        ],
                        [{"text": "Вегетаріанська", "callback_data": "vegetarian"}],
                    ]
                },
            },
            "chat_instance": "-6286455501612302882",
            "data": "four_cheeses",
        },
    },
    {
        "update_id": 366965248,
        "callback_query": {
            "id": "3291890574876534470",
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "message": {
                "message_id": 334,
                "from": {
                    "id": 8669703310,
                    "is_bot": True,
                    "first_name": "Гончаренко Д.І. бот",
                    "username": "hdi_lesson_bot",
                },
                "chat": {
                    "id": 766453001,
                    "first_name": "Дмитро",
                    "last_name": "Гончаренко",
                    "type": "private",
                },
                "date": 1791381941,
                "text": "Будь ласка, оберіть розмір піци.",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {
                                "text": "Маленька (25 см.)",
                                "callback_data": "size_small",
                            },
                            {
                                "text": "Середня (30 см.)",
                                "callback_data": "size_medium",
                            },
                        ],
                        [
                            {"text": "Велика (35 см.)", "callback_data": "size_large"},
                            {
                                "text": "Дуже велика (40 см.)",
                                "callback_data": "size_super",
                            },
                        ],
                    ]
                },
            },
            "chat_instance": "-6286455501612302882",
            "data": "size_large",
        },
    },
    {
        "update_id": 366965249,
        "callback_query": {
            "id": "3291890574795588469",
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "message": {
                "message_id": 335,
                "from": {
                    "id": 8669703310,
                    "is_bot": True,
                    "first_name": "Гончаренко Д.І. бот",
                    "username": "hdi_lesson_bot",
                },
                "chat": {
                    "id": 766453001,
                    "first_name": "Дмитро",
                    "last_name": "Гончаренко",
                    "type": "private",
                },
                "date": 1791381943,
                "text": "Будь ласка, оберіть напій.",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {"text": "Кока-кола", "callback_data": "coca_cola"},
                            {"text": "Пепсі", "callback_data": "pepsi"},
                        ],
                        [
                            {"text": "Апельсиновий сік", "callback_data": "orange_jus"},
                            {"text": "Яблучний сік", "callback_data": "apple_jus"},
                        ],
                        [{"text": "Без напою", "callback_data": "no_drinks"}],
                    ]
                },
            },
            "chat_instance": "-6286455501612302882",
            "data": "no_drinks",
        },
    },
    {
        "update_id": 366965250,
        "callback_query": {
            "id": "3291890574750010318",
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "message": {
                "message_id": 336,
                "from": {
                    "id": 8669703310,
                    "is_bot": True,
                    "first_name": "Гончаренко Д.І. бот",
                    "username": "hdi_lesson_bot",
                },
                "chat": {
                    "id": 766453001,
                    "first_name": "Дмитро",
                    "last_name": "Гончаренко",
                    "type": "private",
                },
                "date": 1791381945,
                "text": "Ви обрали:\n                піцу - Чотири сира,\n                розмір - Велика (35 см.),\n                напій - Без напою",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {"text": "Підтвердити", "callback_data": "approval"},
                            {"text": "Відмова", "callback_data": "cancel"},
                        ]
                    ]
                },
            },
            "chat_instance": "-6286455501612302882",
            "data": "cancel",
        },
    },
    {
        "update_id": 366965251,
        "message": {
            "message_id": 338,
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "chat": {
                "id": 766453001,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "type": "private",
            },
            "date": 1791383344,
            "text": "Старт",
        },
    },
    {
        "update_id": 366965252,
        "callback_query": {
            "id": "3291890577305615337",
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "message": {
                "message_id": 340,
                "from": {
                    "id": 8669703310,
                    "is_bot": True,
                    "first_name": "Гончаренко Д.І. бот",
                    "username": "hdi_lesson_bot",
                },
                "chat": {
                    "id": 766453001,
                    "first_name": "Дмитро",
                    "last_name": "Гончаренко",
                    "type": "private",
                },
                "date": 1791383345,
                "text": "Будь ласка, оберіть Вашу піцу.",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {"text": "Маргарита", "callback_data": "margherita"},
                            {"text": "Пеппероні", "callback_data": "pepperoni"},
                        ],
                        [
                            {"text": "Чотири сира", "callback_data": "four_cheeses"},
                            {"text": "Гавайська", "callback_data": "hawaiian"},
                        ],
                        [
                            {"text": "Куриця барбекю", "callback_data": "bbq_chicken"},
                            {"text": "М'ясна", "callback_data": "all_meet"},
                        ],
                        [{"text": "Вегетаріанська", "callback_data": "vegetarian"}],
                    ]
                },
            },
            "chat_instance": "-6286455501612302882",
            "data": "four_cheeses",
        },
    },
    {
        "update_id": 366965253,
        "callback_query": {
            "id": "3291890576521026136",
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "message": {
                "message_id": 341,
                "from": {
                    "id": 8669703310,
                    "is_bot": True,
                    "first_name": "Гончаренко Д.І. бот",
                    "username": "hdi_lesson_bot",
                },
                "chat": {
                    "id": 766453001,
                    "first_name": "Дмитро",
                    "last_name": "Гончаренко",
                    "type": "private",
                },
                "date": 1791383349,
                "text": "Будь ласка, оберіть розмір піци.",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {
                                "text": "Маленька (25 см.)",
                                "callback_data": "size_small",
                            },
                            {
                                "text": "Середня (30 см.)",
                                "callback_data": "size_medium",
                            },
                        ],
                        [
                            {"text": "Велика (35 см.)", "callback_data": "size_large"},
                            {
                                "text": "Дуже велика (40 см.)",
                                "callback_data": "size_super",
                            },
                        ],
                    ]
                },
            },
            "chat_instance": "-6286455501612302882",
            "data": "size_super",
        },
    },
    {
        "update_id": 366965254,
        "callback_query": {
            "id": "3291890575412451871",
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "message": {
                "message_id": 342,
                "from": {
                    "id": 8669703310,
                    "is_bot": True,
                    "first_name": "Гончаренко Д.І. бот",
                    "username": "hdi_lesson_bot",
                },
                "chat": {
                    "id": 766453001,
                    "first_name": "Дмитро",
                    "last_name": "Гончаренко",
                    "type": "private",
                },
                "date": 1791383351,
                "text": "Будь ласка, оберіть напій.",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {"text": "Кока-кола", "callback_data": "coca_cola"},
                            {"text": "Пепсі", "callback_data": "pepsi"},
                        ],
                        [
                            {"text": "Апельсиновий сік", "callback_data": "orange_jus"},
                            {"text": "Яблучний сік", "callback_data": "apple_jus"},
                        ],
                        [{"text": "Без напою", "callback_data": "no_drinks"}],
                    ]
                },
            },
            "chat_instance": "-6286455501612302882",
            "data": "orange_jus",
        },
    },
    {
        "update_id": 366965255,
        "callback_query": {
            "id": "3291890574537561746",
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "message": {
                "message_id": 343,
                "from": {
                    "id": 8669703310,
                    "is_bot": True,
                    "first_name": "Гончаренко Д.І. бот",
                    "username": "hdi_lesson_bot",
                },
                "chat": {
                    "id": 766453001,
                    "first_name": "Дмитро",
                    "last_name": "Гончаренко",
                    "type": "private",
                },
                "date": 1791383353,
                "text": "Ви обрали:\n                піцу - Чотири сира,\n                розмір - Дуже велика (40 см.),\n                напій - Апельсиновий сік",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {"text": "Підтвердити", "callback_data": "approval"},
                            {"text": "Відмова", "callback_data": "cancel"},
                        ]
                    ]
                },
            },
            "chat_instance": "-6286455501612302882",
            "data": "approval",
        },
    },
    {
        "update_id": 366965256,
        "message": {
            "message_id": 345,
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "chat": {
                "id": 766453001,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "type": "private",
            },
            "date": 1791623954,
            "text": "Старт",
        },
    },
    {
        "update_id": 366965257,
        "callback_query": {
            "id": "3291890577112945562",
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "message": {
                "message_id": 347,
                "from": {
                    "id": 8669703310,
                    "is_bot": True,
                    "first_name": "Гончаренко Д.І. бот",
                    "username": "hdi_lesson_bot",
                },
                "chat": {
                    "id": 766453001,
                    "first_name": "Дмитро",
                    "last_name": "Гончаренко",
                    "type": "private",
                },
                "date": 1791623955,
                "text": "Будь ласка, оберіть Вашу піцу.",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {"text": "Маргарита", "callback_data": "margherita"},
                            {"text": "Пеппероні", "callback_data": "pepperoni"},
                        ],
                        [
                            {"text": "Чотири сира", "callback_data": "four_cheeses"},
                            {"text": "Гавайська", "callback_data": "hawaiian"},
                        ],
                        [
                            {"text": "Куриця барбекю", "callback_data": "bbq_chicken"},
                            {"text": "М'ясна", "callback_data": "all_meet"},
                        ],
                        [{"text": "Вегетаріанська", "callback_data": "vegetarian"}],
                    ]
                },
            },
            "chat_instance": "-6286455501612302882",
            "data": "margherita",
        },
    },
    {
        "update_id": 366965258,
        "callback_query": {
            "id": "3291890574522018690",
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "message": {
                "message_id": 348,
                "from": {
                    "id": 8669703310,
                    "is_bot": True,
                    "first_name": "Гончаренко Д.І. бот",
                    "username": "hdi_lesson_bot",
                },
                "chat": {
                    "id": 766453001,
                    "first_name": "Дмитро",
                    "last_name": "Гончаренко",
                    "type": "private",
                },
                "date": 1791624130,
                "text": "Будь ласка, оберіть розмір піци.",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {
                                "text": "Маленька (25 см.)",
                                "callback_data": "size_small",
                            },
                            {
                                "text": "Середня (30 см.)",
                                "callback_data": "size_medium",
                            },
                        ],
                        [
                            {"text": "Велика (35 см.)", "callback_data": "size_large"},
                            {
                                "text": "Дуже велика (40 см.)",
                                "callback_data": "size_super",
                            },
                        ],
                    ]
                },
            },
            "chat_instance": "-6286455501612302882",
            "data": "size_small",
        },
    },
    {
        "update_id": 366965259,
        "callback_query": {
            "id": "3291890576422690968",
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "message": {
                "message_id": 349,
                "from": {
                    "id": 8669703310,
                    "is_bot": True,
                    "first_name": "Гончаренко Д.І. бот",
                    "username": "hdi_lesson_bot",
                },
                "chat": {
                    "id": 766453001,
                    "first_name": "Дмитро",
                    "last_name": "Гончаренко",
                    "type": "private",
                },
                "date": 1791624132,
                "text": "Будь ласка, оберіть напій.",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {"text": "Кока-кола", "callback_data": "coca_cola"},
                            {"text": "Пепсі", "callback_data": "pepsi"},
                        ],
                        [
                            {"text": "Апельсиновий сік", "callback_data": "orange_jus"},
                            {"text": "Яблучний сік", "callback_data": "apple_jus"},
                        ],
                        [{"text": "Без напою", "callback_data": "no_drinks"}],
                    ]
                },
            },
            "chat_instance": "-6286455501612302882",
            "data": "no_drinks",
        },
    },
    {
        "update_id": 366965260,
        "callback_query": {
            "id": "3291890576858941556",
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "message": {
                "message_id": 350,
                "from": {
                    "id": 8669703310,
                    "is_bot": True,
                    "first_name": "Гончаренко Д.І. бот",
                    "username": "hdi_lesson_bot",
                },
                "chat": {
                    "id": 766453001,
                    "first_name": "Дмитро",
                    "last_name": "Гончаренко",
                    "type": "private",
                },
                "date": 1791624134,
                "text": "Ви обрали:\n                піцу - Маргарита,\n                розмір - Маленька (25 см.),\n                напій - Без напою",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {"text": "Підтвердити", "callback_data": "approval"},
                            {"text": "Відмова", "callback_data": "cancel"},
                        ]
                    ]
                },
            },
            "chat_instance": "-6286455501612302882",
            "data": "approval",
        },
    },
    {
        "update_id": 366965261,
        "message": {
            "message_id": 352,
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "chat": {
                "id": 766453001,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "type": "private",
            },
            "date": 1791697389,
            "text": "Старт",
        },
    },
    {
        "update_id": 366965262,
        "callback_query": {
            "id": "3291890577350230035",
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "message": {
                "message_id": 354,
                "from": {
                    "id": 8669703310,
                    "is_bot": True,
                    "first_name": "Гончаренко Д.І. бот",
                    "username": "hdi_lesson_bot",
                },
                "chat": {
                    "id": 766453001,
                    "first_name": "Дмитро",
                    "last_name": "Гончаренко",
                    "type": "private",
                },
                "date": 1791705634,
                "text": "Будь ласка, оберіть Вашу піцу.",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {"text": "Маргарита", "callback_data": "margherita"},
                            {"text": "Пеппероні", "callback_data": "pepperoni"},
                        ],
                        [
                            {"text": "Чотири сира", "callback_data": "four_cheeses"},
                            {"text": "Гавайська", "callback_data": "hawaiian"},
                        ],
                        [
                            {"text": "Куриця барбекю", "callback_data": "bbq_chicken"},
                            {"text": "М'ясна", "callback_data": "all_meet"},
                        ],
                        [{"text": "Вегетаріанська", "callback_data": "vegetarian"}],
                    ]
                },
            },
            "chat_instance": "-6286455501612302882",
            "data": "vegetarian",
        },
    },
    {
        "update_id": 366965263,
        "callback_query": {
            "id": "3291890574617155303",
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "message": {
                "message_id": 355,
                "from": {
                    "id": 8669703310,
                    "is_bot": True,
                    "first_name": "Гончаренко Д.І. бот",
                    "username": "hdi_lesson_bot",
                },
                "chat": {
                    "id": 766453001,
                    "first_name": "Дмитро",
                    "last_name": "Гончаренко",
                    "type": "private",
                },
                "date": 1791705653,
                "text": "Будь ласка, оберіть розмір піци.",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {
                                "text": "Маленька (25 см.)",
                                "callback_data": "size_small",
                            },
                            {
                                "text": "Середня (30 см.)",
                                "callback_data": "size_medium",
                            },
                        ],
                        [
                            {"text": "Велика (35 см.)", "callback_data": "size_large"},
                            {
                                "text": "Дуже велика (40 см.)",
                                "callback_data": "size_super",
                            },
                        ],
                    ]
                },
            },
            "chat_instance": "-6286455501612302882",
            "data": "size_large",
        },
    },
    {
        "update_id": 366965264,
        "callback_query": {
            "id": "3291890575494223803",
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "message": {
                "message_id": 356,
                "from": {
                    "id": 8669703310,
                    "is_bot": True,
                    "first_name": "Гончаренко Д.І. бот",
                    "username": "hdi_lesson_bot",
                },
                "chat": {
                    "id": 766453001,
                    "first_name": "Дмитро",
                    "last_name": "Гончаренко",
                    "type": "private",
                },
                "date": 1791705656,
                "text": "Будь ласка, оберіть напій.",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {"text": "Кока-кола", "callback_data": "coca_cola"},
                            {"text": "Пепсі", "callback_data": "pepsi"},
                        ],
                        [
                            {"text": "Апельсиновий сік", "callback_data": "orange_jus"},
                            {"text": "Яблучний сік", "callback_data": "apple_jus"},
                        ],
                        [{"text": "Без напою", "callback_data": "no_drinks"}],
                    ]
                },
            },
            "chat_instance": "-6286455501612302882",
            "data": "no_drinks",
        },
    },
    {
        "update_id": 366965265,
        "callback_query": {
            "id": "3291890573446508298",
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "message": {
                "message_id": 357,
                "from": {
                    "id": 8669703310,
                    "is_bot": True,
                    "first_name": "Гончаренко Д.І. бот",
                    "username": "hdi_lesson_bot",
                },
                "chat": {
                    "id": 766453001,
                    "first_name": "Дмитро",
                    "last_name": "Гончаренко",
                    "type": "private",
                },
                "date": 1791705658,
                "text": "Ви обрали:\n                піцу - Вегетаріанська,\n                розмір - Велика (35 см.),\n                напій - Без напою",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {"text": "Підтвердити", "callback_data": "approval"},
                            {"text": "Відмова", "callback_data": "cancel"},
                        ]
                    ]
                },
            },
            "chat_instance": "-6286455501612302882",
            "data": "cancel",
        },
    },
    {
        "update_id": 366965266,
        "message": {
            "message_id": 359,
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "chat": {
                "id": 766453001,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "type": "private",
            },
            "date": 1791727226,
            "text": "Старт",
        },
    },
    {
        "update_id": 366965267,
        "callback_query": {
            "id": "3291890576803278787",
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "message": {
                "message_id": 361,
                "from": {
                    "id": 8669703310,
                    "is_bot": True,
                    "first_name": "Гончаренко Д.І. бот",
                    "username": "hdi_lesson_bot",
                },
                "chat": {
                    "id": 766453001,
                    "first_name": "Дмитро",
                    "last_name": "Гончаренко",
                    "type": "private",
                },
                "date": 1791727227,
                "text": "Будь ласка, оберіть Вашу піцу.",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {"text": "Маргарита", "callback_data": "margherita"},
                            {"text": "Пеппероні", "callback_data": "pepperoni"},
                        ],
                        [
                            {"text": "Чотири сира", "callback_data": "four_cheeses"},
                            {"text": "Гавайська", "callback_data": "hawaiian"},
                        ],
                        [
                            {"text": "Куриця барбекю", "callback_data": "bbq_chicken"},
                            {"text": "М'ясна", "callback_data": "all_meet"},
                        ],
                        [{"text": "Вегетаріанська", "callback_data": "vegetarian"}],
                    ]
                },
            },
            "chat_instance": "-6286455501612302882",
            "data": "vegetarian",
        },
    },
    {
        "update_id": 366965268,
        "callback_query": {
            "id": "3291890574429862493",
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "message": {
                "message_id": 362,
                "from": {
                    "id": 8669703310,
                    "is_bot": True,
                    "first_name": "Гончаренко Д.І. бот",
                    "username": "hdi_lesson_bot",
                },
                "chat": {
                    "id": 766453001,
                    "first_name": "Дмитро",
                    "last_name": "Гончаренко",
                    "type": "private",
                },
                "date": 1791727229,
                "text": "Будь ласка, оберіть розмір піци.",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {
                                "text": "Маленька (25 см.)",
                                "callback_data": "size_small",
                            },
                            {
                                "text": "Середня (30 см.)",
                                "callback_data": "size_medium",
                            },
                        ],
                        [
                            {"text": "Велика (35 см.)", "callback_data": "size_large"},
                            {
                                "text": "Дуже велика (40 см.)",
                                "callback_data": "size_super",
                            },
                        ],
                    ]
                },
            },
            "chat_instance": "-6286455501612302882",
            "data": "size_large",
        },
    },
    {
        "update_id": 366965269,
        "callback_query": {
            "id": "3291890577289634538",
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "message": {
                "message_id": 363,
                "from": {
                    "id": 8669703310,
                    "is_bot": True,
                    "first_name": "Гончаренко Д.І. бот",
                    "username": "hdi_lesson_bot",
                },
                "chat": {
                    "id": 766453001,
                    "first_name": "Дмитро",
                    "last_name": "Гончаренко",
                    "type": "private",
                },
                "date": 1791727231,
                "text": "Будь ласка, оберіть напій.",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {"text": "Кока-кола", "callback_data": "coca_cola"},
                            {"text": "Пепсі", "callback_data": "pepsi"},
                        ],
                        [
                            {"text": "Апельсиновий сік", "callback_data": "orange_jus"},
                            {"text": "Яблучний сік", "callback_data": "apple_jus"},
                        ],
                        [{"text": "Без напою", "callback_data": "no_drinks"}],
                    ]
                },
            },
            "chat_instance": "-6286455501612302882",
            "data": "no_drinks",
        },
    },
    {
        "update_id": 366965270,
        "callback_query": {
            "id": "3291890575953211328",
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "message": {
                "message_id": 364,
                "from": {
                    "id": 8669703310,
                    "is_bot": True,
                    "first_name": "Гончаренко Д.І. бот",
                    "username": "hdi_lesson_bot",
                },
                "chat": {
                    "id": 766453001,
                    "first_name": "Дмитро",
                    "last_name": "Гончаренко",
                    "type": "private",
                },
                "date": 1791727233,
                "text": "Ви обрали:\n                піцу - Вегетаріанська,\n                розмір - Велика (35 см.),\n                напій - Без напою",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {"text": "Підтвердити", "callback_data": "approval"},
                            {"text": "Відмова", "callback_data": "cancel"},
                        ]
                    ]
                },
            },
            "chat_instance": "-6286455501612302882",
            "data": "approval",
        },
    },
    {
        "update_id": 366965271,
        "message": {
            "message_id": 366,
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "chat": {
                "id": 766453001,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "type": "private",
            },
            "date": 1791727760,
            "text": "Старт",
        },
    },
    {
        "update_id": 366965272,
        "callback_query": {
            "id": "3291890575347925681",
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "message": {
                "message_id": 368,
                "from": {
                    "id": 8669703310,
                    "is_bot": True,
                    "first_name": "Гончаренко Д.І. бот",
                    "username": "hdi_lesson_bot",
                },
                "chat": {
                    "id": 766453001,
                    "first_name": "Дмитро",
                    "last_name": "Гончаренко",
                    "type": "private",
                },
                "date": 1791727760,
                "text": "Будь ласка, оберіть Вашу піцу.",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {"text": "Маргарита", "callback_data": "margherita"},
                            {"text": "Пеппероні", "callback_data": "pepperoni"},
                        ],
                        [
                            {"text": "Чотири сира", "callback_data": "four_cheeses"},
                            {"text": "Гавайська", "callback_data": "hawaiian"},
                        ],
                        [
                            {"text": "Куриця барбекю", "callback_data": "bbq_chicken"},
                            {"text": "М'ясна", "callback_data": "all_meet"},
                        ],
                        [{"text": "Вегетаріанська", "callback_data": "vegetarian"}],
                    ]
                },
            },
            "chat_instance": "-6286455501612302882",
            "data": "hawaiian",
        },
    },
    {
        "update_id": 366965273,
        "callback_query": {
            "id": "3291890574779849276",
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "message": {
                "message_id": 369,
                "from": {
                    "id": 8669703310,
                    "is_bot": True,
                    "first_name": "Гончаренко Д.І. бот",
                    "username": "hdi_lesson_bot",
                },
                "chat": {
                    "id": 766453001,
                    "first_name": "Дмитро",
                    "last_name": "Гончаренко",
                    "type": "private",
                },
                "date": 1791727762,
                "text": "Будь ласка, оберіть розмір піци.",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {
                                "text": "Маленька (25 см.)",
                                "callback_data": "size_small",
                            },
                            {
                                "text": "Середня (30 см.)",
                                "callback_data": "size_medium",
                            },
                        ],
                        [
                            {"text": "Велика (35 см.)", "callback_data": "size_large"},
                            {
                                "text": "Дуже велика (40 см.)",
                                "callback_data": "size_super",
                            },
                        ],
                    ]
                },
            },
            "chat_instance": "-6286455501612302882",
            "data": "size_medium",
        },
    },
    {
        "update_id": 366965274,
        "callback_query": {
            "id": "3291890574687801674",
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "message": {
                "message_id": 370,
                "from": {
                    "id": 8669703310,
                    "is_bot": True,
                    "first_name": "Гончаренко Д.І. бот",
                    "username": "hdi_lesson_bot",
                },
                "chat": {
                    "id": 766453001,
                    "first_name": "Дмитро",
                    "last_name": "Гончаренко",
                    "type": "private",
                },
                "date": 1791727766,
                "text": "Будь ласка, оберіть напій.",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {"text": "Кока-кола", "callback_data": "coca_cola"},
                            {"text": "Пепсі", "callback_data": "pepsi"},
                        ],
                        [
                            {"text": "Апельсиновий сік", "callback_data": "orange_jus"},
                            {"text": "Яблучний сік", "callback_data": "apple_jus"},
                        ],
                        [{"text": "Без напою", "callback_data": "no_drinks"}],
                    ]
                },
            },
            "chat_instance": "-6286455501612302882",
            "data": "apple_jus",
        },
    },
    {
        "update_id": 366965275,
        "callback_query": {
            "id": "3291890576540249663",
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "message": {
                "message_id": 371,
                "from": {
                    "id": 8669703310,
                    "is_bot": True,
                    "first_name": "Гончаренко Д.І. бот",
                    "username": "hdi_lesson_bot",
                },
                "chat": {
                    "id": 766453001,
                    "first_name": "Дмитро",
                    "last_name": "Гончаренко",
                    "type": "private",
                },
                "date": 1791727768,
                "text": "Ви обрали:\n                піцу - Гавайська,\n                розмір - Середня (30 см.),\n                напій - Яблучний сік",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {"text": "Підтвердити", "callback_data": "approval"},
                            {"text": "Відмова", "callback_data": "cancel"},
                        ]
                    ]
                },
            },
            "chat_instance": "-6286455501612302882",
            "data": "cancel",
        },
    },
    {
        "update_id": 366965276,
        "message": {
            "message_id": 373,
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "chat": {
                "id": 766453001,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "type": "private",
            },
            "date": 1792497326,
            "text": "Старт",
        },
    },
    {
        "update_id": 366965277,
        "callback_query": {
            "id": "3291890575020759301",
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "message": {
                "message_id": 375,
                "from": {
                    "id": 8669703310,
                    "is_bot": True,
                    "first_name": "Гончаренко Д.І. бот",
                    "username": "hdi_lesson_bot",
                },
                "chat": {
                    "id": 766453001,
                    "first_name": "Дмитро",
                    "last_name": "Гончаренко",
                    "type": "private",
                },
                "date": 1792497641,
                "text": "Будь ласка, оберіть Вашу піцу.",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {"text": "Маргарита", "callback_data": "margherita"},
                            {"text": "Пеппероні", "callback_data": "pepperoni"},
                        ],
                        [
                            {"text": "Чотири сира", "callback_data": "four_cheeses"},
                            {"text": "Гавайська", "callback_data": "hawaiian"},
                        ],
                        [
                            {"text": "Куриця барбекю", "callback_data": "bbq_chicken"},
                            {"text": "М'ясна", "callback_data": "all_meet"},
                        ],
                        [{"text": "Вегетаріанська", "callback_data": "vegetarian"}],
                    ]
                },
            },
            "chat_instance": "-6286455501612302882",
            "data": "margherita",
        },
    },
    {
        "update_id": 366965278,
        "callback_query": {
            "id": "3291890576786441353",
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "message": {
                "message_id": 376,
                "from": {
                    "id": 8669703310,
                    "is_bot": True,
                    "first_name": "Гончаренко Д.І. бот",
                    "username": "hdi_lesson_bot",
                },
                "chat": {
                    "id": 766453001,
                    "first_name": "Дмитро",
                    "last_name": "Гончаренко",
                    "type": "private",
                },
                "date": 1792497649,
                "text": "Будь ласка, оберіть розмір піци.",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {
                                "text": "Маленька (25 см.)",
                                "callback_data": "size_small",
                            },
                            {
                                "text": "Середня (30 см.)",
                                "callback_data": "size_medium",
                            },
                        ],
                        [
                            {"text": "Велика (35 см.)", "callback_data": "size_large"},
                            {
                                "text": "Дуже велика (40 см.)",
                                "callback_data": "size_super",
                            },
                        ],
                    ]
                },
            },
            "chat_instance": "-6286455501612302882",
            "data": "size_medium",
        },
    },
    {
        "update_id": 366965279,
        "callback_query": {
            "id": "3291890574318123889",
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "message": {
                "message_id": 377,
                "from": {
                    "id": 8669703310,
                    "is_bot": True,
                    "first_name": "Гончаренко Д.І. бот",
                    "username": "hdi_lesson_bot",
                },
                "chat": {
                    "id": 766453001,
                    "first_name": "Дмитро",
                    "last_name": "Гончаренко",
                    "type": "private",
                },
                "date": 1792497651,
                "text": "Будь ласка, оберіть напій.",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {"text": "Кока-кола", "callback_data": "coca_cola"},
                            {"text": "Пепсі", "callback_data": "pepsi"},
                        ],
                        [
                            {"text": "Апельсиновий сік", "callback_data": "orange_jus"},
                            {"text": "Яблучний сік", "callback_data": "apple_jus"},
                        ],
                        [{"text": "Без напою", "callback_data": "no_drinks"}],
                    ]
                },
            },
            "chat_instance": "-6286455501612302882",
            "data": "orange_jus",
        },
    },
    {
        "update_id": 366965280,
        "callback_query": {
            "id": "3291890577258082020",
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "message": {
                "message_id": 378,
                "from": {
                    "id": 8669703310,
                    "is_bot": True,
                    "first_name": "Гончаренко Д.І. бот",
                    "username": "hdi_lesson_bot",
                },
                "chat": {
                    "id": 766453001,
                    "first_name": "Дмитро",
                    "last_name": "Гончаренко",
                    "type": "private",
                },
                "date": 1792497654,
                "text": "Ви обрали:\n                піцу - Маргарита,\n                розмір - Середня (30 см.),\n                напій - Апельсиновий сік",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {"text": "Підтвердити", "callback_data": "approval"},
                            {"text": "Відмова", "callback_data": "cancel"},
                        ]
                    ]
                },
            },
            "chat_instance": "-6286455501612302882",
            "data": "approval",
        },
    },
    {
        "update_id": 366965281,
        "message": {
            "message_id": 380,
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "chat": {
                "id": 766453001,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "type": "private",
            },
            "date": 1792554922,
            "text": "Старт",
        },
    },
    {
        "update_id": 366965282,
        "callback_query": {
            "id": "3291890573887084491",
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "message": {
                "message_id": 382,
                "from": {
                    "id": 8669703310,
                    "is_bot": True,
                    "first_name": "Гончаренко Д.І. бот",
                    "username": "hdi_lesson_bot",
                },
                "chat": {
                    "id": 766453001,
                    "first_name": "Дмитро",
                    "last_name": "Гончаренко",
                    "type": "private",
                },
                "date": 1792554923,
                "text": "Будь ласка, оберіть Вашу піцу.",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {"text": "Маргарита", "callback_data": "margherita"},
                            {"text": "Пеппероні", "callback_data": "pepperoni"},
                        ],
                        [
                            {"text": "Чотири сира", "callback_data": "four_cheeses"},
                            {"text": "Гавайська", "callback_data": "hawaiian"},
                        ],
                        [
                            {"text": "Куриця барбекю", "callback_data": "bbq_chicken"},
                            {"text": "М'ясна", "callback_data": "all_meet"},
                        ],
                        [{"text": "Вегетаріанська", "callback_data": "vegetarian"}],
                    ]
                },
            },
            "chat_instance": "-6286455501612302882",
            "data": "pepperoni",
        },
    },
    {
        "update_id": 366965283,
        "callback_query": {
            "id": "3291890575487397932",
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "message": {
                "message_id": 383,
                "from": {
                    "id": 8669703310,
                    "is_bot": True,
                    "first_name": "Гончаренко Д.І. бот",
                    "username": "hdi_lesson_bot",
                },
                "chat": {
                    "id": 766453001,
                    "first_name": "Дмитро",
                    "last_name": "Гончаренко",
                    "type": "private",
                },
                "date": 1792554926,
                "text": "Будь ласка, оберіть розмір піци.",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {
                                "text": "Маленька (25 см.)",
                                "callback_data": "size_small",
                            },
                            {
                                "text": "Середня (30 см.)",
                                "callback_data": "size_medium",
                            },
                        ],
                        [
                            {"text": "Велика (35 см.)", "callback_data": "size_large"},
                            {
                                "text": "Дуже велика (40 см.)",
                                "callback_data": "size_super",
                            },
                        ],
                    ]
                },
            },
            "chat_instance": "-6286455501612302882",
            "data": "size_medium",
        },
    },
    {
        "update_id": 366965284,
        "callback_query": {
            "id": "3291890574003465801",
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "message": {
                "message_id": 384,
                "from": {
                    "id": 8669703310,
                    "is_bot": True,
                    "first_name": "Гончаренко Д.І. бот",
                    "username": "hdi_lesson_bot",
                },
                "chat": {
                    "id": 766453001,
                    "first_name": "Дмитро",
                    "last_name": "Гончаренко",
                    "type": "private",
                },
                "date": 1792554930,
                "text": "Будь ласка, оберіть напій.",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {"text": "Кока-кола", "callback_data": "coca_cola"},
                            {"text": "Пепсі", "callback_data": "pepsi"},
                        ],
                        [
                            {"text": "Апельсиновий сік", "callback_data": "orange_jus"},
                            {"text": "Яблучний сік", "callback_data": "apple_jus"},
                        ],
                        [{"text": "Без напою", "callback_data": "no_drinks"}],
                    ]
                },
            },
            "chat_instance": "-6286455501612302882",
            "data": "pepsi",
        },
    },
    {
        "update_id": 366965285,
        "callback_query": {
            "id": "3291890574549200929",
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "message": {
                "message_id": 385,
                "from": {
                    "id": 8669703310,
                    "is_bot": True,
                    "first_name": "Гончаренко Д.І. бот",
                    "username": "hdi_lesson_bot",
                },
                "chat": {
                    "id": 766453001,
                    "first_name": "Дмитро",
                    "last_name": "Гончаренко",
                    "type": "private",
                },
                "date": 1792554933,
                "text": "Ви обрали:\n                піцу - Пеппероні,\n                розмір - Середня (30 см.),\n                напій - Пепсі",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {"text": "Підтвердити", "callback_data": "approval"},
                            {"text": "Відмова", "callback_data": "cancel"},
                        ]
                    ]
                },
            },
            "chat_instance": "-6286455501612302882",
            "data": "approval",
        },
    },
    {
        "update_id": 366965286,
        "message": {
            "message_id": 387,
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "chat": {
                "id": 766453001,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "type": "private",
            },
            "date": 1792555188,
            "text": "Старт",
        },
    },
    {
        "update_id": 366965287,
        "callback_query": {
            "id": "3291890573755691398",
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "message": {
                "message_id": 389,
                "from": {
                    "id": 8669703310,
                    "is_bot": True,
                    "first_name": "Гончаренко Д.І. бот",
                    "username": "hdi_lesson_bot",
                },
                "chat": {
                    "id": 766453001,
                    "first_name": "Дмитро",
                    "last_name": "Гончаренко",
                    "type": "private",
                },
                "date": 1792555189,
                "text": "Будь ласка, оберіть Вашу піцу.",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {"text": "Маргарита", "callback_data": "margherita"},
                            {"text": "Пеппероні", "callback_data": "pepperoni"},
                        ],
                        [
                            {"text": "Чотири сира", "callback_data": "four_cheeses"},
                            {"text": "Гавайська", "callback_data": "hawaiian"},
                        ],
                        [
                            {"text": "Куриця барбекю", "callback_data": "bbq_chicken"},
                            {"text": "М'ясна", "callback_data": "all_meet"},
                        ],
                        [{"text": "Вегетаріанська", "callback_data": "vegetarian"}],
                    ]
                },
            },
            "chat_instance": "-6286455501612302882",
            "data": "vegetarian",
        },
    },
    {
        "update_id": 366965288,
        "callback_query": {
            "id": "3291890573965539121",
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "message": {
                "message_id": 390,
                "from": {
                    "id": 8669703310,
                    "is_bot": True,
                    "first_name": "Гончаренко Д.І. бот",
                    "username": "hdi_lesson_bot",
                },
                "chat": {
                    "id": 766453001,
                    "first_name": "Дмитро",
                    "last_name": "Гончаренко",
                    "type": "private",
                },
                "date": 1792555191,
                "text": "Будь ласка, оберіть розмір піци.",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {
                                "text": "Маленька (25 см.)",
                                "callback_data": "size_small",
                            },
                            {
                                "text": "Середня (30 см.)",
                                "callback_data": "size_medium",
                            },
                        ],
                        [
                            {"text": "Велика (35 см.)", "callback_data": "size_large"},
                            {
                                "text": "Дуже велика (40 см.)",
                                "callback_data": "size_super",
                            },
                        ],
                    ]
                },
            },
            "chat_instance": "-6286455501612302882",
            "data": "size_small",
        },
    },
    {
        "update_id": 366965289,
        "callback_query": {
            "id": "3291890574577723719",
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "message": {
                "message_id": 391,
                "from": {
                    "id": 8669703310,
                    "is_bot": True,
                    "first_name": "Гончаренко Д.І. бот",
                    "username": "hdi_lesson_bot",
                },
                "chat": {
                    "id": 766453001,
                    "first_name": "Дмитро",
                    "last_name": "Гончаренко",
                    "type": "private",
                },
                "date": 1792555196,
                "text": "Будь ласка, оберіть напій.",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {"text": "Кока-кола", "callback_data": "coca_cola"},
                            {"text": "Пепсі", "callback_data": "pepsi"},
                        ],
                        [
                            {"text": "Апельсиновий сік", "callback_data": "orange_jus"},
                            {"text": "Яблучний сік", "callback_data": "apple_jus"},
                        ],
                        [{"text": "Без напою", "callback_data": "no_drinks"}],
                    ]
                },
            },
            "chat_instance": "-6286455501612302882",
            "data": "no_drinks",
        },
    },
    {
        "update_id": 366965290,
        "callback_query": {
            "id": "3291890575556033699",
            "from": {
                "id": 766453001,
                "is_bot": False,
                "first_name": "Дмитро",
                "last_name": "Гончаренко",
                "language_code": "ru",
            },
            "message": {
                "message_id": 392,
                "from": {
                    "id": 8669703310,
                    "is_bot": True,
                    "first_name": "Гончаренко Д.І. бот",
                    "username": "hdi_lesson_bot",
                },
                "chat": {
                    "id": 766453001,
                    "first_name": "Дмитро",
                    "last_name": "Гончаренко",
                    "type": "private",
                },
                "date": 1792555201,
                "text": "Ви обрали:\n                піцу - Вегетаріанська,\n                розмір - Маленька (25 см.),\n                напій - Без напою",
                "reply_markup": {
                    "inline_keyboard": [
                        [
                            {"text": "Підтвердити", "callback_data": "approval"},
                            {"text": "Відмова", "callback_data": "cancel"},
                        ]
                    ]
                },
            },
            "chat_instance": "-6286455501612302882",
            "data": "approval",
        },
    },
]
