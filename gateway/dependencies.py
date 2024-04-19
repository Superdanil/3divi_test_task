from service import GatewayService
from settings import settings


def get_gateway() -> GatewayService:
    return GatewayService(settings)
