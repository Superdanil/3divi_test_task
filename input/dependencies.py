from service import InputService
from settings import settings


def get_input_service() -> InputService:
    return InputService(settings)
