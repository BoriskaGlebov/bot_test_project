from contextlib import suppress

from aiogram import Router, F
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, InputMediaPhoto, CallbackQuery

from requests import ReadTimeout

from tg_api.keyboards.reply.keybord_find_film import get_bot_function_find_film
from tg_api.states.user_state import MovieSearch
from tg_api.handlers.custom_handlers.common_func import photo_finder, caption
from tg_api.keyboards.inline.some_inline_kb import change_films_kb

from site_api.core import def_find_film

from database.utilits.common_func import create_list_for_find_film
from database.models.models import User, FilmsBase, db
from database.core import def_insert_data, def_get_elem

router = Router()
user_data = {}
dict_with_films = {}


@router.message(F.text == 'Поиск 🎥 по названию')
@router.message(Command('find_film'))
async def finder_film(message: Message, state: FSMContext):
    """Действие по нажатии кнопки поиск фильмов, отображение новых кнопок"""
    await message.answer('🏆Введите название фильма?', reply_markup=get_bot_function_find_film())
    await state.set_state(MovieSearch.choosing_film_name)


@router.message(MovieSearch.choosing_film_name, F.text)
async def rez_finder(message: Message, state: FSMContext):
    """Поиск фильмов по названию и вывод результата в виде картинки с описанием и кнопками листания"""
    user_inf = message.from_user
    try:
        response_list = def_find_film(message.text, limit_page=30)
        if isinstance(response_list, list) and len(response_list):
            out_list = create_list_for_find_film(User.get(User.user_id == user_inf.id), response_list, message.text)
            def_insert_data(db, FilmsBase, out_list)
            if user_inf.id in dict_with_films:
                del dict_with_films[user_inf.id]
            if user_inf.id in user_data:
                del user_data[user_inf.id]
            dict_with_films[user_inf.id] = def_get_elem(db, user_inf.id, FilmsBase, User)
            await message.answer_photo(
                photo=photo_finder(num=0, user_id=user_inf.id, out_message_dict=dict_with_films),
                caption=caption(num=0, user_id=user_inf.id, out_message_dict=dict_with_films),
                reply_markup=change_films_kb(num=0, all_num=len(dict_with_films[user_inf.id])))
            await state.set_state(MovieSearch.changing_films)
        elif isinstance(response_list, list):
            await message.answer('А я не знаю такой фильм 🤖')
        else:
            print(response_list)
            await message.answer('Что то пошло не так ! Буду разбираться', reply_markup=ReplyKeyboardRemove())
            await message.answer_sticker('CAACAgIAAxkBAAELUIxlv4FmGKw0Z7rVlCfWSo1gTA_n1wACWQADJxRJC-OPDSX1raG1NAQ')
            await state.clear()
    except ReadTimeout as exs:
        print(f'{exs} - сайт не отвечает')

        await message.answer('Упсссс...Сервер не отвечает', reply_markup=ReplyKeyboardRemove())
        await message.answer_sticker('CAACAgIAAxkBAAELUIxlv4FmGKw0Z7rVlCfWSo1gTA_n1wACWQADJxRJC-OPDSX1raG1NAQ')


async def update_num_text(message: Message, new_value: int, user_id):
    """Обновление описания картинки"""
    with suppress(TelegramBadRequest):
        photo = InputMediaPhoto(
            media=photo_finder(num=new_value, user_id=user_id, out_message_dict=dict_with_films),
            caption=caption(num=new_value, user_id=user_id, out_message_dict=dict_with_films))
        await message.edit_media(
            media=photo,
            reply_markup=change_films_kb(num=new_value, all_num=len(dict_with_films[user_id]))
        )


@router.callback_query(MovieSearch.changing_films, F.data.startswith("num_"))
async def callbacks_num(callback: CallbackQuery, state: FSMContext):
    """Кнопки колбэки"""
    user_value = user_data.get(callback.from_user.id, 0)
    action = callback.data.split("_")[1]

    if action == "incr":
        user_data[callback.from_user.id] = (user_value + 1) % len(dict_with_films[callback.from_user.id])
        await update_num_text(callback.message, (user_value + 1) % len(dict_with_films[callback.from_user.id]),
                              callback.from_user.id)
    elif action == "decr":
        user_data[callback.from_user.id] = (user_value - 1) % len(dict_with_films[callback.from_user.id])
        await update_num_text(callback.message, (user_value - 1) % len(dict_with_films[callback.from_user.id]),
                              callback.from_user.id)
    await callback.answer(' ')
    await state.set_state(MovieSearch.changing_films)


@router.message(MovieSearch.changing_films, F.text)
async def change_state(message: Message, state: FSMContext):
    """Поиск фильма без команды поиска"""
    await state.set_state(MovieSearch.choosing_film_name)
    await rez_finder(message, state)
