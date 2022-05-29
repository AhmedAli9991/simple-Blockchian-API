from pydantic import BaseSettings

class Settings(BaseSettings):
    access_key: str
    refresh_key: str
    algorithm: str
    access_expire: int
    refresh_expire: int
    path:str
    class Config:
        env_file = ".env"


settings = Settings()