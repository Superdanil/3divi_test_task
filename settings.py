from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra="allow")

    # ===== INPUT SERVICE =====
    INPUT_SERVICE_HOST: str  # = "127.0.0.1"
    INPUT_SERVICE_PORT: int = 8000

    # ===== HANDLE SERVICE =====
    HANDLE_SERVICE_HOST: str = "127.0.0.1"
    HANDLE_SERVICE_PORT: int = 8001
    HANDLE_SERVICE_URL: str = f"http://{HANDLE_SERVICE_HOST}:{HANDLE_SERVICE_PORT}"

    # ===== WRITE SERVICE =====
    WRITE_SERVICE_HOST: str = "127.0.0.1"
    WRITE_SERVICE_PORT: int = 8002
    WRITE_SERVICE_URL: str = f"http://{WRITE_SERVICE_HOST}:{WRITE_SERVICE_PORT}"
    TXT1_PATH: str = "logs/txt1.txt"
    TXT2_PATH: str = "logs/txt2.txt"

    # ===== CLIENT SERVICE =====
    CONNECTION_COUNT: int = 6
    CONNECTION_VALUE: int = 60
    DELAY_RANGE: float = 2

    @property
    def txt1_path(self):
        return Path(__file__).parent.resolve() / self.TXT1_PATH

    @property
    def txt2_path(self):
        return Path(__file__).parent.resolve() / self.TXT2_PATH

    @property
    def input_service_url(self):
        return f"http://{self.INPUT_SERVICE_HOST}:{self.INPUT_SERVICE_PORT}"

    @property
    def handle_service_url(self):
        return f"http://{self.HANDLE_SERVICE_HOST}:{self.HANDLE_SERVICE_PORT}"

    @property
    def write_service_url(self):
        return f"http://{self.WRITE_SERVICE_HOST}:{self.WRITE_SERVICE_PORT}"


settings = Settings()
