from abc import ABC, abstractmethod
from enum import IntEnum

from bot.domain.messenger import Messenger
from bot.domain.storage import Storage


class HandlerStatus(IntEnum):
    CONTINUE = 1
    STOP = 2


class Handler(ABC):
    @abstractmethod
    def can_handle(
        self,
        update: dict,
        state: str,
        order_data: dict,
    ) -> bool: ...

    @abstractmethod
    def handle(
        self,
        update: dict,
        state: str,
        order_data: dict,
        storage: Storage,
        messenger: Messenger,
    ) -> HandlerStatus: ...
