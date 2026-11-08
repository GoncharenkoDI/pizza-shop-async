from bot.domain.messenger import Messenger
from bot.domain.storage import Storage
from bot.handlers.handler import Handler, HandlerStatus


class EnsureUserExists(Handler):
    def can_handle(
        self,
        update: dict,
        state: str | None,
        order_data: list[dict],
    ) -> bool:
        return "message" in update and "from" in update["message"]

    async def handle(
        self,
        update: dict,
        state: str | None,
        order_data: list[dict],
        storage: Storage,
        messenger: Messenger,
    ) -> HandlerStatus:
        telegram_id = update["message"]["from"]["id"]
        await storage.ensure_user_exists(telegram_id)
        return HandlerStatus.CONTINUE
