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


class FilmsBase(peewee.Model):
    """Таблица для запроса поиска фильмов по названию"""
    created_at = peewee.DateTimeField(default=datetime.now().strftime('%Y-%m-%d %X'))
    user = peewee.ForeignKeyField(User, backref='query')
    query = peewee.TextField()
    internalNames = JSONField(null=True, json_dumps=my_json_dumps)
    name = peewee.TextField(null=True)
    alternativeName = peewee.TextField(null=True)
    enName = peewee.TextField(null=True)
    year = peewee.IntegerField(null=True)
    genres = JSONField(null=True, json_dumps=my_json_dumps)
    countries = JSONField(null=True, json_dumps=my_json_dumps)
    releaseYears = JSONField(null=True, json_dumps=my_json_dumps)
    film_id = peewee.IntegerField(null=True)
    names = JSONField(null=True, json_dumps=my_json_dumps)
    type = peewee.TextField(null=True)
    description = peewee.TextField(null=True)
    shortDescription = peewee.TextField(null=True)
    logo = JSONField(null=True, json_dumps=my_json_dumps)
    poster = JSONField(null=True, json_dumps=my_json_dumps)
    backdrop = JSONField(null=True, json_dumps=my_json_dumps)
    rating = JSONField(null=True, json_dumps=my_json_dumps)
    votes = JSONField(null=True, json_dumps=my_json_dumps)
    movieLength = peewee.IntegerField(null=True)
    isSeries = peewee.IntegerField(null=True)
    ticketsOnSale = peewee.IntegerField(null=True)
    totalSeriesLength = peewee.TextField(null=True)
    seriesLength = peewee.TextField(null=True)
    ratingMpaa = peewee.TextField(null=True)
    ageRating = peewee.TextField(null=True)
    top10 = peewee.TextField(null=True)
    top250 = peewee.TextField(null=True)
    typeNumber = peewee.IntegerField(null=True)
    status = peewee.TextField(null=True)
    internalRating = JSONField(null=True, json_dumps=my_json_dumps)
    internalVotes = peewee.IntegerField(null=True)
    externalId = JSONField(null=True, json_dumps=my_json_dumps)

    class Meta:
        database = db


db.connect()
db.create_tables([User, FilmsBase])
