from datetime import datetime

from pydantic import BaseModel


class Req(BaseModel):
    request_id: str
    delay_seconds: float
    time: datetime


class ReqLine(Req):
    line_number: int
