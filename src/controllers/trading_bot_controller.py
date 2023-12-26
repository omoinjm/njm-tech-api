from flask import request, Response, json, Blueprint
from src.services.crawler_service import Crawler
from datetime import datetime

# trading bot controller blueprint to be registered with api blueprint
trading_bot = Blueprint("trading_bot", __name__)

entry_price = 0

# route for signup api/users/signup
@trading_bot.route('/alert', methods = ["POST"])
def process_alert():
    global entry_price

    # Read the body from request
    data = request.json

    if "type" in data and "ticker" in data and "close" in data:

        if data["type"] == "supertrend_buy":
            print("Buying %s for %s" % (data["ticker"], data["close"]))
            entry_price = int(data["close"])
        elif data["type"] == "supertrend_sell":
            print("Selling %s for %s" % (data["ticker"], data["close"]))
            pnl = int(data["close"]) - entry_price
            print("PNL : %d" % pnl)

    else:
        # if request parameters are not correct 
        return Response(
            response=json.dumps({
                "status": "failed", 
                "message": "URI is required",
                "payload": "",
                "iat": datetime.utcnow(),
            }),
            status=400,
            mimetype='application/json'
        )