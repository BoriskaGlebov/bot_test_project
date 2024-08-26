import asyncio
import logging
import sys
from logging import config
from config_data.logger_config import *
import os.path
from database.models.models import default_path
from aiogram import Dispatcher
from aiogram import Bot
from config_data.config import site_tg_settings

from tg_api.utils.set_bot_commands import set_main_menu, set_discription
from tg_api.handlers.default_handlers import start, help, echo
from tg_api.handlers.custom_handlers import top_100_films, find_film_param, history, find_film, db_sender

# from tg_api.handlers.custom_handlers import find_film, top_100_films, find_film_param, history, some

logger = logging.getLogger('main.' + str(os.path.relpath(__file__)))
logging.config.dictConfig(dict_config)  # отключить после проведения тестов
sys.excepthook = any_exeption
import shutil

# инициализация бота
bot_init = Bot(token=site_tg_settings.bot_key, parse_mode='HTML')


async def copy(i):
    if not os.path.isdir(site_tg_settings.directory + '/app'):
        os.mkdir(site_tg_settings.directory + '/app')
    db = os.path.join(site_tg_settings.directory, 'db', 'films.db')
    dist = os.path.join(site_tg_settings.directory, 'app')
    shutil.copy2(db, dist)
    print('копировал')
    # shutil.copy(os.path.join(site_tg_settings.directory, 'db','films.db'),
    #             os.path.join(site_tg_settings.directory, app))
    await asyncio.sleep(i)


async def main():
    """
    Функцця запускает работу бота
    :return:
    """
    logger.debug(f'{main.__name__} - начинает работу')
    await copy(1)
    bot = bot_init
    dp = Dispatcher()

    await set_discription(bot)
    logger.debug(f'{main.__name__} - Загрузил кнопки меню и описание бота')
    #

    dp.include_router(start.router)
    dp.include_router(top_100_films.router)
    dp.include_router(find_film_param.router)
    dp.include_router(history.router)
    dp.include_router(find_film.router)
    dp.include_router(help.router)
    dp.include_router(db_sender.router)
    dp.include_router(echo.router)

    # Запускаем бота и пропускаем все накопленные входящие
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
    print('test')
