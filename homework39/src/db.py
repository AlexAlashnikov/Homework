import datetime

from sqlalchemy import Table, MetaData, String, Time, Column, Integer
import aiopg.sa


meta = MetaData()
now = datetime.datetime.now()

message = Table(
    'message', meta,

    Column('id', Integer, primary_key=True),
    Column('message_text', String(255), nullable=False),
    Column('time', Time, default=now.strftime("%H:%M:%S"))
)

async def pg_context(app):
    conf = app['config']['postgres']
    engine = await aiopg.sa.create_engine(
                            database=conf['database'],
                            user=conf['user'],
                            password=conf['password'],
                            host=conf['host'],
                            port=conf['port'],
                            minsize=conf['minsize'],
                            maxsize=conf['maxsize'],
    )
    app['db'] = engine

    yield
    app['db'].close()
    await app['db'].wait_closed()
