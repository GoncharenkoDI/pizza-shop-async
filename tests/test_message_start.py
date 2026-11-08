import pytest

from bot.dispatcher import Dispatcher
from bot.domain.shop_menu import States
from bot.handlers.message_start import MessageStart
from tests.mock import Mock
from tests.updates import get_chat_id_from_update, get_telegram_id_from_update, updates


@pytest.mark.asyncio
async def test_message_start_execution():
    current_chat_id = 0
    current_telegram_id = 0
    send_message_texts = []
    clear_user_state_called_count = 0
    update_user_state_called = 0
    for update in updates:
        if (
            "message" in update
            and "text" in update["message"]
            and update["message"]["text"] == "/start"
        ):
            clear_user_state_called_count += 1
            update_user_state_called += 1

    async def clear_user_state(telegram_id: int) -> None:
        """Clear user state and order_json in table users"""
        nonlocal current_telegram_id, clear_user_state_called_count
        assert telegram_id == current_telegram_id
        clear_user_state_called_count -= 1

    async def update_user_state(telegram_id: int, state: str) -> None:
        """Update user state in table users"""
        nonlocal current_telegram_id, update_user_state_called
        assert telegram_id == current_telegram_id
        assert state == States.WAIT_FOR_GOOD_TYPE
        update_user_state_called -= 1

    async def get_user(telegram_id: int) -> dict | None:
        """
        Get complete user object from table users by telegram_id
        {id, telegram_id, created_at, state, order_json}
        """
        nonlocal current_telegram_id
        assert telegram_id == current_telegram_id
        return None

    async def send_message(chat_id: int, text: str, **kwargs) -> dict:
        nonlocal current_chat_id, send_message_texts
        assert chat_id == current_chat_id
        send_message_texts.append(text)
        return {}

    mock_storage = Mock(
        {
            "clear_user_state": clear_user_state,
            "update_user_state": update_user_state,
            "get_user": get_user,
        }
    )

    mock_messenger = Mock(
        {
            "send_message": send_message,
        }
    )

    dispatcher = Dispatcher(mock_storage, mock_messenger)
    dispatcher.add_handlers(MessageStart())
    for update in updates:
        current_telegram_id = get_telegram_id_from_update(update)
        current_chat_id = get_chat_id_from_update(update)
        send_message_texts = []
        await dispatcher.dispatch(update)
        if (
            "message" in update
            and "text" in update["message"]
            and update["message"]["text"] == "/start"
        ):
            assert len(send_message_texts) == 2
            assert send_message_texts[0] == "🍕 Вітаю в магазині PIZZA SHOP.\n"
            assert (
                send_message_texts[1]
                == "Будь ласка. Оберіть тип товару, який ви хочете замовити.\n"
            )

    assert clear_user_state_called_count == 0
    assert update_user_state_called == 0
