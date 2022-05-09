from typing import List, Optional

from beanie import PydanticObjectId
from pydantic import BaseModel

from os_cfdb.api.v1.finding.models import Metadata, NistPublication_800_53, Reference, Risk, Service, TechnicalData


class FindingRead(BaseModel):
    id: PydanticObjectId
    title: str
    vsr: int
    cvss: int
    risk: Risk
    internal_id: str
    service: List[Service]
    nist_publication: List[NistPublication_800_53]
    references: Optional[List[Reference]]
    technical_data: TechnicalData
    metadata: Metadata


class FindingCreate(BaseModel):
    title: str
    vsr: int
    cvss: int
    risk: Risk
    internal_id: str
    service: List[Service]
    nist_publication: List[NistPublication_800_53]
    references: Optional[List[Reference]]
    technical_data: TechnicalData
    metadata: Metadata


class FindingDelete(BaseModel):
    pass


class FindingUpdate(BaseModel):
    pass


class FindingList(BaseModel):
    pass


class FindingResponseModel(BaseModel):
    data: FindingRead
