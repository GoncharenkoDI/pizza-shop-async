import asyncio
from bot.domain.storage import Storage
from bot.infrastructure.storage_postgres import StoragePostgres

async def main():
    storage: Storage = StoragePostgres()
    await storage.recreate_database()

asyncio.run(main())