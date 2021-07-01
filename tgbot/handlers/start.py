from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.config import load_config
from tgbot.models.models import User, Quiz, Question
from tgbot.services.database import create_db_session


async def start(message: Message):
    await message.reply(f"Hello, {message.from_user.username}, for start quiz click to the -> /quiz")
    config = load_config()
    session = await create_db_session(config)
    users = await User.get_all_users(db_session=session)
    for user in users:
        print(user.telegram_id, flush=True)

    print("ALL USERS -->", users, flush=True)
    quiz = await Quiz.get_quiz(db_session=session, id=1)
    print("QUIZ_THEME -->>", quiz, flush=True)
    # await Quiz.add_quiz(db_session=session, theme='Apple')
    # await Question.add_question(db_session=session, quiz_id=1, question='Its an apple?', answer='True')
    if await User.get_user(db_session=session,
                           telegram_id=message.from_user.id):
        return
    await User.add_user(db_session=session,
                        telegram_id=message.from_user.id,
                        chat_id=message.chat.id,
                        first_name=message.from_user.first_name,
                        last_name=message.from_user.last_name,
                        username=message.from_user.username)


def get_start(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"], state="*")

