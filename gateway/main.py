import uvicorn
from fastapi import FastAPI

from settings import settings
from routers import router as gateway_router


def create_app() -> FastAPI:
    app = FastAPI(title="Gateway")
    app.include_router(gateway_router)

    return app


if __name__ == "__main__":
    app = create_app()

    uvicorn.run(app=app, host=settings.GATEWAY_HOST, port=settings.GATEWAY_PORT, log_level="info")
