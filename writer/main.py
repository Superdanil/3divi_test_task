import uvicorn
from fastapi import FastAPI

from settings import settings
from writer import write_router


def create_app() -> FastAPI:
    app = FastAPI(title="Сервис записи")
    app.include_router(write_router)

    return app


if __name__ == "__main__":
    app = create_app()

    uvicorn.run(
        app=app,
        host=settings.WRITE_SERVICE_HOST,
        port=settings.WRITE_SERVICE_PORT,
        log_level="info",
    )
