from datetime import datetime

import uvicorn
from fastapi import FastAPI, status

from schemas import Req

app = FastAPI(title="Сервис записи")


@app.post("/txt1", status_code=status.HTTP_201_CREATED)
async def write_txt1(req: Req) -> str:
    with open("txt1.txt", "a", encoding="utf-8") as file:
        str_ = f"| {req.request_id} | {req.time} | {datetime.now()} |\n"
        file.write(str_)
    return str_


@app.post("/txt2", status_code=status.HTTP_201_CREATED)
async def write_txt2(req: Req) -> str:
    with open("txt2.txt", "a", encoding="utf-8") as file:
        str_ = f"| {req.request_id} | {req.time} |\n"
        file.write(str_)
    return str_


if __name__ == "__main__":
    uvicorn.run("main:app", port=8002, log_level="info", reload=True)
