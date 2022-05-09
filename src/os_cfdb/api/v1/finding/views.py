from beanie import PydanticObjectId
from fastapi import APIRouter

from os_cfdb.api.v1.finding.crud import create_finding, get_finding
from os_cfdb.api.v1.finding.schemas import FindingCreate, FindingResponseModel

router = APIRouter(prefix="/finding", tags=["finding"])


@router.post("/", response_model=FindingResponseModel)
async def add_finding(finding_data: FindingCreate) -> FindingResponseModel:
    finding = await create_finding(finding_data)
    return FindingResponseModel(data=finding)


@router.get("/{finding_id}", response_model=FindingResponseModel)
async def finding(finding_id: PydanticObjectId) -> FindingResponseModel:
    finding = await get_finding(finding_id)
    return FindingResponseModel(data=finding)
