from enum import StrEnum

from bot.domain.goods import labels


class States(StrEnum):
    WAIT_FOR_GOOD_TYPE = "wait_for_good_type"
    WAIT_FOR_GOOD_NAME = "wait_for_good_name"


def build_inline_keyboard(menu: dict) -> list:
    result: list[list[dict]] = []
    Index = 0
    for key, value in menu.items():
        row, column = divmod(Index, 2)
        if column == 0:
            result.append([])
        result[row].append({"text": value, "callback_data": key})
        Index += 1  # noqa: SIM113

    result.append(
        [
            {"text": "Відмінити товар", "callback_data": "cancel"},
        ]
    )
    result.append(
        [
            {"text": "Скасувати замовлення", "callback_data": "cancel_order"},
        ]
    )

    return result


def build_order_info(order_data: list[dict]) -> str:
    goods = []
    for order_item in order_data:
        fields = [
            f"{label}: {order_item[key]}"
            for key, label in labels.items()
            if order_item.get(key) not in (None, "")
        ]
        goods.append(", ".join(fields))
    return "\n".join(goods)


if __name__ == "__main__":
    import json

    from bot.domain.goods import get_goods_types

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
            "goods_type": "Одяг",
            "goods_name": "штани спортивні",
            "goods_price": 180,
            "goods_quantity": 1,
            # goods_type, goods_size та goods_cost відсутні
        },
        {
            "goods_type": "Взуття",
            "goods_name": "Кросівки",
            "goods_size": 42,
            "goods_price": 2500,
        },
    ]
    print(build_order_info(products))
    # inline_keyboard = build_inline_keyboard(get_goods_types())
    print(
        json.dumps(
            {"inline_keyboard": build_inline_keyboard(get_goods_types())},
            ensure_ascii=False,
        )
    )
