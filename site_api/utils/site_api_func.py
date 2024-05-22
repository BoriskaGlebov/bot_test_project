from typing import Dict, Any, Union, Callable, List, AnyStr
from requests import get
from site_api.settings.site_settings import headers_dict, status_code
from site_api.utils.common_func import column_names


# @column_names
def _find_film(query_str: str, timeout: Any = 3, limit_page: int = 20, ) -> Union[List[Dict], AnyStr]:
    """
    Поиск фильма по названию и возвращает ответ в формате списка словарей с фильмами,
    так же может вернуть ключи словаря с типом данных пригодным для
    подготовки таблицы в БД
    :param query_str: название фильма
    :param timeout: прерывание запроса через секунд
    :param limit_page: количество выводимых фильмов
    :return: response: ответ с сайта в формате json или код ошибки
    """
    url = 'https://api.kinopoisk.dev/v1.4/movie/search?'
    param = {'page': 1, 'limit': limit_page, 'query': query_str}
    response = get(url, params=param, headers=headers_dict, timeout=timeout)
    if response.status_code == 200:
        print(status_code.get(response.status_code))
        return response.json()['docs']
    else:
        return (f'Что-то пошло не так! '
                f'Код = {response.status_code} = {status_code.get(response.status_code)}')


# @column_names
def _find_100_film(timeout: Any = 5, limit_page: int = 100, ) -> Union[Dict, str]:
    """Поиск топ 100 фильмов Кинопоиска"""
    url = 'https://api.kinopoisk.dev/v1.4/movie?'
    param = {'page': 1, 'limit': limit_page,
             'selectFields': ['id', 'name', 'alternativeName', 'year', 'genres', 'description',
                              'rating', 'movieLength', 'poster', 'videos', 'networks', ],
             'notNullFields': 'id',
             'sortField': 'rating.kp', 'sortType': '-1', 'lists': 'top250'}
    response = get(url, params=param, headers=headers_dict, timeout=timeout)
    if response.status_code == 200:
        print(status_code.get(response.status_code))
        return response.json()['docs']
    else:
        return (f'Что-то пошло не так! '
                f'Код = {response.status_code} = {status_code.get(response.status_code)}')


# @column_names
def _find_film_param(film_types: str | None = None, years: str | None = None,
                     rating_kp: str | None = None, genres: str | None = None,
                     countries: str | None = None,
                     limit_page: int = 20,
                     timeout: Any = 10, ) -> Union[Dict, str]:
    """Поиск фильмов и сериалов по параметрам Кинопоиска
        :param film_types-movie,tv-series,cartoon,animated-series,anime или !anime
        :param years-1874, 2050, !2020, 2020-2024
        :param rating_kp-7, 10, 7.2-10
        :param genres-"драма", "комедия", "!мелодрама", "+ужасы"
        :param countries-"США", "Россия", "!Франция" , "+Великобритания"

    """
    url = 'https://api.kinopoisk.dev/v1.4/movie?'
    param = {'page': '1', 'limit': limit_page, 'selectFields': '',
             'notNullFields': ['id', 'name', 'alternativeName', 'description', 'type', 'year',]}
    keys = ['type', 'year', 'rating.kp', 'genres.name', 'countries.name']
    values = [film_types, years, rating_kp, genres, countries]
    param_user = {keys[num]: el for num, el in enumerate(values) if el is not None}
    param.update(param_user)
    response = get(url, params=param, headers=headers_dict, timeout=timeout)
    if response.status_code == 200:
        print(status_code.get(response.status_code))
        return response.json()['docs']
    else:
        return (f'Что-то пошло не так! '
                f'Код = {response.status_code} = {status_code.get(response.status_code)}')


class SiteApiInterface:
    """
    Интерфейс поиска фильмов
    """

    @classmethod
    def film_finder(cls) -> Callable:
        """Ищет фильм по названию и записывает в словарь json"""
        return _find_film

    @classmethod
    def top_100_film(cls):
        """Поиск топ 100 фильмов Кинопоиска"""
        return _find_100_film

    @classmethod
    def find_film_param(cls):
        """
        Поиск фильмов и сериалов по параметрам Кинопоиска
        fields-можно оставить пустым, это какие поля не должны быть пустыми
        film_types-movie,tv-series,cartoon,animated-series,anime или !anime
        years-1874, 2050, !2020, 2020-2024
        rating_kp-7, 10, 7.2-10
        genres-"драма", "комедия", "!мелодрама", "+ужасы"
        countries-"США", "Россия", "!Франция" , "+Великобритания"
        """
        return _find_film_param


if __name__ == '__main__':
    res = _find_film_param()
    print(res)