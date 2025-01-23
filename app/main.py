from contextlib import asynccontextmanager

import sentry_sdk
from fastapi import FastAPI

from app.application.controllers.health_check_controller import router as health_check_router
from app.config.app import get_config
from app.utils.logging_config import setup_logger

config = get_config()
setup_logger()

if config.ENVIRONMENT != "LOCAL":
    sentry_sdk.init(
        dsn=config.SENTRY_DSN,
        traces_sample_rate=1.0,
    )

app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application lifecycle."""
    yield


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title=config.PROJECT_NAME,
        version=config.APP_VERSION,
        description="Template FastAPI application",
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
        lifespan=lifespan,
    )

    app.include_router(health_check_router)

    return app


app = create_app()
