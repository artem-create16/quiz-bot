from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from tgbot.models.models import Quiz


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Dogs"),
            KeyboardButton(text="Cats")
        ],
        [
            KeyboardButton(text="")
        ],
    ],
    resize_keyboard=True
)