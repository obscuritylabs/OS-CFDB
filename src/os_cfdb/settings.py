from functools import lru_cache
from multiprocessing import cpu_count
from typing import List

from dotenv import load_dotenv
from pydantic import BaseSettings, Field, SecretStr, StrictBool

from os_cfdb import __version__

load_dotenv()  # pragma: no cover


def number_of_workers():
    """Calculate worker count.

    Worker count based on CPU resources.

    Returns:
        cpu c (int): worker count
    """
    return (cpu_count() * 2) + 1


class CORSSettings(BaseSettings):
    """CORS Environment settings & configuration.

    Args:
        BaseSettings (Class): Pydantic BaseSetting management
    """

    # Settings for the CORS
    default_sites: List[str] = [
        "http://localhost",
        "https://localhost",
        "http://localhost:3000",
        "https://localhost:3000",
        "http://localhost:8000",
        "https://localhost:8000",
    ]

    # EXAMPLE: export origins='["http://localhost", "http://127.0.0.1"]'
    origins: List[str] = default_sites
    allow_credentials: StrictBool = True
    # EXAMPLE: export allow_methods='["POST", "GET"]'
    allow_methods: List[str] = ["*"]
    allow_headers: List[str] = ["authorization", "*"]


class AppConfig(BaseSettings):
    # Application Setting
    PROJECT_NAME: str = "OS-CFDB"
    LOG_LEVEL: str = "INFO"
    ROOT_PATH: str = ""

    # Host server configuration
    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: str = "8000"
    SERVER_WORKERS: int = Field(default_factory=number_of_workers)

    # CORS settings
    corssettings: CORSSettings = Field(default_factory=CORSSettings)

    # MongoDB configuration
    MONGO_PORT: int = 27017
    MONGO_USER: str = ""
    MONGO_PASS: SecretStr
    MONGO_AUTH_DATABASE: str = "local"
    MONGO_HOST: str = ""
    MONGO_DATABASE: str = "os_cfdb"
    MONGO_RETRY_WRITES: bool = True

    @property
    def mongo_dsn(self) -> str:
        return f"mongodb+srv://{self.MONGO_USER}:{self.MONGO_PASS.get_secret_value()}@{self.MONGO_HOST}"


@lru_cache()  # pragma: no cover
def settings() -> AppConfig:
    """Portal application configuration and settings.

    Returns:
        AppConfig: Portal BaseSetting
    """
    return AppConfig()
