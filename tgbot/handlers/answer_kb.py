from aiogram import Dispatcher, types
from aiogram.types import Message, MessageEntity
from aiogram.types import ReplyKeyboardRemove
from tgbot.models.models import User
from tgbot.config import load_config
from tgbot.models.models import User
from tgbot.services.database import create_db_session


async def get_answer(message: Message):
    options = ["True", "False"]
    await message.answer_poll(question="its a cat?", options=options,
                              type='quiz', correct_option_id=0, explanation="12345",
                              reply_markup=ReplyKeyboardRemove())


async def yes(quiz_answer: types.PollAnswer):
    config = load_config()
    session = await create_db_session(config)
    user = User.get_user(db_session=session, telegram_id=quiz_answer.user.id)
    print("USER_CHAT -->>", user, flush=True)

    await quiz_answer.bot.send_message(chat_id=user, text='Nice')


def answer_kb(dp: Dispatcher):
    dp.register_message_handler(get_answer, lambda message: message.text.lower() == 'cats', state="*")
    dp.register_poll_answer_handler(yes)
