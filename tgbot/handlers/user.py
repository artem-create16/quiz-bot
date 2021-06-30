from aiogram import Dispatcher
from aiogram.types import Message
from tgbot.models.users import User
from tgbot.services.database import create_async_engine

from tgbot.config import load_config
from tgbot.services.database import create_db_session


async def user_start(message: Message):
    await message.reply(f"Hello, {message.from_user.username}")
    config = load_config()
    session = await create_db_session(config)
    await User.add_user(db_session=session,
                    telegram_id=message.from_user.id,
                    chat_id=message.chat.id,
                    first_name=message.from_user.first_name,
                    last_name=message.from_user.last_name,
                    username=message.from_user.username)


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
