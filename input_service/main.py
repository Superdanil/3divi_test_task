from settings import settings

import aiohttp
import uvicorn
from fastapi import FastAPI, status
from fastapi.encoders import jsonable_encoder

from schemas import Req

app = FastAPI(title="Сервис-приёмщик")


@app.post("/", status_code=status.HTTP_200_OK)
async def gogogo(req: Req) -> dict:
    payload = jsonable_encoder(req)

    async with aiohttp.ClientSession() as session:
        await session.post(settings.handle_service_url,
                           headers={"Content-Type": "application/json"},
                           json=payload)

    return {"asyncAnswer": "Ok"}


print()
if __name__ == "__main__":
    print(settings.INPUT_SERVICE_HOST, settings.INPUT_SERVICE_PORT)
    uvicorn.run(
        app="main:app",
        host=settings.INPUT_SERVICE_HOST,
        port=settings.INPUT_SERVICE_PORT,
        log_level="info",
        reload=True
    )
