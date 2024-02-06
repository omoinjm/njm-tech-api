import os
from dotenv import load_dotenv


class DevConfig:
    # loading environment variables
    load_dotenv()

    def __init__(self):
        self.ENV = "development"
        self.DEBUG = True
        self.PORT = 5000
        self.HOST = "0.0.0.0"
        self.PYTHON_ENV = os.getenv("PYTHON_ENV")
        self.META_API_TOKEN = os.getenv("METAAPI_TOKEN")
        self.FLASK_SWAGGER_UI = os.getenv("FLASK_SWAGGER_UI")
        self.META_API_ACCOUNT_ID = os.getenv("METAAPI_ACCOUNT_ID")
