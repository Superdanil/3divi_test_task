from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra="allow")

    # ===== INPUT SERVICE =====
    INPUT_SERVICE_HOST: str
    INPUT_SERVICE_PORT: int

    # ===== HANDLE SERVICE =====
    HANDLE_SERVICE_HOST: str
    HANDLE_SERVICE_PORT: int

    # ===== WRITE SERVICE =====
    WRITE_SERVICE_HOST: str
    WRITE_SERVICE_PORT: int
    TXT1_PATH: str = "writer/logs/txt1.txt"
    TXT2_PATH: str = "writer/logs/txt2.txt"

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
