# Тестові дані для таблиці goods {
# id SERIAL PRIMARY KEY,
# goods_type VARCHAR(10) NOT NULL,
# goods_type_label VARCHAR(10) NOT NULL,
# goods_name VARCHAR(40) NOT NULL,
# goods_label TEXT NOT NULL,
# goods_size VARCHAR(10),
# goods_size_label VARCHAR(40),
# goods_price INT,
# created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
# }
"""
products = [
    {
        "goods_type": "Одяг",
        "goods_name": "Футболка базова",
        "goods_size": "L",
        "goods_price": 450,
        "goods_quantity": 2,
        "goods_cost": 900,
    },
    {
        "goods_name": "Чашка керамічна",
        "goods_price": 180,
        "goods_quantity": 1,
        # goods_type, goods_size та goods_cost відсутні
    },
    {
        "goods_type": "Взуття",
        "goods_name": "Кросівки",
        "goods_size": 42,
        "goods_cost": 2500,
    },
]

# Словник для гарного відображення назв полів у потрібному порядку
labels = {
    "goods_type": "Тип",
    "goods_name": "Назва",
    "goods_size": "Розмір",
    "goods_price": "Ціна",
    "goods_quantity": "Кількість",
    "goods_cost": "Вартість",
}

lines = []
for item in products:
    # Збираємо тільки ті поля, які є в словнику і не дорівнюють None або порожньому рядку
    fields = [
        f"{label}: {item[key]}"
        for key, label in labels.items()
        if item.get(key) not in (None, "")
    ]
    # Об'єднуємо поля одного товару через кому
    lines.append(", ".join(fields))

# Об'єднуємо всі товари, щоб кожен був з нового рядка
result = "\n".join(lines)
"""

# Словник для гарного відображення назв полів у потрібному порядку
labels = {
    "goods_type": "Тип",
    "goods_name": "Назва",
    "goods_size": "Розмір",
    "goods_price": "Ціна",
    "goods_quantity": "Кількість",
    "goods_cost": "Вартість",
}


