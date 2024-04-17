from service import WriteService
from settings import settings


def get_write_service() -> WriteService:
    return WriteService(settings)
