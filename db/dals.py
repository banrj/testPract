from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Optional

from db.models import User


class UserDAL:

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_user(
        self,
        name: str,
        email: str,
        hashed_password: str,
    ) -> User:
        new_user = User(
            name=name,
            email=email,
            hashed_password=hashed_password,
        )
        self.db_session.add(new_user)
        await self.db_session.flush()
        return new_user

    async def get_user_by_name(self, name: str) -> Optional[User]:
        query = select(User).where(User.name == name)
        res = await self.db_session.execute(query)
        user_row = res.fetchone()
        print(user_row)
        if user_row:
            return user_row[0]
