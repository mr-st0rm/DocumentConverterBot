from environs import Env

env = Env()
env.read_env()


class BotData:
    bot_token: str = env.str("BOT_TOKEN")
    admins: list = env.list("ADMINS")


class DatabaseData:
    username: str = env.str("DB_USERNAME")
    password: str = env.str("DB_PASSWORD")
    host: str = env.str("DB_HOST")
    port: int = env.int("DB_PORT")
    database: str = env.str("DB_NAME")

    database_url: str = f"postgresql+asyncpg://{username}:{password}@{host}/{database}"
