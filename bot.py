import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command

TOKEN = "7556829484:AAESxC6eNoq5sdAF8MCIyUN3iC2S3QDlheE"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Привет🤗 меня зовут Мирослава Чиж.\n\nСейчас я тебе покажу как ты можешь создать постоянный входящий поток партнеров в свой бизнес.\n\n\nБлагодаря своей системе "ТУРБО-ПРОКАЧКА СОЦСЕТЕЙ" и 1 мощному инструменту я ежедневно получаю от 3-5 входящих заявок в бизнес. За несколько месяцев заработала 370тыс  на партнерских программах.\n\n\nСейчас я покажу как ты сможешь выйти на доход от 30тыс уже в первый месяц благодаря системе 👇👇👇\n\n\n✅"ТУРБО-ПРОКАЧКА СОЦСЕТЕЙ". Пошаговое обучение по запуску соцсетей в инстаграм,вконтакте,телеграм, ютуб.\n\n✅Чат- Бот рекрутер ,который будет работать 24/7 \n\n\nСЕЙЧАС ПОКАЖУ👇👇👇")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
