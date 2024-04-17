from service import HandleService
from settings import settings


def get_handle_service() -> HandleService:
    return HandleService(settings)
