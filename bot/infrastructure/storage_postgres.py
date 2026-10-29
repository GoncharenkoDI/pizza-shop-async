import logging
import os
import time

import asyncpg
from dotenv import load_dotenv

from bot.domain.storage import Storage

load_dotenv(override=True)

# Налаштування логування для обробки запитів до БД
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s.%(msecs)03d] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


class StoragePostgres(Storage):
    def __init__(self):
        self._pool: asyncpg.Pool | None = None

    async def _get_pool(self):
        if self._pool is None:
            host = os.getenv("POSTGRES_HOST")
            port = os.getenv("POSTGRES_PORT")
            user = os.getenv("POSTGRES_USER")
            password = os.getenv("POSTGRES_PASSWORD")
            database = os.getenv("POSTGRES_DB")
            if host is None:
                raise ValueError("POSTGRES_HOST value is not set!!!")
            if port is None:
                raise ValueError("POSTGRES_PORT value is not set!!!")
            if user is None:
                raise ValueError("POSTGRES_USER value is not set!!!")
            if password is None:
                raise ValueError("POSTGRES_PASSWORD value is not set!!!")
            if database is None:
                raise ValueError("POSTGRES_DB value is not set!!!")

            self._pool = await asyncpg.create_pool(
                user=user,
                password=password,
                database=database,
                host=host,
                port=port,
                min_size=25,
                max_size=25,
            )
        return self._pool

    async def close(self):
        if self._pool:
            await self._pool.close()
            self._pool = None

    async def recreate_database(self) -> None:
        method_name = "recreate_database"
        start_time = time.time()
        logger.info(f"[DB] start {method_name}")
        try:
            pool: asyncpg.Pool = await self._get_pool()
            async with pool.acquire() as conn:
                await conn.execute("""
                    CREATE TABLE IF NOT EXISTS telegram_events
                    (
                        id SERIAL PRIMARY KEY,
                        payload TEXT NOT NULL
                    )
                """)
                await conn.execute("""
                    CREATE TABLE IF NOT EXISTS users
                    (
                        id SERIAL PRIMARY KEY,
                        telegram_id BIGINT NOT NULL UNIQUE,
                        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                        state TEXT DEFAULT NULL,
                        order_json TEXT DEFAULT NULL
                    )
                """)
                await conn.execute("""
                    CREATE TABLE IF NOT EXISTS goods
                    (
                        id SERIAL PRIMARY KEY,
                        goods_type VARCHAR(10) NOT NULL,
                        goods_name VARCHAR(40) NOT NULL,
                        goods_label TEXT NOT NULL,
                        goods_size VARCHAR(10),
                        goods_size_label VARCHAR(40),
                        goods_price INT,
                        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
                    ) 
                """)
            duration_ms = (time.time() - start_time) * 1000
            logger.info(f"[DB] finished {method_name} - {duration_ms:.2f}ms")
        except Exception as e:
            duration_ms = (time.time() - start_time) * 1000
            logger.error(
                f"[DB] failed {method_name} - {duration_ms:.2f}ms. Error:- {e}"
            )
            raise

    async def persist_updates(self, updates: list[dict]) -> None: ...

    async def persist_update(self, update: dict) -> None: ...

    async def ensure_user_exists(self, telegram_id: int) -> None:
        """
        Ensure a users with given telegram_id exists in users table.
        If user doesn't exists, create them.
        All operation happen in single transaction.
        """

    async def clear_user_state(self, telegram_id: int) -> None:
        """Clear user state and order_json in table users"""

    async def update_user_state(self, telegram_id: int, state: str) -> None:
        """Update user state in table users"""

    async def update_user_order_json(self, telegram_id: int, order_data: dict) -> None:
        """Update user state in table users"""

    async def get_user(self, telegram_id: int) -> dict:
        """
        Get complete user object from table users by telegram_id
        {id, telegram_id, created_at, state, order_json}
        """
