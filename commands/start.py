from copy import deepcopy

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Regexp

import keyboards
from config import dp


@dp.message_handler(Command("start"))
async def start(message: types.Message):
    await message.answer("Выберите топики", reply_markup=keyboards.multiple_select())


@dp.callback_query_handler(Regexp(r'choose_topic\|\d+\|\w{4,5}'))
async def choose_topic_change(call: types.CallbackQuery, state: FSMContext):
    _, key, str_condition = call.data.split("|")
    condition = True if str_condition == "true" else False
    keyboard = call.message.reply_markup
    new_keyboard = keyboards.change_multiple_select(keyboard, key, condition)
    await call.message.edit_reply_markup(reply_markup=new_keyboard)
