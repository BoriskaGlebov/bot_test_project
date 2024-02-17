from aiogram import Bot
from config_data.config import site_tg_settings

bot_init = Bot(token=site_tg_settings.bot_key.get_secret_value(), parse_mode='HTML')
# from telebot import TeleBot
# from telebot.storage import StateMemoryStorage
# from config_data import config
#
# storage = StateMemoryStorage()
# bot = TeleBot(token=config.BOT_TOKEN, state_storage=storage)

# Не разобрался для чего он
# Сюда кажется состояния FSM Писать
# class Start_command(StatesGroup):или в states
