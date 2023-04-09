from sqlalchemy import create_engine, MetaData

from src.settings import config
from src.db import message


DSN = "postgresql://{user}:{password}@{host}:{port}/{database}"

def create_table(engine):
    meta = MetaData()
    meta.create_all(bind=engine, tables=[message])

def sample_data(engine):
    conn = engine.connect()
    conn.execute(message.insert(), [
        {'message_text': 'How are you'}
    ])
    conn.close()

if __name__ == '__main__':
    db_url = DSN.format(**config['postgres'])
    engine = create_engine(db_url)
    create_table(engine)
    sample_data(engine)
