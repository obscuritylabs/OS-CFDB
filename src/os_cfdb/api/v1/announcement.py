from beanie import PydanticObjectId
from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from os_cfdb.models.announcement import Announcement, AnnouncementCreate

router = APIRouter(prefix="/announcement", tags=["announcement"])


# @router.get("/{id}", response_model=Announcement)
# async def get_announcement(id: PydanticObjectId) -> Announcement:
#     address = await Announcement.get(document_id=id)
#     if not address:
#         raise HTTPException(status_code=404)
#     return address


@router.post("/")
async def add_announcement(announcement: AnnouncementCreate):
    created_announcement = Announcement(
        title=announcement.title,
        short_summary=announcement.short_summary,
        full_announcement=announcement.full_announcement,
    )
    await created_announcement.save()
    if not created_announcement:
        raise HTTPException(status_code=404)
    return created_announcement
