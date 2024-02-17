from aiogram import Router, F
from aiogram.filters import Command

from tg_api.states.user_state import MovieSearch
from tg_api.handlers.custom_handlers.common_func import *

from database.models.models import db, Top100Films


router = Router()
user_data = {}
dict_with_films = {}


@router.message(F.text == 'Топ 100 🎥 Кинопоиска')
@router.message(Command('top_100'))
async def finder_film(message: Message, state: FSMContext):
    """Действие по нажатии кнопки топ 100 фильмов, отображение новых кнопок"""
    await state.set_state(MovieSearch.choosing_top_100)
    user_inf = message.from_user
    await message.answer('🤖 Уже через секунду покажу эти фильмы', reply_markup=ReplyKeyboardRemove())
    await rez_finder(message, state, MovieSearch.changing_films_top_100, Top100Films)


@router.callback_query(MovieSearch.changing_films_top_100, F.data.startswith("num_"))
async def callbacks_films(callback: CallbackQuery, state: FSMContext):
    await callbacks_num(callback, state, MovieSearch.changing_films_top_100)
