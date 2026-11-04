import pytest

from bot.dispatcher import Dispatcher
from bot.handlers.ensure_user_exists import EnsureUserExists
from tests.mock import Mock
from tests.updates import get_telegram_id_from_update, updates


@pytest.mark.asyncio
async def test_ensure_user_exits_execution():

    ensure_user_exists_called_count = 0
    for update in updates:
        if "message" in update and "from" in update["message"]:
            ensure_user_exists_called_count += 1

    async def ensure_user_exists(telegram_id: int) -> None:
        nonlocal current_telegram_id, ensure_user_exists_called_count
        assert telegram_id == current_telegram_id
        ensure_user_exists_called_count -= 1

    async def get_user(telegram_id: int) -> dict | None:
        """
        Get complete user object from table users by telegram_id
        {id, telegram_id, created_at, state, order_json}
        """
        nonlocal current_telegram_id
        assert telegram_id == current_telegram_id
        return None

    mock_storage = Mock(
        {
            "ensure_user_exists": ensure_user_exists,
            "get_user": get_user,
        }
    )

    mock_messenger = Mock({})

    dispatcher = Dispatcher(mock_storage, mock_messenger)
    dispatcher.add_handlers(EnsureUserExists())
    for update in updates:
        current_telegram_id = get_telegram_id_from_update(update)
        await dispatcher.dispatch(update)

    assert ensure_user_exists_called_count == 0
