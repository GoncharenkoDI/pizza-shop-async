from bot.handlers.ensure_user_exists import EnsureUserExists
from bot.handlers.handler import Handler
from bot.handlers.message_start import MessageStart
from bot.handlers.update_logger import UpdateLogger


def get_handlers() -> list[Handler]:
    return [UpdateLogger(), EnsureUserExists(), MessageStart()]
