import asyncio
import logging
from bot_config import dp, bot
from handlers.advertisement import advertisement_router
from handlers.dishes_catalog import catalog_router
from handlers.feedback import feedback_router
from handlers.myinfo import myinfo_router
from handlers.other_messages import other_router
from handlers.random import random_router
from handlers.review_dialog import review_router
from handlers.start import start_router


async def main():
    dp.include_router(start_router)
    dp.include_router(myinfo_router)
    dp.include_router(random_router)
    dp.include_router(advertisement_router)
    dp.include_router(catalog_router)
    dp.include_router(feedback_router)
    dp.include_router(review_router)

    dp.include_router(other_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())