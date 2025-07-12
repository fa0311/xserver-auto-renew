from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    id_vps: str = Field()

    def __init__(self):
        super().__init__()


class LoginSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    username: str = Field()
    password: str = Field()

    def __init__(self):
        super().__init__()
