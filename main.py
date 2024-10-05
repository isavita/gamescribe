import os
import logging
from flask import Flask
from ui import ui_blueprint

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.register_blueprint(ui_blueprint)

if __name__ == '__main__':
    debug_mode = os.environ.get('DEBUG', 'false').lower() == 'true'
    
    if debug_mode:
        logger.setLevel(logging.DEBUG)
        logger.debug("Debug mode is ON")
    
    app.run(debug=debug_mode)
