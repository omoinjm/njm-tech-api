from flask import Flask, Blueprint
from src.api.core.config.config import Config


class ApiController:
    def __init__(self):
        self.app = Flask(__name__)

        self.api = Blueprint("api", __name__)

        self.config = Config().current_config()

        self.app.config["ENV"] = self.config.ENV

        self.controller_name = self.__class__.__name__.replace("Controller", "").lower()

        super(ApiController, self).__init__()

    def register_blueprint(self, blueprint_array):
        for item in blueprint_array:
            instance = item["instance"]
            blueprint = item["blueprint"]
            controller_name = instance().controller_name
            self.api.register_blueprint(blueprint, url_prefix=controller_name)

        swagger_url = self.config.FLASK_SWAGGER_UI
        swagger_ui = Config().swagger_ui(swagger_url)

        self.app.register_blueprint(swagger_ui)
        self.app.register_blueprint(self.api, url_prefix="/api/v1/")

        return self.app

