import os
import logging
from flask import Flask
from ui import ui_blueprint

app = Flask(__name__)
app.register_blueprint(ui_blueprint)

if __name__ == '__main__':
    debug_env = os.environ.get('DEBUG', 'true').lower()
    debug_mode = debug_env == 'true'
    print(f"DEBUG environment variable: {debug_env}")

    if debug_mode:
        # Configure the root logger to DEBUG
        logging.basicConfig(level=logging.DEBUG)
        logger = logging.getLogger(__name__)
        logger.debug("Debug mode is ON")
    else:
        # Configure the root logger to INFO
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)
        logger.info("Running in production mode")
    
    # Optionally, adjust Flask's logger as well
    app.logger.setLevel(logging.DEBUG if debug_mode else logging.INFO)
    
    # Set Flask's debug mode
    app.debug = debug_mode
    
    # Run the app
    app.run(debug=debug_mode)
