import functools
from datetime import datetime
import peewee
from playhouse.sqlite_ext import *

db = peewee.SqliteDatabase('films.db')
# Для отключения экранирования в таблицах
my_json_dumps = functools.partial(json.dumps, ensure_ascii=False)


class ModelBase(peewee.Model):
    """Модель базы данных"""
    created_at = peewee.DateTimeField(default=datetime.now().
                                      strftime('%Y-%m-%d %X'))

    class Meta:
        database = db


class User(peewee.Model):
    """Модель таблицы с пользователями"""
    created_at = peewee.DateTimeField(default=datetime.now().
                                      strftime('%Y-%m-%d %X'))
    user_id = peewee.IntegerField()
    user_name = peewee.TextField(null=True)

    class Meta:
        database = db


db.connect()
db.create_tables([User])
if __name__ == '__main__':
    print('nem')
