import asyncio
import logging
import sys
import os
TOKEN = os.environ['TOKEN']

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Router

from aiogram.types.callback_query import CallbackQuery
from aiogram import F

router = Router(name=__name__)






dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")

# @dp.callback_query_handler(func=lambda c: c.data == 'button1')
# async def process_callback_button1(callback_query: types.CallbackQuery):
#     await Bot.answer_callback_query(callback_query.id)
#     await Bot.send_message(callback_query.from_user.id, 'Нажата первая кнопка!')


@dp.message()
async def echo_handler(message: types.Message) -> None:
    builder = InlineKeyboardBuilder()
    for index in range(1, 11):
        builder.button(text=f"Set {index}", callback_data=f"set:{index}")
    await message.answer("Some text here", reply_markup=builder.as_markup())
    # for index in range(1, 11):
    # builder.button(text=f"Set {index}", callback_data=f"set:{index}")
    # inline_btn_1 = InlineKeyboardButton('Первая кнопка!', callback_data='button1')
    # inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)
    # await message.reply("Первая инлайн кнопка", reply_markup=inline_kb1)
        # Send a copy of the received message

@dp.callback_query(F.data == "set:10")
async def my_handler(callback_query: CallbackQuery ):
      
        print("11")
        # await Bot.callback_query(callback_query.id)
        await callback_query.answer(text='Нажата первая кнопка!')# выводит ответ всплывающим сообщением
        # callback_answer.text = "All is ok"

@dp.callback_query(F.data == "set:9")
async def my_handler(callback_query: CallbackQuery ):
       
        print("1")
        # await Bot.callback_query(callback_query.id)
        await callback_query.answer(text='Нажата первая кнопка!')# выводит ответ всплывающим сообщением
        # callback_answer.text = "All is ok"

async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())