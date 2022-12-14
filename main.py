from aiogram.utils import executor
from config import dp
from handlers import client, admin, other
from database import sqlite_db


async def on_start_up(_):
    print('Bot online')
    sqlite_db.sql_start()


client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_start_up)
