import asyncio
import logging
from keyboards import start_keyboard, day_keyboard
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config import Settings
from aiogram.types import FSInputFile
from Table.Table import imeg

f = open('database/database.info', 'r', encoding="utf-8")
l = f.readline()
info = l.strip("\n").split(",")
f.close()

day =["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "↩ вернуться к выбору класса", "Вся неделя"]
colum = 0
all = [False,False]

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=Settings()["TOKEN"])
# Диспетчер
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Шаг 1.\n Для начала выберите класс.", reply_markup=start_keyboard())

@dp.message()
async def echo(message: types.Message):
    global colum, all
    msg = message.text.lower()
    for i in range(len(info)-1):
        if info[i].lower() == msg:
            colum = i
            await message.answer("Шаг 2.\n Теперь выберите день недели.", reply_markup=day_keyboard())
    for i in range(len(day)-2):
        if day[i].lower() == msg:
            await message.answer_photo(photo=FSInputFile(imeg(message.from_user.id, all, i, colum)))
            all = [False, False]
            await message.answer("Шаг 1.\n Для начала выберите класс.", reply_markup=start_keyboard())
    if info[-1].lower() == msg:
        all[0] = True
        await message.answer("Шаг 2.\n Теперь выберите день недели.", reply_markup=day_keyboard())
    elif day[-1].lower() == msg:
        all[1] = True
        await message.answer_photo(photo=FSInputFile(imeg(message.from_user.id, all, i, colum)))
        all = [False, False]
        await message.answer("Шаг 1.\n Для начала выберите класс.", reply_markup=start_keyboard())
    elif day[-2].lower() == msg:
        all = [False, False]
        await message.answer("Шаг 1.\n Для начала выберите класс.", reply_markup=start_keyboard())
    #print(msg)

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())