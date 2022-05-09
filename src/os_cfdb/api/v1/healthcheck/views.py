from fastapi import APIRouter

from os_cfdb.api.v1.healthcheck.models import HealthcheckStatusModel, HealthcheckStatusResponseModel

router = APIRouter(prefix="/healthcheck", tags=["healthcheck"])


@router.get("/", response_model=HealthcheckStatusResponseModel)
async def healthcheck() -> HealthcheckStatusResponseModel:
    """Server Healthcheck API Endpoint.

    Returns:
        HealthcheckStatusResponseModel: Healthcheck status response model.
    """
    status = HealthcheckStatusModel(status=True)
    return HealthcheckStatusResponseModel(data=status)
