from pydantic_settings import BaseSettings
from pydantic import BaseModel


class RunConfig(BaseModel):
    host: str = "localhost"
    port: int = 8000


class DbConfig(BaseModel):
    db_user: str = "postgres"
    db_host: str = "localhost"
    db_port: int = 5432
    db_password: str = "qwerty123"
    db_name: str = "shop"


class ApiPrefix(BaseModel):
    api_prefix: str = "/api"


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    db: DbConfig = DbConfig()
    api: ApiPrefix = ApiPrefix()


settings = Settings()
