import asyncio
from loader import bot
from database.db import create_database
from handlers import dp


async def start():
    create_database()
    await bot.delete_webhook(True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(start())

