from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from .config import config_by_name

db = SQLAlchemy()
flask_bcrypt = Bcrypt()


def create_server(config_name):

    # Configure Server
    server = Flask(__name__)
    server.config.from_object(config_by_name[config_name])

    # Initialize DB
    db.init_app(server)

    # Initialize Encryption
    flask_bcrypt.init_app(server)

    return server
