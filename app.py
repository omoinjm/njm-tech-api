import logging
from src import config, app
from gevent.pywsgi import WSGIServer

# Set up logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    if config.ENV == "production":
        http_server = WSGIServer(('', config.PORT), app)
        http_server.serve_forever()
    else:
        # Debug/Development
        app.run(host= config.HOST,
                port= config.PORT,
                debug= config.DEBUG)
