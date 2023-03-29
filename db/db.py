from peewee import *
from playhouse.postgres_ext import ArrayField

tiktok_db = PostgresqlDatabase(database='tiktok', user='postgres', password='password', host='localhost', port='5432')


class BaseModel(Model):
    class Meta:
        database = tiktok_db


class VideoEntity(BaseModel):
    url = TextField()
    duration = IntegerField()  # секунды

    class Meta:
        db_table = "video"


class PublicationEntity(BaseModel):
    publication_id = TextField()
    publication_url = TextField()
    author_unique_id = TextField()
    desc = TextField()
    like_count = IntegerField()
    comment_count = IntegerField()
    view_count = IntegerField()
    share_count = IntegerField()
    hashtags = ArrayField(TextField, index=False)
    category = IntegerField(null=True)
    created_at = BigIntegerField(null=True)
    video = ForeignKeyField(VideoEntity, backref="publication", unique=True)

    class Meta:
        db_table = "publication"


class AuthorEntity(BaseModel):
    author_id = TextField()
    last_publication_id = TextField()
    category = IntegerField()
    is_working = BooleanField()
    is_deleted = BooleanField()

    class Meta:
        db_table = "author"


def init():
    VideoEntity.create_table()
    PublicationEntity.create_table()
    AuthorEntity.create_table()
