import asyncio
from settings import settings

import aiohttp
import uvicorn
from fastapi import FastAPI, status

from schemas import Req

app = FastAPI(title="Сервис-обработчик")


@app.post("/", status_code=status.HTTP_200_OK)
async def handle(req: Req):
    payload = req.model_dump(mode="json")

    async with aiohttp.ClientSession() as session:
        url = f"{settings.write_service_url}/write/txt2"
        res = await session.post(url,
                                 headers={"Content-Type": "application/json"},
                                 json=payload)
        res = await res.json()
        print(res)

    await asyncio.sleep(req.delay_seconds)

    req_payload = payload | res

    async with aiohttp.ClientSession() as session:
        url = f"{settings.write_service_url}/write/txt1"
        await session.post(url,
                           headers={"Content-Type": "application/json"},
                           json=req_payload)


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=settings.HANDLE_SERVICE_HOST,
        port=settings.HANDLE_SERVICE_PORT,
        log_level="info",
        reload=True
    )
