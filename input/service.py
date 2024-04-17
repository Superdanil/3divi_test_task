import aiohttp
from fastapi.encoders import jsonable_encoder

from schemas import Req
from settings import Settings


class InputService:
    """Класс приёма запросов от клиентов."""

    def __init__(self, settings: Settings):
        self.settings = settings

    async def handle_request(self, req: Req) -> str:
        """Перенаправляет запрос сервису-обработчику."""
        payload = jsonable_encoder(req)

        async with aiohttp.ClientSession() as session:
            await session.post(
                self.settings.handle_service_url,
                headers={"Content-Type": "application/json"},
                json=payload
            )
