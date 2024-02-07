import asyncio
from aiogram import Dispatcher
from tg_api.loader import bot_init
from tg_api.utils.set_bot_commands import set_main_menu, set_discription
from tg_api.handlers.default_handlers import start, help, echo
from tg_api.handlers.custom_handlers import find_film


async def main():
    bot = bot_init
    dp = Dispatcher()
    await set_main_menu(bot)
    await set_discription(bot)

    dp.include_router(start.router)
    dp.include_router(find_film.router)
    dp.include_router(help.router)
    dp.include_router(echo.router)

    # Запускаем бота и пропускаем все накопленные входящие
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
