# Тестові дані для таблиці goods {
# id SERIAL PRIMARY KEY,
# goods_type VARCHAR(10) NOT NULL,
# goods_name VARCHAR(40) NOT NULL,
# goods_label TEXT NOT NULL,
# goods_size VARCHAR(10),
# goods_size_label VARCHAR(40),
# goods_price INT,
# created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
# }
TEST_GOODS = [
    ("pizza", "margherita", "Маргарита", "size_small", "Маленька (25 см.)", 23000),
    ("pizza", "margherita", "Маргарита", "size_medium", "Середня (30 см.)", 25000),
    ("pizza", "margherita", "Маргарита", "size_large", "Велика (35 см.)", 27000),
    ("pizza", "margherita", "Маргарита", "size_super", "Дуже велика (40 см.)", 29000),
    ("pizza", "pepperoni", "Пеппероні", "size_small", "Маленька (25 см.)", 26000),
    ("pizza", "pepperoni", "Пеппероні", "size_medium", "Середня (30 см.)", 28000),
    ("pizza", "pepperoni", "Пеппероні", "size_large", "Велика (35 см.)", 30000),
    ("pizza", "pepperoni", "Пеппероні", "size_super", "Дуже велика (40 см.)", 32000),
    ("pizza", "four_cheeses", "Чотири сира", "size_small", "Маленька (25 см.)", 33000),
    ("pizza", "four_cheeses", "Чотири сира", "size_medium", "Середня (30 см.)", 35000),
    ("pizza", "four_cheeses", "Чотири сира", "size_large", "Велика (35 см.)", 37000),
    (
        "pizza",
        "four_cheeses",
        "Чотири сира",
        "size_super",
        "Дуже велика (40 см.)",
        39000,
    ),
    ("pizza", "hawaiian", "Гавайська", "size_small", "Маленька (25 см.)", 21000),
    ("pizza", "hawaiian", "Гавайська", "size_medium", "Середня (30 см.)", 22000),
    ("pizza", "hawaiian", "Гавайська", "size_large", "Велика (35 см.)", 23000),
    ("pizza", "hawaiian", "Гавайська", "size_super", "Дуже велика (40 см.)", 24000),
    (
        "pizza",
        "bbq_chicken",
        "Куриця барбекю",
        "size_small",
        "Маленька (25 см.)",
        23000,
    ),
    (
        "pizza",
        "bbq_chicken",
        "Куриця барбекю",
        "size_medium",
        "Середня (30 см.)",
        25000,
    ),
    ("pizza", "bbq_chicken", "Куриця барбекю", "size_large", "Велика (35 см.)", 27000),
    (
        "pizza",
        "bbq_chicken",
        "Куриця барбекю",
        "size_super",
        "Дуже велика (40 см.)",
        29000,
    ),
    ("pizza", "all_meet", "М'ясна", "size_small", "Маленька (25 см.)", 23000),
    ("pizza", "all_meet", "М'ясна", "size_medium", "Середня (30 см.)", 25000),
    ("pizza", "all_meet", "М'ясна", "size_large", "Велика (35 см.)", 27000),
    ("pizza", "all_meet", "М'ясна", "size_super", "Дуже велика (40 см.)", 29000),
    ("pizza", "vegetarian", "Вегетаріанська", "size_small", "Маленька (25 см.)", 23000),
    ("pizza", "vegetarian", "Вегетаріанська", "size_medium", "Середня (30 см.)", 25000),
    ("pizza", "vegetarian", "Вегетаріанська", "size_large", "Велика (35 см.)", 27000),
    (
        "pizza",
        "vegetarian",
        "Вегетаріанська",
        "size_super",
        "Дуже велика (40 см.)",
        29000,
    ),
    ("drink", "coca_cola", "Кока-кола", "small", "0,25 л.", 1200),
    ("drink", "coca_cola", "Кока-кола", "medium", "0,5 л.", 2400),
    ("drink", "coca_cola", "Кока-кола", "large", "1 л.", 4800),
    ("drink", "pepsi", "Пепсі", "small", "0,25 л.", 1200),
    ("drink", "pepsi", "Пепсі", "medium", "0,5 л.", 2400),
    ("drink", "pepsi", "Пепсі", "large", "1 л.", 4800),
    ("drink", "orange_jus", "Апельсиновий сік", "small", "0,25 л.", 1200),
    ("drink", "orange_jus", "Апельсиновий сік", "medium", "0,5 л.", 2400),
    ("drink", "orange_jus", "Апельсиновий сік", "large", "1 л.", 4800),
    ("drink", "apple_jus", "Яблучний сік", "small", "0,25 л.", 1200),
    ("drink", "apple_jus", "Яблучний сік", "medium", "0,5 л.", 2400),
    ("drink", "apple_jus", "Яблучний сік", "large", "1 л.", 4800),
]


def get_goods_types() -> list:
    result = []
    current = ""
    for item in TEST_GOODS:
        if item[0] != current:
            result.append(item[0])
            current = item[0]
    return result


if __name__ == "__main__":
    print(get_goods_types())
