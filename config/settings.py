from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_name: str = "app.db"
    db_url: str = f"sqlite+aiosqlite:///{db_name}"


settings = Settings()
