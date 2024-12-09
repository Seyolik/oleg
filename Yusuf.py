import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor

API_TOKEN = '7937709942:AAGn3JpGoNUI8Gd1eO_2WweoVKkjGqNgmDE'

logging.basicConfig(level = logging.INFO)

bot = Bot(token = API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply('Я голосовой автоответчик Олег, к вашим услугам. Напиши /help для списка команд')
@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply('Команды: /anekdot, /mat')

@dp.message_handler(commands=['anekdot'])
async def send_welcome(message: types.Message):
    await message.reply('-Здравствуйте, меня зовут Олег, и я врун. -Садись, Олег. -Я не Олег.')

@dp.message_handler(commands=['mat'])
async def send_welcome(message: types.Message):
    await message.reply('Материться - плохо!!!')

dp.message_handler()
async def echo(message: types.Message):
    await message.reply('По звёздочка звёздочка звёздочка звёздочка на звёздочка звёздочка звёздочка звёздочка')

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
