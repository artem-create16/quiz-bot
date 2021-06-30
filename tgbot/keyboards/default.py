from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Dogs"),
            KeyboardButton(text="Cats")
        ],
    ],
    resize_keyboard=True
)