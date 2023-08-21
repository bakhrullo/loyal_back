from dataclasses import dataclass

from environs import Env


@dataclass
class DbConfig:
    name: str
    user: str
    password: str
    host: str
    port: str


@dataclass
class Miscellaneous:
    secret_key: str


@dataclass
class Config:
    db: DbConfig
    misc: Miscellaneous


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        db=DbConfig(
            name=env.str("DB_NAME"),
            user=env.str("DB_USER"),
            password=env.str("DB_PASS"),
            host=env.str("DB_HOST"),
            port=env.str("DB_PORT"),
        ),
        misc=Miscellaneous(
            secret_key=env.str("SECRET_KEY")
        )
    )