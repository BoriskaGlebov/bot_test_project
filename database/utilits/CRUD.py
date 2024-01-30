from datetime import datetime
from typing import TypeVar
# from typing import Union

T = TypeVar('T')


def _insert_single_user(model: T, user_id: int, user_name: str) -> None:
    """Добавление пользователя в БД"""
    cr_time = datetime.now().strftime('%Y-%m-%d %X')
    if len(model.select().where(model.user_id == user_id)):
        print('Такой пользователь уже в БД')
    else:
        model.create(created_at=cr_time, user_id=user_id, user_name=user_name)
        print(f'Добавил {user_name}')


class CRUDInterface:

    @classmethod
    def insert_single_user(cls):
        """Добавление пользователя в БД"""
        return _insert_single_user


if __name__ == "__main__":
    print('БД>')
