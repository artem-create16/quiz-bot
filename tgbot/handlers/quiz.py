from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.keyboards.default import menu


async def quiz(message: Message):
    await message.reply("Select the theme of quiz in keyboards", reply_markup=menu)


def get_quiz(dp: Dispatcher):
    dp.register_message_handler(quiz, commands=["quiz"], state="*")
