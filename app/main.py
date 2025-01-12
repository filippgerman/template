from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI

from app.application.controllers.health_check_controller import router as health_check_router
from app.application.dependency.db_dependency import get_db_session
from app.config.app import get_config

config = get_config()


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

    app.include_router(health_check_router, dependencies=[Depends(get_db_session)])

    return app


app = create_app()
