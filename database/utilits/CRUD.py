from datetime import datetime, timedelta

from typing import TypeVar, List, Dict

from peewee import SqliteDatabase

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


def _insert_data(database: SqliteDatabase, model: T, data: List[Dict]) -> None:
    """Вставка всех элементов в базу данных"""
    with database.atomic():
        model.insert_many(data).execute()
    print('Данные добавлены в таблицу')


def _retrieve_elem(database: SqliteDatabase, user_id: int, model_film: T, model_user: T | None) -> list[dict]:
    """Извлечение в список последних фильмов которые пользователь спрашивал"""
    if user_id is not None and model_user is not None:
        last_query_time = model_film.select(model_film, model_user).join(model_user).where(
            model_user.user_id == user_id).order_by(-model_film.created_at).limit(1)[0].created_at
        with (database.atomic()):
            response = model_film.select(model_film, model_user).join(model_user).where(
                model_user.user_id == user_id, model_film.created_at == last_query_time).dicts()
    else:
        with (database.atomic()):
            response = model_film.select().dicts()
    return response


def _del_instance(database: SqliteDatabase, user_id: int | None, model_film: T, model_user: T | None):
    """Удаляет элементы в таблице если прошло больше какого-то времени"""
    with database.atomic():
        if user_id is None:
            res = model_film.select().where(model_film.created_at < datetime.now() - timedelta(minutes=15))
            for el in res:
                el.delete_instance()
        else:
            res = model_film.select().join(model_user).where(model_user.user_id == user_id,
                                                             model_film.created_at < datetime.now() - timedelta(
                                                                 minutes=15))
            print(res)
            for el in res:
                el.delete_instance()
    return res


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
        """Извлечение в список последних элементов поиска фильма в БД пользователем"""
        return _retrieve_elem

    @classmethod
    def del_olf_el(cls):
        """Удаление старых элементов в БД после определенного времени"""
        return _del_instance


if __name__ == '__main__':
    print('test')
