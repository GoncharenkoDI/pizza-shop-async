import json
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

    async def persist_update(self, update: dict) -> None:
        start_time = time.time()
        method_name = "persist_update"
        sql = "INSERT INTO telegram_events (payload) VALUES ($1)"
        payload: str = json.dumps(update, ensure_ascii=False, indent=2)
        logger.info(f"[DB] - {method_name} {sql}- start")
        try:
            pool: asyncpg.Pool = await self._get_pool()
            async with pool.acquire() as conn:
                await conn.execute(sql, payload)

            duration_ms = (time.time() - start_time) * 1000
            logger.info(f"[DB] finished {method_name} - {duration_ms:.2f}ms")
        except Exception as e:
            duration_ms = (time.time() - start_time) * 1000
            logger.error(
                f"[DB] failed {method_name} - {duration_ms:.2f}ms. Error:- {e}"
            )
            raise

    async def _is_user_exists(
        self, connection: asyncpg.Connection, telegram_id: int, method_name: str
    ) -> bool:
        start_time = time.time()
        sql = "SELECT 1 FROM users WHERE telegram_id = $1"
        logger.info(f"[DB] - {method_name} - {sql} - start")
        row = await connection.fetchrow(sql, telegram_id)
        duration_ms = (time.time() - start_time) * 1000
        logger.info(f"[DB] - {method_name} {sql} - finished - {duration_ms:.2f}ms.")
        return row is not None

    async def _insert_user(
        self, connection: asyncpg.Connection, telegram_id: int, method_name: str
    ) -> None:
        start_time = time.time()
        sql = "INSERT INTO users (telegram_id) VALUES ($1)"
        logger.info(f"[DB] - {method_name} - {sql} - start")
        await connection.execute(sql, telegram_id)
        duration_ms = (time.time() - start_time) * 1000
        logger.info(f"[DB] - {method_name} {sql} - finished - {duration_ms:.2f}ms.")

    async def ensure_user_exists(self, telegram_id: int) -> None:
        """
        Ensure a users with given telegram_id exists in users table.
        If user doesn't exists, create them.
        All operation happen in single transaction.
        """
        start_time = time.time()
        method_name = "ensure_user_exists"
        logger.info(f"[DB] - {method_name} - start")
        try:
            pool: asyncpg.Pool = await self._get_pool()
            async with pool.acquire() as conn:
                if not await self._is_user_exists(conn, telegram_id, method_name):
                    await self._insert_user(conn, telegram_id, method_name)
            duration_ms = (time.time() - start_time) * 1000
            logger.info(f"[DB] - {method_name} - finished - {duration_ms:.2f}ms.")
        except Exception as e:
            duration_ms = (time.time() - start_time) * 1000
            logger.error(
                f"[DB] - {method_name} - failed - {duration_ms:.2f}ms. Error: {e}"
            )
            raise

    async def clear_user_state(self, telegram_id: int) -> None:
        """Clear user state and order_json in table users"""
        sql = "UPDATE users SET state=NULL, order_json = NULL WHERE telegram_id = $1"
        start_time = time.time()
        method_name = "clear_user_state"
        logger.info(f"[DB] - {method_name} {sql} - start")
        try:
            pool: asyncpg.Pool = await self._get_pool()
            async with pool.acquire() as conn:
                await conn.execute(sql, telegram_id)
            duration_ms = (time.time() - start_time) * 1000
            logger.info(f"[DB] - {method_name} - finished - {duration_ms:.2f}ms")
        except Exception as e:
            duration_ms = (time.time() - start_time) * 1000
            logger.error(
                f"[DB] - {method_name} - failed - {duration_ms:.2f}ms. Error: {e}"
            )
            raise

    async def update_user_state(self, telegram_id: int, state: str) -> None:
        """Update user state in table users"""
        sql = "UPDATE users SET state=$1 WHERE telegram_id = $2"
        start_time = time.time()
        method_name = "update_user_state"
        logger.info(f"[DB] - {method_name} {sql} - start")
        try:
            pool: asyncpg.Pool = await self._get_pool()
            async with pool.acquire() as conn:
                await conn.execute(sql, state, telegram_id)
            duration_ms = (time.time() - start_time) * 1000
            logger.info(f"[DB] - {method_name} - finished - {duration_ms:.2f}ms")
        except Exception as e:
            duration_ms = (time.time() - start_time) * 1000
            logger.error(
                f"[DB] - {method_name} - failed - {duration_ms:.2f}ms. Error: {e}"
            )
            raise

    async def update_user_order_json(self, telegram_id: int, order_data: dict) -> None:
        """Update user state in table users"""
        sql = "UPDATE users SET order_json=$1 WHERE telegram_id = $2"
        start_time = time.time()
        method_name = "update_user_order_json"
        logger.info(f"[DB] - {method_name} {sql} - start")
        try:
            pool: asyncpg.Pool = await self._get_pool()
            async with pool.acquire() as conn:
                await conn.execute(
                    sql,
                    json.dumps(order_data, ensure_ascii=False, indent=2),
                    telegram_id,
                )
            duration_ms = (time.time() - start_time) * 1000
            logger.info(f"[DB] - {method_name} - finished - {duration_ms:.2f}ms")

        except Exception:
            duration_ms = (time.time() - start_time) * 1000
            logger.error(f"[DB] - {method_name} - failed - {duration_ms:.2f}ms")
            raise

    async def get_user(self, telegram_id: int) -> dict:
        """
        Get complete user object from table users by telegram_id
        {id, telegram_id, created_at, state, order_json}
        """
        sql = "SELECT id, telegram_id, created_at, state, order_json FROM users WHERE telegram_id = $1"
        method_name = "get_user"
        start_time = time.time()
        logger.info(f"[DB] - {method_name} - {sql} started.")
        try:
            pool: asyncpg.Pool = await self._get_pool()
            async with pool.acquire() as conn:
                result = await conn.fetchrow(sql, telegram_id)
            duration_ms = (time.time() - start_time) * 1000
            logger.info(f"[DB] - {method_name} finished - {duration_ms:.2f}ms.")
        except Exception:
            duration_ms = (time.time() - start_time) * 1000
            logger.error(f"[DB] - {method_name} failed - {duration_ms}ms.")
            raise
        if result:
            return {
                "id": result["id"],
                "telegram_id": result["telegram_id"],
                "created_at": result["created_at"],
                "state": result["state"],
                "order_json": result["order_json"],
            }
        return None
