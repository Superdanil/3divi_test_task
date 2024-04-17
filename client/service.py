import asyncio
from datetime import datetime
from random import uniform

import aiohttp
from fastapi.encoders import jsonable_encoder
from settings import settings


class ClientService:

    def __init__(self, pid: int, request_count: int, delay_range: float):
        self.pid = pid
        self.request_count = request_count
        self.delay_range = delay_range

    async def _send_request_pool(self):
        """Метод отправки запроса сервису-приёмщику"""

        async with aiohttp.ClientSession() as session:
            requests = [self._send_request(session, self._get_params(self.pid, request_id)) for request_id in
                        range(self.request_count)]
            await asyncio.gather(*requests)

    def _get_params(self, pid: int, request_id: int) -> dict:
        """Возвращает словарь параметров для HTTP-запроса."""

        id_ = f"{pid}_{request_id}"
        delay = round(uniform(0.1, self.delay_range), 2)
        params = {'request_id': id_, 'delay_seconds': delay, "time": datetime.now()}

        return params

    async def _send_request(self, session, params):
        self._write_log(params)
        payload = jsonable_encoder(params)
        async with session.post(settings.input_service_url,
                                headers={"Content-Type": "application/json"},
                                json=payload) as result:
            return result

    @staticmethod
    def _write_log(params):
        """Метод записи лога."""

        with open("log.txt", "a", encoding="utf-8") as file:
            file.write(
                datetime.now().strftime("%H:%M:%S:%f") + " | " + f"{params["request_id"]}".center(
                    7) + f" | {params}\n")
        return file

    async def start(self):
        loop_task = asyncio.create_task(self._send_request_pool())
        await asyncio.wait([loop_task])
