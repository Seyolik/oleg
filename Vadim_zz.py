
import logging
from random import random, randrange, randint
from aiogram import Bot, Dispatcher, types
from aiogram.types import InputFile
from aiogram.types import ParseMode
from aiogram.utils import executor


#API BOTA
API_TOKEN = '7903656656:AAHmSnosRXxfZSrlEPCF4AwbEr7P-bWDjA8'


logging.basicConfig(level = logging.INFO)



bot = Bot(token = API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply('1./start, 2./bio, 3./rand, 4./photo')

@dp.message_handler(commands=['bio'])
async def send_welcome(message: types.Message):
    await message.reply('Олег —  мужское русское личное имя древнескандинавского происхождения.')

@dp.message_handler(commands=['rand'])
async def send_welcome(message: types.Message):
    await message.reply('У меня '+str(randint(0, 100))+' отчимов')

@dp.message_handler(commands=['photo'])
async def send_image(message: types.Message):
    images_path = 'photo\photo.jpg'

    with open(images_path, 'rb') as image:
        await bot.send_photo(message.chat.id, image)


@dp.message_handler()
async def echo(message: types.Message):
    await message.reply('Матери своей так говорить будешь')



if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)