from bot.handlers.handler import Handler
from bot.handlers.update_logger import UpdateLogger


def get_handlers() -> list[Handler]:
    return [UpdateLogger()]
