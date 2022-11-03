from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/Время')
b2 = KeyboardButton('/Расположение')
b3 = KeyboardButton('/Меню')
b4 = KeyboardButton('Поделиться номером', request_contact=True)
b5 = KeyboardButton('Отправить где я', request_location=True)

# one_time_keyboard=True - скрывает клавиатуру после 1 тыка
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

#kb_client.row(b1, b2, b3) Всё в одну строку
kb_client.add(b1).insert(b2).add(b3).row(b4, b5)
