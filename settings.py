from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra="allow")

    # ========== GATEWAY ==========
    GATEWAY_HOST: str
    GATEWAY_PORT: int

    # ========== HANDLER ==========
    HANDLE_SERVICE_HOST: str
    HANDLE_SERVICE_PORT: int

    # ========== WRITER ==========
    WRITE_SERVICE_HOST: str
    WRITE_SERVICE_PORT: int
    TXT1_PATH: str = "writer/logs/txt1.txt"
    TXT2_PATH: str = "writer/logs/txt2.txt"

    @property
    def input_service_url(self):
        return f"http://{self.GATEWAY_HOST}:{self.GATEWAY_PORT}"

    @property
    def handle_service_url(self):
        return f"http://{self.HANDLE_SERVICE_HOST}:{self.HANDLE_SERVICE_PORT}"

    @property
    def write_service_url(self):
        return f"http://{self.WRITE_SERVICE_HOST}:{self.WRITE_SERVICE_PORT}"


settings = Settings()
