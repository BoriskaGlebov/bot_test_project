from urllib3.util import url


def photo_finder(num: int, user_id: int, out_message_dict: dict) -> url:
    """Поиск фото в списке результатов поиска"""
    print(out_message_dict[user_id][num]['poster'].get('previewUrl'))
    return out_message_dict[user_id][num]['poster'].get('previewUrl')


def caption(num: int, user_id: int, out_message_dict: dict) -> str:
    """Генерация описание картинки"""
    film_name = out_message_dict[user_id][num].get('name')
    alternative_name = out_message_dict[user_id][num].get('alternativeName')
    year = out_message_dict[user_id][num].get('year')
    genres = ','.join([el['name'] for el in out_message_dict[user_id][num].get('genres')])
    description = out_message_dict[user_id][num].get('description')
    rating = ', '.join(
        [f'{k}={round(v, 2)}' for k, v in out_message_dict[user_id][num].get('rating').items() if v is not None][0:2])
    series_length = out_message_dict[user_id][num].get('seriesLength')
    movie_length = out_message_dict[user_id][num].get('movieLength')
    if out_message_dict[user_id][num].get('isSeries'):
        photo_caption = (f'<b>{film_name}</b>\\<i>{alternative_name}</i>'
                         f'({year})\n'
                         f'<b>Жанры:</b> {genres}\n'
                         f'<b>Описание:</b> {description}\n'
                         f'<b>Рейтинг:</b>🏆{rating}\n'
                         f'Сериал\n'
                         f'Продолжительность серии: {series_length} минут')
        return photo_caption
    else:
        photo_caption = (f'<b>{film_name}</b>\\<i>{alternative_name}</i>'
                         f'({year})\n'
                         f'<b>Жанры:</b> {genres}\n'
                         f'<b>Описание:</b> {description}\n'
                         f'<b>Рейтинг:</b>🏆{rating}\n'
                         f'Фильм\n'
                         f'Продолжительность: {movie_length} минут')
        return photo_caption

