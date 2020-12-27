from flask import Flask, jsonify, g
from flask_cors import CORS
from flask_socketio import SocketIO

from db import create_tables, create_sessionmaker

from exceptions import NotFoundException, ValidationException

from todos.controller import create_todos_api

from boards.controller import create_boards_api
from boards.events import create_boards_socket_api

create_tables()
sessionmaker = create_sessionmaker()

app = Flask(__name__)
app.debug = True
socketio = SocketIO(app, cors_allowed_origins='*')
CORS(app)

boards_api = create_boards_api(sessionmaker)
app.register_blueprint(boards_api)
create_boards_socket_api(socketio)

todos_api = create_todos_api(sessionmaker, socketio)
app.register_blueprint(todos_api)

def handle_not_found(error):
    return jsonify(errors=[f'Resource "{error.resource_name}" with id "{error.id}" was not found.']), 404

def handle_validation_error(error):
    return jsonify(errors=[error.errors]), 400

app.register_error_handler(NotFoundException, handle_not_found)
app.register_error_handler(ValidationException, handle_validation_error)

if __name__ == "__main__":
    socketio.run(app)