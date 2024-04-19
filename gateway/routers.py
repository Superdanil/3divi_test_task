from typing import Annotated

from fastapi import APIRouter
from fastapi import status, Depends

from schemas import Req
from service import GatewayService
from dependencies import get_gateway

router = APIRouter()


@router.post("/", status_code=status.HTTP_200_OK)
async def input_request(req: Req, input_service: Annotated[GatewayService, Depends(get_gateway)]) -> dict[str, str]:
    await input_service.handle_request(req)

    return {"asyncAnswer": "Ok"}
