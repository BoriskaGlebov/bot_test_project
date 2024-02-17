import os
from dotenv import load_dotenv, find_dotenv
from pydantic import SecretStr, StrictStr
from pydantic_settings import BaseSettings

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()


class SiteSettings(BaseSettings):
    """Класс получения базовых настроек"""
    api_key: SecretStr = os.getenv('SITE_API')
    host_api: StrictStr = os.getenv('HOST_API')
    bot_key: SecretStr = os.getenv('BOT_TOKEN')


site_tg_settings = SiteSettings()
