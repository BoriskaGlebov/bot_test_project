from aiogram import Bot
from aiogram.types import BotCommand

main_menu_commands = [
    BotCommand(command='/start',
               description='Запуск бота'),
    BotCommand(command='/find_film',
               description='Поиск 🎥 по названию'),
    BotCommand(command='/find_param',
               description='Подбор 🎥 по параметрам'),
    BotCommand(command='/top_100',
               description='Топ 100 🎥 Кинопоиска'),
    BotCommand(command='/history',
               description='📜История запросов'),
    BotCommand(command='/help',
               description='Справка по работе бота')
]


async def set_main_menu(bot: Bot):
    """Создаем список с командами и их описанием для кнопки menu"""
    await bot.set_my_commands(main_menu_commands)
