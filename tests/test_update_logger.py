import pytest

from bot.dispatcher import Dispatcher
from bot.handlers.update_logger import UpdateLogger
from tests.mock import Mock
from tests.updates import get_telegram_id_from_update, updates


@pytest.mark.asyncio
async def test_update_logger_execution():
    current_telegram_id  = 0
    persist_update_called_count = 0

    async def persist_update(update: dict) -> None:
        nonlocal persist_update_called_count
        persist_update_called_count += 1

    async def get_user(telegram_id: int) -> dict | None:
        nonlocal current_telegram_id
        assert telegram_id == current_telegram_id
        return None

    mock_storage = Mock(
        {
            "persist_update": persist_update,
            "get_user": get_user,
        }
    )

    mock_messenger = Mock({})

    dispatcher = Dispatcher(mock_storage, mock_messenger)
    dispatcher.add_handlers(UpdateLogger())
    for update in updates:
        current_telegram_id = get_telegram_id_from_update(update)
        await dispatcher.dispatch(update)

    assert persist_update_called_count == len(updates)
