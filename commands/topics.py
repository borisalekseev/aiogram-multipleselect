from aiogram import types
from aiogram.dispatcher.filters import Text

from config import dp
from config.data import topics


@dp.callback_query_handler(Text("choose_topic_ready"))
async def selected_topics(call: types.CallbackQuery):
    text = "Вы выбрали данные топики:\n"
    for line in call.message.reply_markup.inline_keyboard:
        if line[0].callback_data == "choose_topic_ready":
            continue
        _, key, cond = line[0].callback_data.split("|")
        if cond == "true":
            text += topics[int(key)].url + "\n"
        print(key, cond)

    await call.message.answer(text)
