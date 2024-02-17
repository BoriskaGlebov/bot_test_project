from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from tg_api.utils.set_bot_commands import main_menu_commands

router = Router()


@router.message(Command('help'))
async def help_cmd(message: Message):
    """Кнопка помощи"""
    text = [f'{el.command} - {el.description}' for el in main_menu_commands]
    await message.answer(text='\n'.join(text), reply_markup=ReplyKeyboardRemove())
