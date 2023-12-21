from flask import Flask
import os
from src.config.config import Config
from dotenv import load_dotenv

# loading environment variables
load_dotenv()

# declaring flask application
app = Flask(__name__)

# calling the environment configuration
python_env = os.environ.get("PYTHON_ENV", "DEV")

if python_env == "DEV":
    config = Config().dev_config
elif python_env == "PROD":
    config = Config().production_config
else:
    raise ValueError("Invalid value for PYTHON_ENV")

# making our application to use dev env
app.env = config.ENV

# import api blueprint to register it with app
from src.routes import api
app.register_blueprint(api, url_prefix="/api")
