from functools import lru_cache

from pydantic import AliasChoices, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    MODEL_NAME: str = "llama-3.1-8b-instant"
    GROQ_API_KEY: str
    TAVILY_API_KEY: str
    APP_NAME: str
    DEBUG_MODE: bool
    MONGO_URI: str
    DATABASE_NAME: str
    SECERET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    HF_TOKEN: str | None = Field(
        default=None,
        validation_alias=AliasChoices("HF_TOKEN", "hf_token"),
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = Settings()