from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config.data import topics

items = {
    False: "✅ ",
    True: "🚫 "
}


def multiple_select():
    keyboard = InlineKeyboardMarkup()
    for topic in topics.values():
        text = f"🚫 {topic.url}"
        callback_data = f"choose_topic|{topic.id}|false"

        keyboard.row(
            InlineKeyboardButton(
                text=text,
                callback_data=callback_data
            )
        )
    keyboard.row(
        InlineKeyboardButton(
            text="Подтвердить",
            callback_data="choose_topic_ready"
        )
    )
    return keyboard


def change_multiple_select(keyboard: InlineKeyboardMarkup, key: int, condition: bool):
    new_str_condition = 'true' if not  condition else 'false'
    new_keyboard = InlineKeyboardMarkup()
    for line in keyboard.inline_keyboard:
        if line[0].callback_data == "choose_topic_ready":
            continue
        if line[0].callback_data.split('|')[1] == str(key):
            new_keyboard.row(
                InlineKeyboardButton(
                    text=items[condition] + line[0].text[2:],
                    callback_data=f"choose_topic|{key}|{new_str_condition}")
            )
        else:
            new_keyboard.row(line[0])

    new_keyboard.row(
        InlineKeyboardButton(
            text="Подтвердить",
            callback_data="choose_topic_ready"
        )
    )
    return new_keyboard
