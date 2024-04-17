import asyncio

import aiohttp
from fastapi.encoders import jsonable_encoder

from schemas import Req
from settings import Settings


class HandleService:
    """Класс обработки запросов."""

    def __init__(self, settings: Settings):
        self.settings = settings

    async def write_files(self, req: Req) -> dict[str, str]:
        """Направляет запрос в сервис записи для записи файла txt1."""
        payload = jsonable_encoder(req)

        async with aiohttp.ClientSession() as session:
            url = f"{self.settings.write_service_url}/write/txt2"
            res = await session.post(url, headers={"Content-Type": "application/json"}, json=payload)
            res = await res.json()

        await asyncio.sleep(req.delay_seconds)

        req_payload = payload | res

        async with aiohttp.ClientSession() as session:
            url = f"{self.settings.write_service_url}/write/txt1"
            await session.post(url, headers={"Content-Type": "application/json"}, json=req_payload)

        return {"asyncAnswer": "Ok"}
