from typing import Dict, Any, Union, Callable, List, AnyStr
from requests import get
from site_api.settings.site_settings import headers_dict, status_code
from site_api.utils.common_func import column_names


# @column_names
def _find_film(query_str: str, headers: Dict = headers_dict,
              timeout: Any = 3, limit_page: int = 20, ) -> Union[List[Dict], AnyStr]:
    """
    Поиск фильма по названию и возвращает ответ в формате списка словарей с фильмами,
    так же может вернуть ключи словаря с типом данных пригодным для
    подготовки таблицы в БД
    :param query_str: название фильма
    :param headers: параметры авторизации
    :param timeout: прерывание запроса через секунд
    :param limit_page: количество выводимых фильмов
    :return: response: ответ с сайта в формате json или код ошибки
    """
    url = 'https://api.kinopoisk.dev/v1.4/movie/search?'
    param = {'page': 1, 'limit': limit_page, 'query': query_str}
    response = get(url, params=param, headers=headers, timeout=timeout)
    if response.status_code == 200:
        print(status_code.get(response.status_code))
        return response.json()['docs']
    else:
        return (f'Что-то пошло не так! '
                f'Код = {response.status_code} = {status_code.get(response.status_code)}')


class SiteApiInterface:
    """
    def film_finder: Ищет фильм по названию и записывает в словарь json\n
    """

    @classmethod
    def film_finder(cls) -> Callable:
        """Ищет фильм по названию и записывает в словарь json"""
        return _find_film


if __name__ == '__main__':
    print('site_api')
