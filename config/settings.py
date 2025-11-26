from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Starter AI Service"

settings = Settings()
