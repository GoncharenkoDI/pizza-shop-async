from abc import ABC, abstractmethod


class Messenger(ABC):

    @abstractmethod
    async def get_updates(self, timeout: int, **kwargs) -> list[dict]: ...

    @abstractmethod
    async def send_message(self, chat_id: int, text: str, **kwargs) -> dict: ...

    @abstractmethod
    async def answer_callback_query(self, callback_query_id: str) -> bool: ...

    @abstractmethod
    async def delete_message(self, chat_id: int, message_id: int) -> bool: ...
