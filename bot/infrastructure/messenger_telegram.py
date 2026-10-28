import logging
import os
import time

import aiohttp
from dotenv import load_dotenv

from bot.domain.messenger import Messenger

load_dotenv(override=True)

# Налаштування логування для обробки updates
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s.%(msecs)03d] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


class MessengerTelegram(Messenger):
    def __init__(self):
        self._session: aiohttp.ClientSession | None = None

    def _get_telegram_base_uri(self) -> str:
        return f"https://api.telegram.org/bot{os.getenv('TELEGRAM_TOKEN')}"

    async def _get_session(self) -> aiohttp.ClientSession:
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession()
        return self._session

    async def close(self):
        if self._session and not self._session.closed:
            await self._session.close()

    async def _make_request(self, method: str, **kwargs):
        start_time = time.time()
        logger.info(f"[HTTP] - POST {method}")

        json_data = kwargs

        session = await self._get_session()
        url = f"{self._get_telegram_base_uri()}/{method}"
        try:
            async with session.post(url=url, json=json_data) as response:
                response_json = await response.json()
                assert response_json["ok"] == True

                duration_ms = (time.time() - start_time) * 1000
                logger.info(f"[HTTP]- POST {method} - finished {duration_ms:.2f}ms")

                return response_json["result"]
        except Exception as e:
            duration_ms = (time.time() - start_time) * 1000
            logger.error(
                f"[HTTP] - POST {method} - failed {duration_ms:.2f}ms. Error - {e}"
            )
            raise

    async def get_updates(self, timeout: int, **kwargs) -> list[dict]:
        """
        Reference of the method:  https://core.telegram.org/bots/api#getupdates
        Returned:   List of Update object
        Reference of the update object:  https://core.telegram.org/bots/api#update
        """
        return await self._make_request("getUpdates", timeout=timeout, **kwargs)

    async def send_message(self, chat_id: int, text: str, **kwargs) -> dict:
        """
        Reference of the method:  https://core.telegram.org/bots/api#sendmessage
        Returned:   Message object
        Reference of the Message object  https://core.telegram.org/bots/api#message
        """
        return await self._make_request(
            "sendMessage", chat_id=chat_id, text=text, **kwargs
        )

    async def answer_callback_query(self, callback_query_id: str) -> bool:
        """
        Reference of the method:  https://core.telegram.org/bots/api#answercallbackquery
        Returned:   True
        """
        return await self._make_request(
            "answerCallbackQuery", callback_query_id=callback_query_id
        )

    async def delete_message(self, chat_id: int, message_id: int) -> bool:
        """
        Reference of the method:  https://core.telegram.org/bots/api#deletemessage
        Returned:   True
        """
        return await self._make_request(
            "deleteMessage", chat_id=chat_id, message_id=message_id
        )
