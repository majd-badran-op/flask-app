from flask import Flask
from .routes import register_routes
from .exceptions import register_error_handlers

app = Flask(__name__)

register_routes(app)
register_error_handlers(app)
