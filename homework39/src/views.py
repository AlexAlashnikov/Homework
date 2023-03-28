import aiohttp_jinja2

import db


@aiohttp_jinja2.template('index.html')
async def index(request):
    async with request.app['db'].acquire() as conn:
        cursor = await conn.execute(db.message.select())
        records = await cursor.fetchall()
        messages = [dict(m) for m in records]
        return {'messages': messages}
