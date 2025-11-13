import logging
import sys

from flask import Flask

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def hello():
    logger.info("Health check endpoint called")
    return 'Hello World!', 200

@app.route('/health')
def health():
    logger.info("Health check endpoint called")
    return 'Healthy', 200

if __name__ == '__main__':
    logger.info("Starting Flask application")
    app.run(host='0.0.0.0', port=8080)
