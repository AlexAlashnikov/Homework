from peewee import *

db = SqliteDatabase('chinook.db')

class BaseModel(Model):
    class Meta:
        database = db

class Album(BaseModel):
    """Определение таблицы albums в базе данных"""
    albums_id = PrimaryKeyField(column_name='Albumid')
    name = TextField(column_name='Title')
    class Meta:
        table_name = 'albums'

class Track(BaseModel):
    """Определение таблицы tracks в базе данных"""
    track_id = PrimaryKeyField(column_name='Albumid')
    name = TextField(column_name='Name')
    class Meta:
        table_name = 'tracks'

def search():
    """Поиск треков в базе данных по названию альбома"""
    album_input = input("Enter album name: ")
    query = (Track.select()
            .where(Track.track_id == (Album.select().where(Album.name == album_input)))
            .order_by(Track.name.asc()))
    for tracks in query:
        print(f"\tTrack: {tracks.name}")

search()

db.close()