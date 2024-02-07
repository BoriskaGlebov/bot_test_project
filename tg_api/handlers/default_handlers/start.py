from aiogram import Router, Bot, F
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, ReplyKeyboardRemove
from tg_api.keybords.reply.keybord_start import start_kb
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from database.core import def_insert_user, User

router = Router()


@router.message(Command('start'))
async def start_cmd(message: Message, bot: Bot, state: FSMContext):
    """Действия бота по команде start"""
    user = message.from_user
    me = await bot.get_me()
    mes = message
    await state.clear()
    # await bot.delete_message(chat_id=mes.chat.id, message_id=mes.message_id,)
    # await asyncio.sleep(1.5)
    # await message.delete()
    await message.answer(f'Привет <b>{user.username}</b>!!!\n'
                         f'Меня зовут <b>{me.first_name}</b> и я могу отлично '
                         f'помочь с поиском фильмов на вечер.🎫',
                         reply_markup=start_kb())
    await message.answer_sticker(
        sticker='CAACAgIAAxkBAAELLfVlpBnLljNASTHd5o59TtC0zuC-'
                'sAACXQEAAooSqg7e1UbQcaOvXjQE')
    def_insert_user(User, user.id, user.username)


# Нетрудно догадаться, что следующие два хэндлера можно
# спокойно объединить в один, но для полноты картины оставим так

# default_state - это то же самое, что и StateFilter(None)
@router.message(StateFilter(None), Command(commands=["cancel"]))
@router.message(default_state, F.text.lower() == "отмена")
async def cmd_cancel_no_state(message: Message, state: FSMContext):
    # Стейт сбрасывать не нужно, удалим только данные
    await state.set_data({})
    await message.answer(
        text="Нечего отменять",
        reply_markup=ReplyKeyboardRemove()
    )


@router.message(Command(commands=["cancel"]))
@router.message(F.text.lower() == "отмена" or
                F.text.lower() == "галя , у нас отмена")
@router.message(F.text.lower() == "галя , у нас отмена")
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="Действие отменено",
        reply_markup=start_kb()
    )
