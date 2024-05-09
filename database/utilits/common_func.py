from typing import TypeVar
from typing import Union, List, Dict
from datetime import datetime

T = TypeVar('T')


def create_list_for_find_film(user_inst: T | None, film_response: Union[List[Dict]], query: str | None) -> List[Dict]:
    """
    Делаю окончательный словарь для добавления в таблицу с фильмам
    :param user_inst: Данные пользователя
    :param film_response: ответ с запроса
    :param query: сам запрос
    :return: словарь для добавления в БД
    """
    out_list = []
    for num, elem in enumerate(film_response):
        if elem['name'] and elem['description'] and elem['poster']['previewUrl']:
            elem['created_at'] = datetime.now().strftime('%Y-%m-%d %X')
            elem['film_id'] = elem.pop('id')
            if query is not None and user_inst is not None:
                elem['query'] = query
                elem['user'] = user_inst
            out_list.append(elem)
    return out_list
