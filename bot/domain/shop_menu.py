from enum import StrEnum


class States(StrEnum):
    WAIT_FOR_GOOD_TYPE = "wait_for_good_type"


MENU_WAIT_FOR_GOOD_TYPE = {"pizza": "Піца", "drinks": "Напої", "cancel": "Відмова"}


def build_inline_keyboard(menu: dict) -> list:
    result = []
    Index = 0
    for key, value in menu.items():
        row, column = divmod(Index, 2)
        if column == 0:
            result.append([])
        result[row].append({"text": value, "callback_data": key})
        Index += 1  # noqa: SIM113

    return result
