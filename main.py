import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from yt_dlp import YoutubeDL
# import importlib

API_TOKEN = "BOT TOKEN"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# configurate yt-dlp options
ydl_ops = {
    "format" : "best",
    "outtmpl" : "downloads/%(title)s.%(ext)s",
}

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.reply(
        "Assalomu aleykum \n Botga instagram link yuboring bot uni sizga ko`chirib beradi!"
    )

# handle instagram link
@dp.message_handler(lambda message : "instagram.com" in message.text)
async def dowland_video(message: types.Message):
    url = message.text

    try:

        await message.answer(
            "⏳ biz sizni kontentinggizni tayyorlaypmiz, iltimos kuting..."
        )

        with YoutubeDL(ydl_ops) as ydl:
            result = ydl.extract_info(url, download=True)
            file_name = ydl.prepare_filename(result)
        if file_name.endswith(".mp3"):
            await message.answer_video(open(file_name, "rb"))
        elif file_name.endswith(".jpg") or file_name.endswith(".png"):
            await message.answer_photo(open(file_name, "rb"))


        os.remove(file_name)

        await message.answer("✅ Ko`chirib bo`lindi.")
    except Exception as e:
        print(f"❌ xato yuz berdi {e}")

if __name__=="__main__":
    if not os.path.exists("downloads"):
        os.mkdir("downloads")
    executor.start_polling(dp, skip_updates=True)

#7550500382:AAFwoJP54vMxtkQZOG9o7hwGo1Rs6KpXv6s