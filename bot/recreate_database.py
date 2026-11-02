import asyncio

from bot.domain.storage import Storage
from bot.infrastructure.storage_postgres import StoragePostgres


async def main():
    storage: Storage = StoragePostgres()
    try:
        await storage.recreate_database()
    finally:
        if hasattr(storage, "close"):
            await storage.close()


asyncio.run(main())
