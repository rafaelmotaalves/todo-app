from flask import Flask, jsonify, g
from flask_cors import CORS
from flask_socketio import SocketIO

from db import create_tables, create_sessionmaker

from exceptions import NotFoundException, ValidationException

from boards import create_boards_app
from todos import create_todos_app

create_tables()
sessionmaker = create_sessionmaker()

app = Flask(__name__)
app.debug = True
socketio = SocketIO(app, cors_allowed_origins='*')
CORS(app)

create_boards_app(app, sessionmaker, socketio)
create_todos_app(app, sessionmaker, socketio)

def handle_not_found(error):
    return jsonify(errors=[f'Resource "{error.resource_name}" with id "{error.id}" was not found.']), 404

def handle_validation_error(error):
    return jsonify(errors=[error.errors]), 400

app.register_error_handler(NotFoundException, handle_not_found)
app.register_error_handler(ValidationException, handle_validation_error)

if __name__ == "__main__":
    socketio.run(app)