from bot.domain.messenger import Messenger
from bot.domain.storage import Storage
from bot.handlers.handler import Handler, HandlerStatus


class UpdateLogger(Handler):
    def can_handle(
        self,
        update: dict,
        state: str,
        order_data: dict,
    ) -> bool:
        return True

    async def handle(
        self,
        update: dict,
        state: str,
        order_data: dict,
        storage: Storage,
        messenger: Messenger,
    ) -> HandlerStatus:
        await storage.persist_update(update)
        return HandlerStatus.CONTINUE
