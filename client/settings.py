from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra="allow")

    # ========== GATEWAY ==========
    GATEWAY_HOST: str
    GATEWAY_PORT: int

    # ========== CLIENT  ==========
    CONNECTION_COUNT: int
    CONNECTION_VALUE: int
    DELAY_RANGE: float

    @property
    def gateway_url(self):
        return f"http://{self.GATEWAY_HOST}:{self.GATEWAY_PORT}"


settings = Settings()
