# Модуль получает токены бота и API Kinopoisk из файла .env
import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()


class SiteSettings:
    """Класс получения базовых настроек"""
    api_key = os.getenv('SITE_API')
    host_api = os.getenv('HOST_API')
    bot_key = os.getenv('BOT_TOKEN')
    directory = os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir))


site_tg_settings = SiteSettings()
if __name__ == '__main__':
    print(site_tg_settings.directory)
