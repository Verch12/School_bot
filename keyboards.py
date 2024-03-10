from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types

def start_keyboard():
    f = open('database/database.info', 'r', encoding="utf-8")
    l = f.readline()
    info = l.strip("\n").split(",")
    f.close()

    # types.KeyboardButton(text="")
    kb = []
    for i in range(len(info)): kb.append([types.KeyboardButton(text=info[i],callback_data = i)])

    # Инициализация клавиатуры с кнопками
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard

def day_keyboard():
    kb = [[types.KeyboardButton(text="Понедельник",callback_data = 0)], [types.KeyboardButton(text="Вторник",callback_data = 1)], [types.KeyboardButton(text="Среда",callback_data = 2)], [types.KeyboardButton(text="Четверг",callback_data = 3)], [types.KeyboardButton(text="Пятница",callback_data = 4)], [types.KeyboardButton(text="Вся неделя",callback_data = 5)]]
    kb.append([KeyboardButton(text="↩ Вернуться к выбору класса")])
    # Инициализация клавиатуры с кнопками
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard

#def start_keyboard():
#    kb = [[types.KeyboardButton(text="📅 Посмотреть расписание")]]
#    # Инициализация клавиатуры с кнопками
#    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
#    return keyboard
