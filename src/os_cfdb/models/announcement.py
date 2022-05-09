from beanie import Document, Indexed
from pydantic import BaseModel

from os_cfdb.models.generic import CamelBase


class AnnouncementCreate(BaseModel):  # noqa: H601
    title: str
    short_summary: str
    full_announcement: str


class AnnouncementUpdate(BaseModel):  # noqa: H601
    """Updatable user fields."""

    title: str
    short_summary: str
    full_announcement: str


class AnnouncementOut(AnnouncementUpdate):  # noqa: H601
    """User fields returned to the client."""

    title: str
    short_summary: str
    full_announcement: str


class Announcement(Document):  # noqa: H601
    title: str
    short_summary: str
    full_announcement: Indexed(str)
