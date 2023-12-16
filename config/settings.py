from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    TITLE: str = "Shovelog Backend API"
    DESCRIPTION: str = "Backend API for Shovelog."

    DB_URL: str
    ECHO_SQL: bool

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
