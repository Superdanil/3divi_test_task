import random
import threading
from threading import Thread
from typing import List
import asyncio
import requests
from requests import Session

from client.logger import logger
from client.config import settings
from pydantic import BaseModel, Field
from fastapi import (
    status,
    APIRouter,
    Response
)

router = APIRouter(tags=["tasks"], prefix="/tasks")


class Task(BaseModel):
    id: int
    delay: float = Field(ge=0)


class TasksData(BaseModel):
    connection_count: int = Field(ge=0)
    connection_value: int = Field(ge=0)
    delay_range: float = Field(ge=0)


class TaskResponse(BaseModel):
    asyncAnswer: str = Field(default="ok")


async def sendTask(task: Task, session: Session) -> None:
    request = requests.Request('POST', settings.RECEIVER_URL, json=task.model_dump())
    prepared_request = request.prepare()
    session.send(prepared_request)
    logger.info(f"Send task {task.model_dump_json()}. "
                f"Thread: {threading.current_thread().name} "
                f"Request: {prepared_request.method} url: {prepared_request.url} - "
                f"headers: {prepared_request.headers} body: {prepared_request.body}")


def startTasks(value: int, delayRange: int) -> None:
    session = requests.Session()
    for i in range(value):
        asyncio.run(sendTask(Task(id=i, delay=random.randint(0, delayRange)), session))


@router.post("/setTask")
async def setTask(tasks: TasksData) -> Response:
    threads: List[Thread] = []
    taskPerThread = tasks.connection_value // tasks.connection_count
    for i in range(tasks.connection_count):
        thread = Thread(target=startTasks, args=(taskPerThread, tasks.delay_range,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    return Response(status_code=status.HTTP_201_CREATED, content=TaskResponse().model_dump_json())
