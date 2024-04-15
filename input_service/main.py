import aiohttp
import uvicorn
from fastapi import FastAPI, status
from fastapi.encoders import jsonable_encoder
from schemas import Req
from config import HANDLE_SERVICE_URL

app = FastAPI(title="Сервис-приёмщик")


@app.post("/", status_code=status.HTTP_200_OK)
async def gogogo(req: Req) -> dict:

    payload = jsonable_encoder(req)

    async with aiohttp.ClientSession() as session:
        await session.post(HANDLE_SERVICE_URL,
                           headers={"Content-Type": "application/json"},
                           json=payload)

    return {"asyncAnswer": "Ok"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, log_level="info", reload=True)
