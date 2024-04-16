from typing import Annotated

from fastapi import APIRouter
from fastapi import status, Depends

from schemas import Req, ReqLine
from write_service import WriteService
from writer.dependencies import get_write_service

write_router = APIRouter(prefix="/write")


@write_router.post("/txt1", status_code=status.HTTP_201_CREATED)
async def write_txt1(req: ReqLine, write_service: Annotated[WriteService, Depends(get_write_service)]) -> str:
    return write_service.write_txt1(req)


@write_router.post("/txt2", status_code=status.HTTP_201_CREATED)
async def write_txt2(
        req: Req,
        write_service: Annotated[WriteService, Depends(get_write_service)]
) -> dict[str, int]:
    return write_service.write_txt2(req)
