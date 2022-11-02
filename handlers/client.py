import json
import string

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

TOKEN = "5732215283:AAEK4rDutfCc6OPsXZZPFGw0CEITWTV5UiE"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.message):
    try:
        await bot.send_message(message.from_user.id, 'Рад тебя видеть! Напиши /command, чтобы посмотреть возможности')
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему \n https://t.me/adsf1234bot')


@dp.message_handler(commands=['Расположение'])
async def place(message: types.message):
    await message.reply("Батуми, Батумский бульвар, дом 13")


@dp.message_handler(commands=['Время'])
async def work_hour_start(message: types.message):
    await message.reply("Пн.8-12 \n Вт. 8-13 \n Ср. 9-16 \n Чт. 10-14 \n Пт. 12-18")
