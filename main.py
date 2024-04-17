import asyncio
from loader import bot
from database.db import create_database
from handlers import dp
from database.crud.update import user_to_administrator
from database.crud.create import create_user


async def start():
    create_database()
    try:
        create_user(telegram_id=853739584,
                    phone_number="+79136874480",
                    username="borodis05")
        user_to_administrator(853739584)
    except Exception:
        pass
    await bot.delete_webhook(True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(start())

