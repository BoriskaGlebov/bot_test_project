from datetime import datetime
from typing import TypeVar, List, Dict
from database.models.models import db

T = TypeVar('T')


def _insert_single_user(model: T, user_id: int, user_name: str = 'Guest_User') -> None:
    """Добавление пользователя в БД
    :param model: название таблицы
    :param user_id: id пользователя
    :param user_name: имя пользователя если оно есть"""
    cr_time = datetime.now().strftime('%Y-%m-%d %X')
    if len(model.select().where(model.user_id == user_id)):
        print('Такой пользователь уже в БД')
    else:
        model.create(created_at=cr_time, user_id=user_id, user_name=user_name)
        print(f'Добавил {user_name}')


def _insert_data(database: db, model: T, data: List[Dict]) -> None:
    """Вставка всех элементов в базу данных"""
    with database.atomic():
        model.insert_many(data).execute()
    print('Данные добавлены в таблицу')


def _retrieve_elem(database: db, user_id: int, model_film: T, model_user: T) -> list[dict]:
    """Извлечение в список последних фильмов которые пользователь спрашивал"""
    last_query_time = model_film.select(model_film, model_user).join(model_user).where(
        model_user.user_id == user_id).order_by(-model_film.created_at).limit(1)[0].created_at
    with (database.atomic()):
        response = model_film.select(model_film, model_user).join(model_user).where(
            model_user.user_id == user_id, model_film.created_at == last_query_time).dicts()
    return response


class CRUDInterface:
    """Создание,чтение,обновление,удаление данных в БД"""

    @classmethod
    def insert_single_user(cls):
        """Добавление пользователя в БД"""
        return _insert_single_user

    @classmethod
    def insert_data(cls):
        """Вставка всех элементов в базу данных"""
        return _insert_data

    @classmethod
    def retrieve_elem(cls):
        """Извлечение в список последних пять элементов поиска фильма в БД"""
        return _retrieve_elem
