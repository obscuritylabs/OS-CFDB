from enum import Enum
from http import HTTPStatus

from pydantic import BaseModel, Field

from os_cfdb.core.utils import to_camel


class CamelBase(BaseModel):  # noqa: H601
    """Core CamelCase Basemodel.

    Args:
        BaseModel (class): pydantic basemodel
    """

    class Config:  # noqa: H601
        """Pydantic model with BaseModel to use accross all custom BaseModels."""

        alias_generator = to_camel
        allow_population_by_field_name = True


class ResponseModel(CamelBase):  # noqa: H601
    """Base API response model."""

    code: HTTPStatus = Field(
        200,
        title="HTTP Status Code",
        description="The HTTP status code can be used for frontend error codes.",
    )
    message: str = Field(
        None,
        title="Operation Message",
        description="Backend message of operation taking place.",
    )


class ErrorResponse(str, Enum):  # noqa: H601
    """Error Responses Options"""

    NOT_FOUND = "Item not found"
    INTERNAL_SERVER_ERROR = "Unknown server error"
    CONFLICT = "Item already exists"
    UNAUTHORIZED = "Request is unauthorized check token or refresh login"
    FORBIDDEN = "Requester does not have access rights to requested content"
    FAILED_DEPENDENCY = "Authentication failed due to an inaccessable upstream resource"


class ErrorResponseModel(ResponseModel):  # noqa: H601
    """Portal base error API response model."""

    error: ErrorResponse = Field(..., description="The error message coresponding to code")


class ErrorNotFound(ErrorResponseModel):  # noqa: H601
    """Portal base error API response model."""

    code: HTTPStatus = Field(
        HTTPStatus.NOT_FOUND,
        title="HTTP Status Code",
        description="The HTTP status code can be used for frontend error codes.",
    )
    error: ErrorResponse = Field(ErrorResponse.NOT_FOUND, description="The error message coresponding to code")


class ErrorJWTValidationFailed(ErrorResponseModel):  # noqa: H601
    """Portal base error for JWTValidation Errors"""

    code: HTTPStatus = Field(
        HTTPStatus.UNAUTHORIZED,
        title="HTTP Status Code",
        description="The HTTP status code can be used for frontend error codes.",
    )
    error: ErrorResponse = Field(ErrorResponse.UNAUTHORIZED, description="The error message coresponding to code")


class ErrorForbidden(ErrorResponseModel):  # noqa: H601
    """Portal base error for client access rights"""

    code: HTTPStatus = Field(
        HTTPStatus.FORBIDDEN,
        title="HTTP Status Code",
        description="The HTTP status code can be used for frontend error codes.",
    )
    error: ErrorResponse = Field(ErrorResponse.FORBIDDEN, description="The error message coresponding to code")


class ErrorFailedDependency(ErrorResponseModel):  # noqa: H601
    """Portal base error for JWKS"""

    code: HTTPStatus = Field(
        HTTPStatus.FAILED_DEPENDENCY,
        title="HTTP Status Code",
        description="The HTTP status code can be used for frontend error codes.",
    )
    error: ErrorResponse = Field(ErrorResponse.FAILED_DEPENDENCY, description="The error message coresponding to code")


class ErrorConflict(ErrorResponseModel):  # noqa: H601
    """Portal base error API response model."""

    code: HTTPStatus = Field(
        HTTPStatus.CONFLICT,
        title="HTTP Status Code",
        description="The HTTP status code can be used for frontend error codes.",
    )
    error: ErrorResponse = Field(ErrorResponse.CONFLICT, description="The error message coresponding to code")


class ErrorUnauthorized(ErrorResponseModel):  # noqa: H601
    """Portal base error API response model."""

    code: HTTPStatus = Field(
        HTTPStatus.UNAUTHORIZED,
        title="HTTP Status Code",
        description="The HTTP status code can be used for frontend error codes.",
    )
    error: ErrorResponse = Field(ErrorResponse.UNAUTHORIZED, description="The error message coresponding to code")


class ValidationError(BaseModel):  # noqa: H601
    """FastAPI validation model"""

    loc: list[str]
    msg: str
    type: str


class HTTPValidationError(BaseModel):  # noqa: H601
    """FastAPI validation model."""

    detail: list[ValidationError]
