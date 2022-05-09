from beanie import init_beanie
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from os_cfdb.api.v1.finding.models import Finding
from os_cfdb.api.v1.user.models import User
from os_cfdb.models.announcement import Announcement
from os_cfdb.settings import settings

app = FastAPI(
    title=settings().PROJECT_NAME,
    root_path=settings().ROOT_PATH,
)


@app.on_event("startup")
async def startup() -> None:
    """FastAPI startup."""
    client = AsyncIOMotorClient(settings().mongo_dsn)
    await init_beanie(database=client[settings().MONGO_DATABASE], document_models=[Announcement, Finding, User])
