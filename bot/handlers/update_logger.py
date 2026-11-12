import logging
import time

from bot.domain.messenger import Messenger
from bot.domain.storage import Storage
from bot.handlers.handler import Handler, HandlerStatus

# Налаштування логування для обробки запитів до БД
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s.%(msecs)03d] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


class UpdateLogger(Handler):
    def can_handle(
        self,
        update: dict,
        state: str | None,
        order_data: list[dict],
    ) -> bool:
        return True

    async def handle(
        self,
        update: dict,
        state: str | None,
        order_data: list[dict],
        storage: Storage,
        messenger: Messenger,
    ) -> HandlerStatus:
        method_name = "UpdateLogger handle"
        start_time = time.time()
        logger.info(f"[{method_name}] - start")

        try:
            await storage.persist_update(update)

            duration_ms = (time.time() - start_time) * 1000
            logger.info(f"[{method_name}] - finished - {duration_ms:.2f}ms")
        except Exception as e:
            duration_ms = (time.time() - start_time) * 1000
            logger.error(f"[{method_name}] failed - {duration_ms:.2f}ms. Error:- {e}")
            raise

        return HandlerStatus.CONTINUE
