import json
import string

from config import types
from aiogram import Dispatcher


# @dp.message_handler() - ловит всё
# чтобы цензор работал в чатах - сделай бота админом!
async def censor_send(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')} \
            .intersection(set(json.load(open('cenz.json')))):
        await message.reply("Мат запрещён!")
        await message.delete()


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(censor_send)
