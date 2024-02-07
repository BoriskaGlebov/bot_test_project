from config_data.comfig import site_tg_settings

headers_dict: dict = {
    "accept": site_tg_settings.host_api,
    "X-API-KEY": site_tg_settings.api_key.get_secret_value()
}

status_code: dict = {200: 'Все хорошо',
                     401: 'Отсутствуют заголовки авторизации',
                     403: 'Запрещенный запрос',
                     404: 'Ничего не нашел',
                     'Default': 'Другие проблемы'}
