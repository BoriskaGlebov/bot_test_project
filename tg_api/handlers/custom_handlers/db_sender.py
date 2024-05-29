import logging
import os
import sys

import requests
from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile

from config_data.logger_config import any_exeption
from database.models.models import User

from database.models.models import FilmsBase, Find_Film_Param
from tg_api.states.user_state import MovieSearch

logger = logging.getLogger(f'main.tg_api.handlers.custom_handlers.{os.path.basename(__file__)}')
sys.excepthook = any_exeption

router = Router()


@router.message(Command('db'))
async def db_sender(message: Message, state: FSMContext, bot: Bot):
    """Итория запросов по Боту"""
    logger.debug(f'{db_sender.__name__} - начало работы')
    await state.set_state(MovieSearch.choosing_db)
    user = message.from_user.username
    if user == 'BorisisTheBlade':
        # print(os.path.exists('films.db'))
        await message.answer('Сейчас отправлю БД')
        agenda = FSInputFile("films.db", filename="films.db")
        await bot.send_document(message.chat.id, document=agenda)
    await state.clear()

    logger.info(f'{db_sender.__name__} - отработала хорошо')
