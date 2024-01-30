from aiogram import Bot
from config_data.comfig import site_tg_settings

bot_init = Bot(token=site_tg_settings.bot_key.get_secret_value(),
               parse_mode='HTML')
