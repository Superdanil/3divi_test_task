from datetime import datetime

import uvicorn
from fastapi import FastAPI, status

from schemas import Req, ReqLine

app = FastAPI(title="Сервис записи")


@app.post("/txt1", status_code=status.HTTP_201_CREATED)
async def write_txt1(req: ReqLine) -> str:
    str_ = f"| {req.request_id} | {req.time} | {datetime.now()} |\n"
    with open("txt1.txt", "r") as f:
        contents = f.readlines()

    contents_length = len(contents)

    if contents_length > req.line_number:
        contents[req.line_number - 1] = str_
    else:
        delta = req.line_number - contents_length
        appending_strings = ["\n" for _ in range(delta - 1)]
        appending_strings.append(str_)
        contents.extend(appending_strings)
    with open("txt1.txt", "w", encoding="utf-8") as file:
        file.writelines(contents)
    return str_


@app.post("/txt2", status_code=status.HTTP_201_CREATED)
async def write_txt2(req: Req) -> dict:
    with open("txt2.txt", "a", encoding="utf-8") as file:
        str_ = f"| {req.request_id} | {req.time} |\n"
        file.write(str_)
    with open("txt2.txt", "rb") as f:
        num_lines = sum(1 for _ in f)
    return {"line_number": num_lines}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8002, log_level="info", reload=True)
