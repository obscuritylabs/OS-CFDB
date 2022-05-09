from pydantic import Field

from os_cfdb.models.generic import CamelBase, ResponseModel


class HealthcheckStatusModel(CamelBase):
    r"""Response model for standard health check.

    Args:
        ResponseModel (Class): primary API standard response
    """

    status: bool = Field(
        True,
        title="Healthcheck Status",
        description="Status of all core services are healthy and running for application.",
    )


class HealthcheckStatusResponseModel(ResponseModel):
    r"""Response model for standard health check.

    Args:
        ResponseModel (Class): primary API standard response
    """

    data: HealthcheckStatusModel
