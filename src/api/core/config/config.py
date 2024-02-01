import os
from dotenv import load_dotenv
from flask_swagger_ui import get_swaggerui_blueprint
from src.api.core.config.dev_config import DevConfig
from src.api.core.config.production_config import ProductionConfig


class Config:
    def __init__(self):
        self.dev_config = DevConfig()
        self.production_config = ProductionConfig()

    def current_config(self):
        load_dotenv()

        # calling the environment configuration
        pyenv = os.environ.get("PYTHON_ENV")

        if pyenv == "DEV":
            return self.dev_config
        elif pyenv == "PROD":
            return self.production_config
        else:
            raise ValueError("Invalid value for PYTHON_ENV")

    def swagger_ui(self):
        SWAGGER_URL = "/api/docs"  # URL for exposing Swagger UI (without trailing '/')

        API_URL = (
            "/static/swagger.json"  # Our API url (can of course be a local resource)
        )

        return get_swaggerui_blueprint(
            SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
            API_URL,
            config={  # Swagger UI config overrides
                "app_name": "NJM Tech API"
            },
            # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
            #    'clientId': "your-client-id",
            #    'clientSecret': "your-client-secret-if-required",
            #    'realm': "your-realms",
            #    'appName': "your-app-name",
            #    'scopeSeparator': " ",
            #    'additionalQueryStringParams': {'test': "hello"}
            # }
        )
