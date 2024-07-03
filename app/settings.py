from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    storage: str = "FILE"
    cache: str = "redis"
    notification: str = "console"

    class Config:
        env_file = ".env"

settings = Settings()