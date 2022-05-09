from beanie import PydanticObjectId
from fastapi_users.db import BeanieBaseUser, BeanieUserDatabase


class User(BeanieBaseUser[PydanticObjectId]):
    pass


async def get_user_db():
    yield BeanieUserDatabase(User)
