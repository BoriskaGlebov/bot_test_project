from aiogram.fsm.state import StatesGroup, State


class MovieSearch(StatesGroup):
    choosing_film_name = State()
    changing_films = State()
