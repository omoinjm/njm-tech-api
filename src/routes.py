from flask import Blueprint
from src.controllers.crawler_controller import bash_cmd

# main blueprint to be registered with application
api = Blueprint('api', __name__)

# register user with api blueprint
api.register_blueprint(bash_cmd, url_prefix="/bash_cmd")