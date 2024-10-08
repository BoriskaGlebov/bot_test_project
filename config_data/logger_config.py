# Словарь настройки логирования проекта
import logging
import os
from logging import config
from config_data.config import site_tg_settings
from logging import FileHandler
from logging.handlers import TimedRotatingFileHandler
import sys
import string

# from database.models.models import default_path

# default_path = os.path.dirname(os.path.abspath(__file__)).split('bot')[0] + 'bot/app/'

default_path=os.path.join(site_tg_settings.directory,'logger')
if not os.path.isdir(default_path):
    os.mkdir(default_path)

# print(default_path)
def any_exeption(type, values, traceback_info):
    """
    Функция логгирования неожиданных исключений
    :param type:
    :param values:
    :param traceback_info:
    :return:
    """
    logger = logging.getLogger('main')
    logging.config.dictConfig(dict_config)
    logger.error(f'some error {type} {values} {traceback_info}', exc_info=(type, values, traceback_info))


dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "%(asctime)s | %(levelname)s | %(name)s | line %(lineno)d | %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "base"

        },
        "file": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "base",
            "filename": f'{default_path}/logger.log',
            "mode": "a",
            "encoding": "utf-8",
        },

    },
    "loggers": {
        "main": {
            "level": "INFO",
            "handlers": ["file", "console"],
        },



    },
    # "filters": {
    #     "my_filter": {
    #         "()": SelfFilter,
    #     }
    # },
    # "root":{},
}