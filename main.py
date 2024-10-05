from flask import Flask
from ui import ui_blueprint

app = Flask(__name__)
app.register_blueprint(ui_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
