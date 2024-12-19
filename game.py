import logging
from distutils.command.build import build
# import sqlite3
from random import random, randrange, randint
from aiogram import Bot, Dispatcher, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import InputFile
from dotenv import load_dotenv
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder
import os
from aiogram.filters import CommandStart , Command
from aiogram.types.callback_query import CallbackQuery
import asyncio
from aiogram.types import Message, CallbackQuery


token = '8161499707:AAHSXk_XZSK2ZZ1cZ7gweY4Qax3UiMgcrmM'

logging.basicConfig(level=logging.INFO)
bot = Bot(token = token)


dp = Dispatcher()



@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Добрый день, что вы хотите сделать: ', reply_markup=create_inline_kb())


# def ease_link_kb():
#     inline_kb_list = [
#         [InlineKeyboardButton(text="Мой хабр", url='https://habr.com/ru/users/yakvenalex/')],
#         [InlineKeyboardButton(text="Мой Telegram", url='tg://resolve?domain=yakvenalexx')],
#         [InlineKeyboardButton(text="Веб приложение", web_app=WebAppInfo(url="https://tg-promo-bot.ru/questions"))]
#     ]
#     return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)
#
#
# @dp.message(F.text == '123')
# async def get_inline_btn_link(message: Message):
#     await message.answer('Вот тебе инлайн клавиатура со ссылками!', reply_markup=ease_link_kb())


# def create_room():
#     bot.send_message('Введите код комнаты')
#
#
# def inline_button():
#     inline_kb_list = [
#         [InlineKeyboardButton(text="Создать комнату", callback_data='create_room')],
#         [InlineKeyboardButton(text="Войти в комнату", url='tg://resolve?domain=yakvenalexx')]
#     ]
#     return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

def create_inline_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text = "Создать комнату",
            callback_data='create_room'
        )
    )
    builder.row(
        InlineKeyboardButton(
            text="Войти в комнату",
            callback_data='join_room'
        )
    )


    builder.adjust(1)
    return builder.as_markup()

@dp.callback_query(F.data == 'create_room')
async def create_new_room(call: CallbackQuery):
    id_room = randint(1000,9999)
    await call.answer('Создание комнаты....')
    formatted_message = (
        f"Комната создана\n"
        f"Айди комнаты: {id_room}"
    )
    await call.message.answer(formatted_message)

class ChooseID(StatesGroup):
    choosing_id = State()
    normal = State()

@dp.callback_query(F.data == 'join_room')
async def join_to_room(call: CallbackQuery, state:FSMContext):
    await call.message.answer('Введите айди комнаты: ')
    await state.set_state(ChooseID.choosing_id)
    print(state.get_state())


@dp.message(
    ChooseID.choosing_id
)
async def room_chosen(message: Message, state: FSMContext):
    await state.update_data(chosen_room_id=message.text.lower())
    await message.answer(
        text=f"Спасибо. ID={message.text.lower()}"
    )
    await state.set_state(ChooseID.normal)

# @dp.message_handler(Command('help'))
# async def send_welcome(message: Message):
#     await message.answer('Добрый день, что вы хотите сделать: ', reply_markup=create_inline_kb())


# @dp.callback_query(F.data == 'create_room')
# async def on_buton_clicked(callback: CallbackQuery):
#     await create_room()


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
