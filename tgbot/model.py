from sqlalchemy import Column, BigInteger, insert, String, update, Integer, ForeignKey
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker

from tgbot.services.db_base import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "telegram_users"
    telegram_id = Column(BigInteger, primary_key=True)
    chat_id = Column(BigInteger, nullable=False)
    first_name = Column(String(length=100), nullable=True)
    last_name = Column(String(length=100), nullable=True)
    username = Column(String(length=100), nullable=True)

    @classmethod
    async def get_user(cls, db_session: sessionmaker, telegram_id: int) -> 'User':
        async with db_session() as db_session:
            sql = select(cls).where(cls.telegram_id == telegram_id)
            request = await db_session.execute(sql)
            user: cls = request.scalar()
        return user

    @classmethod
    async def add_user(cls,
                       db_session: sessionmaker,
                       telegram_id: int,
                       chat_id: int,
                       first_name: str,
                       last_name: str = None,
                       username: str = None,
                       ) -> 'User':
        async with db_session() as db_session:
            sql = insert(cls).values(telegram_id=telegram_id,
                                     chat_id=chat_id,
                                     first_name=first_name,
                                     last_name=last_name,
                                     username=username).returning('*')
            result = await db_session.execute(sql)
            await db_session.commit()
            return result.first()

    async def update_user(self, db_session: sessionmaker, updated_fields: dict) -> 'User':
        async with db_session() as db_session:
            sql = update(User).where(User.telegram_id == self.telegram_id).values(**updated_fields)
            result = await db_session.execute(sql)
            await db_session.commit()
            return result

    def __repr__(self):
        return f'User (ID: {self.telegram_id} - {self.first_name} {self.last_name})'


class Quiz(Base):
    __tablename__ = "quizzes"
    id = Column(Integer, primary_key=True)
    theme = Column(String, nullable=False)
    questions = relationship('Question', back_populates='quizzes')


class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True)
    quiz_id = Column(Integer, ForeignKey('quizzes.id'))
    quiz = relationship("Quiz", back_populates="questions")
    answer = Column(String, nullable=False)
