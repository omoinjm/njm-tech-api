# src/__init__.py
from src.api.controllers import ApiController, blueprint_array

base = ApiController()

app = base.register_blueprint(blueprint_array)

config = base.config
