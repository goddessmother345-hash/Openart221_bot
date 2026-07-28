import json
from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    BOT_TOKEN: str
    ADMIN_IDS: str = "[]"
    REQUIRED_CHANNEL_ID: str = ""
    REQUIRED_CHANNEL_URL: str = ""
    
    DATABASE_URL: str = "sqlite+aiosqlite:///./nexaptrade.db"
    
    GEMINI_API_KEY: str
    NEWS_API_KEY: str = ""
    TAAPI_SECRET: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    @property
    def admin_list(self) -> List[int]:
        try:
            return json.loads(self.ADMIN_IDS)
        except Exception:
            return []

settings = Settings()
