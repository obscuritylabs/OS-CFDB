from gettext import find

from beanie import PydanticObjectId
from fastapi import status

from os_cfdb.api.v1.finding.models import Finding
from os_cfdb.api.v1.finding.schemas import FindingCreate, FindingRead
from os_cfdb.core.errors import Http404Exception


async def get_finding(finding_id: PydanticObjectId) -> Finding:
    finding = await Finding.get(finding_id)
    if not finding:
        raise Http404Exception(status_code=status.HTTP_404_NOT_FOUND, detail=f"Finding {finding_id} doesn't exist.")
    return finding


async def create_finding(finding_data: FindingCreate) -> FindingRead:
    finding = Finding(**finding_data.dict())
    await finding.insert()
    return FindingRead(**finding.dict())
