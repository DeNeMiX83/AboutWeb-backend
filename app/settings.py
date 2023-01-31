import os
from pydantic import BaseSettings, Field
from dataclasses import dataclass




# @dataclass
# class PostgresSettings(BaseSettings):
#     host: str = os.getenv('POSTGRES_HOST')
#     port: int = os.getenv('POSTGRES_PORT')
#     user: str = os.getenv('POSTGRES_USER')
#     password: str = os.getenv('POSTGRES_PASSWORD')
#     database: str = os.getenv('POSTGRES_DB')

#     def dsn(self) -> str:
#         return "{scheme}://{user}:{password}@{host}/{db}".format(
#             scheme="postgresql+asyncpg",
#             user=self.user,
#             password=self.password,
#             host=self.host,
#             db=self.database,
#         )

class PostgresSettings(BaseSettings):
    host: str = Field(..., env='POSTGRES_HOST')
    port: int = Field(..., env='POSTGRES_PORT')
    user: str = Field(..., env='POSTGRES_USER')
    password: str = Field(..., env='POSTGRES_PASSWORD')
    database: str = Field(..., env='POSTGRES_DB')

    def dsn(self) -> str:
        return "{scheme}://{user}:{password}@{host}/{db}".format(
            scheme="postgresql+asyncpg",
            user=self.user,
            password=self.password,
            host=self.host,
            db=self.database,
        )

    class Config:
        env_file = 'deploy/.env'
