import uvicorn
from fastapi import FastAPI

from settings import settings
from handler import router as handle_router


def create_app() -> FastAPI:
    app = FastAPI(title="Сервис-обработчик")
    app.include_router(handle_router)

    return app


if __name__ == "__main__":
    app = create_app()

    uvicorn.run(app=app, host=settings.HANDLE_SERVICE_HOST, port=settings.HANDLE_SERVICE_PORT, log_level="info")
