import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from config import settings
from app.handlers import common, ocr
from app.utils.set_commands import set_default_commands
from app.middlewares.throttling import ThrottlingMiddleware


async def main():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode='HTML'))
    dp = Dispatcher()

    dp.message.middleware(ThrottlingMiddleware())
    dp.include_router(common.router)
    dp.include_router(ocr.router)

    await set_default_commands(bot)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
