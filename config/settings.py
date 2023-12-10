from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_NAME: str = "app.db"
    DB_URL: str = f"sqlite+aiosqlite:///{DB_NAME}"


settings = Settings()
