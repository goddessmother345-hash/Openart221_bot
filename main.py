import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from config.settings import settings
from database.connection import init_db
from middlewares.auth import UserAuthMiddleware

# Handlers
from handlers import start, market, ai

logging.basicConfig(level=logging.INFO)

async def main():
    await init_db()

    bot = Bot(
        token=settings.BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN)
    )
    dp = Dispatcher()

    # Register Middlewares
    dp.message.outer_middleware(UserAuthMiddleware())

    # Include Routers
    dp.include_router(start.router)
    dp.include_router(market.router)
    dp.include_router(ai.router)

    logging.info("🚀 NexapTrade Bot starting...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
