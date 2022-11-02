import json
import string

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

TOKEN = "5732215283:AAEK4rDutfCc6OPsXZZPFGw0CEITWTV5UiE"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def on_start_up(_):
    print('Bot online')



@dp.message_handler()
# чтобы цензор работал в чатах - сделай бота админом!
async def censor_send(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')} \
            .intersection(set(json.load(open('cenz.json')))):
        await message.reply("Мат запрещён!")
        await message.delete()


executor.start_polling(dp, skip_updates=True, on_startup=on_start_up)
