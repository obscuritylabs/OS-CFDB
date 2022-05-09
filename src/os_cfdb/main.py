from os_cfdb.api.v1.announcement import router as AnnouncementRouter
from os_cfdb.api.v1.finding.views import router as FindingRouter
from os_cfdb.api.v1.healthcheck.views import router as HealthcheckRouter
from os_cfdb.api.v1.user import auth_backend, current_active_user, fastapi_users
from os_cfdb.api.v1.user.models import User
from os_cfdb.api.v1.user.schemas import UserCreate, UserRead, UserUpdate
from os_cfdb.app import app

# registered API routes
app.include_router(AnnouncementRouter)
app.include_router(HealthcheckRouter)
app.include_router(FindingRouter)

# FastAPI Users
app.include_router(fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"])
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)
