"""Portal: Application error handlers"""

from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse

from os_cfdb.models.generic import (
    ErrorConflict,
    ErrorFailedDependency,
    ErrorForbidden,
    ErrorJWTValidationFailed,
    ErrorNotFound,
)

error_responses = {
    403: {"model": ErrorForbidden},
    404: {"model": ErrorNotFound},
    409: {"model": ErrorConflict},
    401: {"model": ErrorJWTValidationFailed},
    424: {"model": ErrorFailedDependency},
}


get_error_responses = {
    401: {"model": ErrorJWTValidationFailed},
    404: {"model": ErrorNotFound},
    403: {"model": ErrorForbidden},
    424: {"model": ErrorFailedDependency},
}

post_error_responses = {
    401: {"model": ErrorJWTValidationFailed},
    403: {"model": ErrorForbidden},
    404: {"model": ErrorNotFound},
    409: {"model": ErrorConflict},
    424: {"model": ErrorFailedDependency},
}

delete_error_responses = {
    401: {"model": ErrorJWTValidationFailed},
    403: {"model": ErrorForbidden},
    404: {"model": ErrorNotFound},
    424: {"model": ErrorFailedDependency},
}

put_error_responses = {
    401: {"model": ErrorJWTValidationFailed},
    403: {"model": ErrorForbidden},
    404: {"model": ErrorNotFound},
    424: {"model": ErrorFailedDependency},
}


class Http401Exception(HTTPException):
    """HTTP 401 Custom Exception handler.

    Args:
        HTTPException (Exception): Starlette HTTP exception.
    """


class Http404Exception(HTTPException):
    """HTTP 404 Custom Exception handler.

    Args:
        HTTPException (Exception): [Starlette HTTP exception.
    """


class Http403Exception(HTTPException):
    """HTTP 403 Custom Exception handler.

    Args:
        HTTPException (Exception): Starlette HTTP exception.
    """


class Http409Exception(HTTPException):
    """HTTP 409 Custom Exception handler.

    Args:
        HTTPException (Exception): Starlette HTTP exception.
    """


class Http424Exception(HTTPException):
    """HTTP 424 Custom Exception handler.

    Args:
        HTTPException (Exception): Starlette HTTP exception.
    """


# the following calling convetion is required
# pylint: disable=unused-argument
async def http_401_exception_handler(request: Request, exc: Http401Exception) -> JSONResponse:
    """401 unauthorized HTTP error handler.

    Exception handler that is registered with FastAPI to handle status code errors of 401.

    Args:
        request (Request): FastAPI Request object.
        exc (Http401Exception): Exception handler.

    Returns:
        JSONResponse: Returns a ErrorJWTValidationFailed modeled error.
    """
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorJWTValidationFailed(code=exc.status_code, message=exc.detail).dict(),
    )


# pylint: disable=unused-argument
async def http_403_exception_handler(request: Request, exc: Http403Exception) -> JSONResponse:
    """401 unauthorized HTTP error handler.

    Exception handler that is registered with FastAPI to handle status code errors of 401.

    Args:
        request (Request): FastAPI Request object.
        exc (Http403Exception): Exception handler.

    Returns:
        JSONResponse: Returns a ErrorJWTValidationFailed modeled error.
    """

    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorForbidden(code=exc.status_code, message=exc.detail).dict(),
    )


# pylint: disable=unused-argument
async def http_404_exception_handler(request: Request, exc: Http404Exception) -> JSONResponse:
    """403 no found HTTP error handler.

    Exception handler that is registered with FastAPI to handle status code errors of 404.

    Args:
        request (Request): FastAPI Request object.
        exc (Http404Exception): Exception handler.

    Returns:
        JSONResponse: Returns a ErrorJWTValidationFailed modeled error.
    """

    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorNotFound(code=exc.status_code, message=exc.detail).dict(),
    )


# pylint: disable=unused-argument
async def http_409_exception_handler(request: Request, exc: Http409Exception) -> JSONResponse:
    """409 conflict HTTP error handler.

    Exception handler that is registered with FastAPI to handle status code errors of 409.

    Args:
        request (Request): FastAPI Request object.
        exc (Http409Exception): Exception handler.

    Returns:
        JSONResponse: Returns a ErrorJWTValidationFailed modeled error.
    """

    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorConflict(code=exc.status_code, message=exc.detail).dict(),
    )


# pylint: disable=unused-argument
async def http_424_exception_handler(request: Request, exc: Http424Exception) -> JSONResponse:
    """424 HTTP error handler.

    Handler for 424 error to transform default pydantic error object to gothinkster format.

    Args:
        request (Request): request object from the caller.
        exc (HTTPException): request exception to be handled.

    Returns:
        JSONResponse: Returns a ErrorFailedDependency modeled error
    """

    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorFailedDependency(code=exc.status_code, message=exc.detail).dict(),
    )
