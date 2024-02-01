import os
from dotenv import load_dotenv

class ProductionConfig:
    # loading environment variables
    load_dotenv()
    
    def __init__(self):
        self.ENV = "production"
        self.DEBUG = False
        self.PORT = 3000
        self.HOST = '0.0.0.0'
        self.PYTHON_ENV = os.getenv("PYTHON_ENV")
        self.META_API_TOKEN = os.getenv('METAAPI_TOKEN')
        self.META_API_ACCOUNT_ID = os.getenv('METAAPI_ACCOUNT_ID')
        
