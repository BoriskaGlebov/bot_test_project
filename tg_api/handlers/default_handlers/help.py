from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from tg_api.utils.set_bot_commands import main_menu_commands

router = Router()


@router.message(Command('help'))
async def help_cmd(message: Message):
    """Действия по команде /help"""
    text = [f'{el.command} - {el.description}' for el in main_menu_commands]
    # await asyncio.sleep(1.5)
    # await message.delete()
    await message.answer(text='\n'.join(text))
