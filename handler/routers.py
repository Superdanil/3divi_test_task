from typing import Annotated

from fastapi import APIRouter
from fastapi import status, Depends

from schemas import Req
from service import HandleService
from .dependencies import get_handle_service

router = APIRouter()


@router.post("/", status_code=status.HTTP_200_OK)
async def write_txt1_and_txt2(
        req: Req,
        handle_service: Annotated[HandleService, Depends(get_handle_service)]
) -> dict[str, str]:
    return await handle_service.write_files(req)
