from flask import Flask
from .routes import register_routes
from .exceptions import register_error_handlers
from .routes import setup_cors

app = Flask(__name__)

setup_cors(app)
register_routes(app)
register_error_handlers(app)

if __name__ == '__main__':
    app.run(debug=True)
