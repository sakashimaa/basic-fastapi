from pydantic_settings import BaseSettings
from pydantic import BaseModel


class RunConfig(BaseModel):
    host: str = "localhost"
    port: int = 8000


class DbConfig(BaseModel):
    db_url: str = "sqlite://db.sqlite3"


class ApiPrefix(BaseModel):
    api_prefix: str = "/api"


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    db: DbConfig = DbConfig()
    api: ApiPrefix = ApiPrefix()


settings = Settings()
