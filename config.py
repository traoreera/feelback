import deps
from dotenv import load_dotenv, find_dotenv

load_dotenv(dotenv_path="./plugins/feelback/.env")


class MQTTConfig:
    BROKER_URL = deps.os.getenv("BROKER_URL")
    USERNAME = deps.os.getenv("USERNAME")
    PASSWORD = deps.os.getenv("PASSWORD")
    BROKER_PORT = 8883
