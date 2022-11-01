from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

TOKEN = "5732215283:AAEK4rDutfCc6OPsXZZPFGw0CEITWTV5UiE"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def command_start(message : types.message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита')
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему \n https://t.me/adsf1234bot')

async def work_hour_start(message : types.message):
    await message.reply("Работает")