TEST_GOODS: list[tuple] = [
    (
        "pizza",
        "Піца",
        "margherita",
        "Маргарита",
        "size_small",
        "Маленька (25 см.)",
        23000,
    ),
    (
        "pizza",
        "Піца",
        "margherita",
        "Маргарита",
        "size_medium",
        "Середня (30 см.)",
        25000,
    ),
    (
        "pizza",
        "Піца",
        "margherita",
        "Маргарита",
        "size_large",
        "Велика (35 см.)",
        27000,
    ),
    (
        "pizza",
        "Піца",
        "margherita",
        "Маргарита",
        "size_super",
        "Дуже велика (40 см.)",
        29000,
    ),
    (
        "pizza",
        "Піца",
        "pepperoni",
        "Пеппероні",
        "size_small",
        "Маленька (25 см.)",
        26000,
    ),
    (
        "pizza",
        "Піца",
        "pepperoni",
        "Пеппероні",
        "size_medium",
        "Середня (30 см.)",
        28000,
    ),
    ("pizza", "Піца", "pepperoni", "Пеппероні", "size_large", "Велика (35 см.)", 30000),
    (
        "pizza",
        "Піца",
        "pepperoni",
        "Пеппероні",
        "size_super",
        "Дуже велика (40 см.)",
        32000,
    ),
    (
        "pizza",
        "Піца",
        "four_cheeses",
        "Чотири сира",
        "size_small",
        "Маленька (25 см.)",
        33000,
    ),
    (
        "pizza",
        "Піца",
        "four_cheeses",
        "Чотири сира",
        "size_medium",
        "Середня (30 см.)",
        35000,
    ),
    (
        "pizza",
        "Піца",
        "four_cheeses",
        "Чотири сира",
        "size_large",
        "Велика (35 см.)",
        37000,
    ),
    (
        "pizza",
        "Піца",
        "four_cheeses",
        "Чотири сира",
        "size_super",
        "Дуже велика (40 см.)",
        39000,
    ),
    (
        "pizza",
        "Піца",
        "hawaiian",
        "Гавайська",
        "size_small",
        "Маленька (25 см.)",
        21000,
    ),
    (
        "pizza",
        "Піца",
        "hawaiian",
        "Гавайська",
        "size_medium",
        "Середня (30 см.)",
        22000,
    ),
    ("pizza", "Піца", "hawaiian", "Гавайська", "size_large", "Велика (35 см.)", 23000),
    (
        "pizza",
        "Піца",
        "hawaiian",
        "Гавайська",
        "size_super",
        "Дуже велика (40 см.)",
        24000,
    ),
    (
        "pizza",
        "Піца",
        "bbq_chicken",
        "Куриця барбекю",
        "size_small",
        "Маленька (25 см.)",
        23000,
    ),
    (
        "pizza",
        "Піца",
        "bbq_chicken",
        "Куриця барбекю",
        "size_medium",
        "Середня (30 см.)",
        25000,
    ),
    ("pizza", "bbq_chicken", "Куриця барбекю", "size_large", "Велика (35 см.)", 27000),
    (
        "pizza",
        "Піца",
        "bbq_chicken",
        "Куриця барбекю",
        "size_super",
        "Дуже велика (40 см.)",
        29000,
    ),
    ("pizza", "Піца", "all_meet", "М'ясна", "size_small", "Маленька (25 см.)", 23000),
    ("pizza", "Піца", "all_meet", "М'ясна", "size_medium", "Середня (30 см.)", 25000),
    ("pizza", "Піца", "all_meet", "М'ясна", "size_large", "Велика (35 см.)", 27000),
    (
        "pizza",
        "Піца",
        "all_meet",
        "М'ясна",
        "size_super",
        "Дуже велика (40 см.)",
        29000,
    ),
    (
        "pizza",
        "Піца",
        "vegetarian",
        "Вегетаріанська",
        "size_small",
        "Маленька (25 см.)",
        23000,
    ),
    (
        "pizza",
        "Піца",
        "vegetarian",
        "Вегетаріанська",
        "size_medium",
        "Середня (30 см.)",
        25000,
    ),
    (
        "pizza",
        "Піца",
        "vegetarian",
        "Вегетаріанська",
        "size_large",
        "Велика (35 см.)",
        27000,
    ),
    (
        "pizza",
        "Піца",
        "vegetarian",
        "Вегетаріанська",
        "size_super",
        "Дуже велика (40 см.)",
        29000,
    ),
    ("drink", "Напій", "coca_cola", "Кока-кола", "small", "0,25 л.", 1200),
    ("drink", "Напій", "coca_cola", "Кока-кола", "medium", "0,5 л.", 2400),
    ("drink", "Напій", "coca_cola", "Кока-кола", "large", "1 л.", 4800),
    ("drink", "Напій", "pepsi", "Пепсі", "small", "0,25 л.", 1200),
    ("drink", "Напій", "pepsi", "Пепсі", "medium", "0,5 л.", 2400),
    ("drink", "Напій", "pepsi", "Пепсі", "large", "1 л.", 4800),
    ("drink", "Напій", "orange_jus", "Апельсиновий сік", "small", "0,25 л.", 1200),
    ("drink", "Напій", "orange_jus", "Апельсиновий сік", "medium", "0,5 л.", 2400),
    ("drink", "Напій", "orange_jus", "Апельсиновий сік", "large", "1 л.", 4800),
    ("drink", "Напій", "apple_jus", "Яблучний сік", "small", "0,25 л.", 1200),
    ("drink", "Напій", "apple_jus", "Яблучний сік", "medium", "0,5 л.", 2400),
    ("drink", "Напій", "apple_jus", "Яблучний сік", "large", "1 л.", 4800),
]


def get_goods_types() -> dict:
    result = {}
    current = ""
    for item in TEST_GOODS:
        if item[0] != current:
            result[item[0]] = item[1]
            current = item[0]
    return result


def get_goods_names(good_type: str) -> dict:
    result = {}
    current = ""
    for item in TEST_GOODS:
        if item[0] != good_type:
            continue
        if item[2] != current:
            result[item[2]] = item[3]
            current = item[2]
    return result


if __name__ == "__main__":
    print(get_goods_types())
    print(get_goods_names("pizza"))
    print(get_goods_names("drink"))
