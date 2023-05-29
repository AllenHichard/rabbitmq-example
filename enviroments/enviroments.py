import os
from dotenv import load_dotenv


class Enviroments:
    def __init__(self):
        load_dotenv()
        self.bootstrap_servers = os.getenv('BOOTSTRAP_SERVERS')
