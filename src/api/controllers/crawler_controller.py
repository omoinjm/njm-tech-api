from flask import jsonify, Blueprint
from src.api.controllers.api_controller import ApiController

crawler = Blueprint("crawler", __name__)


class CrawlerController(ApiController):
    def __init__(self):
        super(CrawlerController, self).__init__()

    @crawler.route("/get", methods=["GET"])
    def get():
        # Logic for handling the GET request
        return jsonify({"message": "This is the GET endpoint"})


# @bash_cmd.route("/crawler", methods=["POST"])
# def handle_crawler():
#    try:
#        # first validate required use parameters
#        data = request.json
#
#        if "url" in data:
#            service_data = Crawler(data["url"]).run_command()
#
#            return Response(
#                response=json.dumps(
#                    {
#                        "status": "success",
#                        "message": "Data Loaded",
#                        "payload": service_data,
#                        "iat": datetime.utcnow(),
#                    }
#                ),
#                status=201,
#                mimetype="application/json",
#            )
#        else:
#            # if request parameters are not correct
#            return Response(
#                response=json.dumps(
#                    {
#                        "status": "failed",
#                        "message": "URI is required",
#                        "payload": "",
#                        "iat": datetime.utcnow(),
#                    }
#                ),
#                status=400,
#                mimetype="application/json",
#            )
#
#    except Exception as e:
#        return Response(
#            response=json.dumps(
#                {
#                    "status": "failed",
#                    "message": "Error Occured",
#                    "error": str(e),
#                    "iat": datetime.utcnow(),
#                }
#            ),
#            status=500,
#            mimetype="application/json",
#        )
#
#
# @bash_cmd.route("/health_check", methods=["GET"])
# def handle_check():
#    try:
#        return Response(
#            response=json.dumps(
#                {
#                    "status": "success",
#                    "message": "Data Loaded",
#                    "payload": "Wasup??",
#                    "iat": datetime.utcnow(),
#                }
#            ),
#            status=201,
#            mimetype="application/json",
#        )
#    except Exception as e:
#        return Response(
#            response=json.dumps(
#                {
#                    "status": "failed",
#                    "message": "Error Occured",
#                    "error": str(e),
#                    "iat": datetime.utcnow(),
#                }
#            ),
#            status=500,
#            mimetype="application/json",
#        )
#
#
# @bash_cmd.route("/install", methods=["POST"])
# def handle_install():
#    try:
#        # first validate required use parameters
#        data = request.json
#
#        if "app" in data:
#            service_data = Crawler().install_command(data["app"])
#
#            return Response(
#                response=json.dumps(
#                    {
#                        "status": "success",
#                        "message": "Data Loaded",
#                        "payload": service_data,
#                        "iat": datetime.utcnow(),
#                    }
#                ),
#                status=201,
#                mimetype="application/json",
#            )
#        else:
#            # if request parameters are not correct
#            return Response(
#                response=json.dumps(
#                    {
#                        "status": "failed",
#                        "message": "URI is required",
#                        "payload": "",
#                        "iat": datetime.utcnow(),
#                    }
#                ),
#                status=400,
#                mimetype="application/json",
#            )
#
#    except Exception as e:
#        return Response(
#            response=json.dumps(
#                {
#                    "status": "failed",
#                    "message": "Error Occured",
#                    "error": str(e),
#                    "iat": datetime.utcnow(),
#                }
#            ),
#            status=500,
#            mimetype="application/json",
#        )
#

