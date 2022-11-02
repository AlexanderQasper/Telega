from config import *
from aiogram import Dispatcher
from keyboards import kb_client

# Если всё в одном файле, то через декоратор можно отлавливать команды
# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.message):
    try:
        await bot.send_message(message.from_user.id, 'Рад тебя видеть!', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему \n https://t.me/adsf1234bot')


# @dp.message_handler(commands=['Расположение'])
async def place(message: types.message):
    await message.reply("Батуми, Батумский бульвар, дом 13")


# @dp.message_handler(commands=['Время'])
async def work_hour(message: types.message):
    await message.reply("Пн.8-12 \n Вт. 8-13 \n Ср. 9-16 \n Чт. 10-14 \n Пт. 12-18")

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands = ['start', 'help'])
    dp.register_message_handler(place, commands=['Расположение'] )
    dp.register_message_handler(work_hour, commands=['Время'])