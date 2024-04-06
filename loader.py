from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from config import settings


bot = Bot(
    token=settings.BOT_TOKEN,
    parse_mode=ParseMode.HTML,
    disable_web_page_preview=True,
)

dp = Dispatcher()
