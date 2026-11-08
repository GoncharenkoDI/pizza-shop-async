import json

from bot.domain.messenger import Messenger
from bot.domain.shop_menu import menu_wait_for_good_type, States, build_inline_keyboard
from bot.domain.storage import Storage
from bot.handlers.handler import Handler, HandlerStatus


class MessageStart(Handler):
    def can_handle(
        self,
        update: dict,
        state: str,
        order_data: dict,
    ) -> bool:
        return (
            "message" in update
            and "text" in update["message"]
            and update["message"]["text"] == "/start"
        )

    async def handle(
        self,
        update: dict,
        state: str,
        order_data: dict,
        storage: Storage,
        messenger: Messenger,
    ) -> HandlerStatus:
        telegram_id = update["message"]["from"]["id"]
        chat_id = update["message"]["chat"]["id"]
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
                {"inline_keyboard": build_inline_keyboard(menu_wait_for_good_type)}
            ),
        )

        return HandlerStatus.STOP
