import asyncio
import json
import multiprocessing

import aiohttp
import uvicorn
from fastapi import FastAPI, status

from config import WRITE_SERVICE_URL
from schemas import Req

app = FastAPI(title="Сервис-обработчик")


@app.post("/", status_code=status.HTTP_200_OK)
async def handle(req: Req):
    payload = req.model_dump(mode="json")

    async with aiohttp.ClientSession() as session:
        res = await session.post(f'{WRITE_SERVICE_URL}/txt2',
                                 headers={"Content-Type": "application/json"},
                                 json=payload)
        res = await res.json()
        print(res)

    await asyncio.sleep(req.delay_seconds)

    req_payload = payload | res

    async with aiohttp.ClientSession() as session:
        await session.post(f'{WRITE_SERVICE_URL}/txt1',
                           headers={"Content-Type": "application/json"},
                           json=req_payload)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8001, log_level="info", reload=True)
