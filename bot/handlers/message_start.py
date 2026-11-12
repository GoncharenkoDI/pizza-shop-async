import json
import logging
import time

from bot.domain.goods import get_goods_types
from bot.domain.messenger import Messenger
from bot.domain.shop_menu import States, build_inline_keyboard
from bot.domain.storage import Storage
from bot.handlers.handler import Handler, HandlerStatus

# Налаштування логування для обробки запитів до БД
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s.%(msecs)03d] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


class MessageStart(Handler):
    def can_handle(
        self,
        update: dict,
        state: str | None,
        order_data: list[dict],
    ) -> bool:
        return (
            "message" in update
            and "text" in update["message"]
            and update["message"]["text"] == "/start"
        )

    async def handle(
        self,
        update: dict,
        state: str | None,
        order_data: list[dict],
        storage: Storage,
        messenger: Messenger,
    ) -> HandlerStatus:
        method_name = "MessageStart handle"
        start_time = time.time()
        logger.info(f"[{method_name}] - start")

        telegram_id = update["message"]["from"]["id"]
        chat_id = update["message"]["chat"]["id"]
        try:
            await storage.clear_user_state(telegram_id)
            await storage.update_user_state(telegram_id, States.WAIT_FOR_GOOD_TYPE)
            await messenger.send_message(
                chat_id=chat_id,
                text="🍕 Вітаю в магазині PIZZA SHOP.\n",
                reply_markup=json.dumps({"remove_keyboard": True}),
            )
            await messenger.send_message(
                chat_id=chat_id,
                text="Будь ласка. Оберіть тип товару, який ви хочете замовити.\n",
                reply_markup=json.dumps(
                    {"inline_keyboard": build_inline_keyboard(get_goods_types())}
                ),
            )
            duration_ms = (time.time() - start_time) * 1000
            logger.info(f"[{method_name}] - finished - {duration_ms:.2f}ms")
        except Exception as e:
            duration_ms = (time.time() - start_time) * 1000
            logger.error(f"[{method_name}] failed - {duration_ms:.2f}ms. Error:- {e}")
            raise

        return HandlerStatus.STOP
