from datetime import datetime
from enum import Enum
from typing import List, Optional

import pymongo
from beanie import Document, Indexed
from pydantic import AnyUrl, BaseModel, EmailStr, Field

from os_cfdb.models.generic import CamelBase, ResponseModel


class Risk(str, Enum):  # noqa: H601
    """Finding risk enum.

    Findings always have a recommended risk associated with them.
    By no means this risk is locked in and may offten have to be adjusted
    for each test.
    """

    info = "informational"
    low = "low"
    medium = "medium"
    high = "high"
    critical = "critical"


class ServiceType(str, Enum):  # noqa: H601
    """Finding service type enum.

    Findings are required to be tied to a service type selection.
    This provides the user a insight into the type of finding and when
    you apply the finding to the type of testing taking place.
    """

    internal_penetration_test = "Internal Penetration Testing"
    external_penetration_test = "External Penetration Testing"
    web_application_penetration_test = "Web Application Penetration Testing"
    mobile_application_penetration_test = "Mobile Application Penetration Testing"
    wifi_penetration_test = "WiFI Penetration Testing"


class Service(BaseModel):  # noqa: H601
    """Finding Service Assigned.

    Findings offten have multiple types of services applied to them.
    This provides the reader the various types of service lines the finding
    applies to.
    """

    type: ServiceType
    description: str


class NistPublication_800_53(BaseModel):  # noqa: H601
    """Fiding NIST 800-53 controls.

    Findings offten have NIST controls that an be applied for
    further reading and research. These are meant to IA controls
    and other controls to help aid the report reader.
    """

    control: str


class Reference(BaseModel):  # noqa: H601
    """Finding public reference.

    Findings offten have useful resources that are public such as
    exploit breakdowns, defenders guides, and other helpful data.
    We create this so we can tie in helpful resources for our clients.
    """

    name: str
    url: AnyUrl = Field(description="URL of reference that supports the finding", example="https://www.google.com/")


class Metadata(BaseModel):  # noqa: H601
    """Finding Metadata.

    Every finding within OS-CFDB must have finding metadata attached.
    This provides users of OS-CFDB the ability to contact or find help
    when raising issues with the original finding data.
    """

    author: str
    twitter_url: Optional[AnyUrl] = Field(
        description="Authors URL to their twitter profile", example="https://twitter.com/killswitch_gui"
    )
    email: Optional[EmailStr] = Field(description="Authors email address")
    creation_date: datetime = Field(
        default_factory=datetime.utcnow,
        description="UTC Datetime of when the finding was created",
    )
    modified_date: datetime = Field(
        default_factory=datetime.utcnow,
        description="UTC Datetime of when the finding was last modified",
    )


class TechnicalData(BaseModel):  # noqa: H601
    """Finding Technical Data.

    Finding technical data is core of the finding. It provides the
    reader the key data required to successfully understand the details
    of the what and why and how to remediate.
    """

    description: str
    impact: str
    recomendation: str


class Finding(Document):  # noqa: H601
    """OS-CFDB Finding.

    OS-CFDB stores various diffrent findings. This document is the core
    structure of what a `finding` is within the system. This stores all the
    various inforation required to display a finding to a user.
    """

    title: Indexed(str, index_type=pymongo.TEXT)  # type: ignore
    vsr: int
    cvss: int
    risk: Risk
    internal_id: str
    service: List[Service]
    nist_publication: List[NistPublication_800_53]
    references: Optional[List[Reference]]
    technical_data: TechnicalData
    metadata: Metadata
