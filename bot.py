from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = "7556829484:AAESxC6eNoq5sdAF8MCIyUN3iC2S3QDlheE"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Привіт! Я вічний безкоштовний бот.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
