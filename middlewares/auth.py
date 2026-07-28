from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject
from database.connection import AsyncSessionLocal
from database.models import User
from sqlalchemy import select

class UserAuthMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        if isinstance(event, Message) and event.from_user:
            async with AsyncSessionLocal() as session:
                stmt = select(User).where(User.id == event.from_user.id)
                result = await session.execute(stmt)
                user = result.scalar_one_or_none()

                if not user:
                    user = User(
                        id=event.from_user.id,
                        username=event.from_user.username,
                        first_name=event.from_user.first_name
                    )
                    session.add(user)
                    await session.commit()

                if user.is_banned:
                    await event.answer("🚫 Your account has been suspended by an administrator.")
                    return

                data["db_user"] = user

        return await handler(event, data)
