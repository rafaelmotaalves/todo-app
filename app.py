from flask import Flask, jsonify, g
from flask_cors import CORS
from flask_socketio import SocketIO

from db import create_tables

from exceptions import NotFoundException, ValidationException

from todos.controller import todos_api
from boards.controller import boards_api

from boards.events import create_event_listener

app = Flask(__name__)
app.debug = True
socketio = SocketIO(app, cors_allowed_origins='*')
CORS(app)

create_tables()
create_event_listener(socketio)

def add_socketio():
    g.socketio = socketio
app.before_request(add_socketio)

app.register_blueprint(todos_api)
app.register_blueprint(boards_api)
def handle_not_found(error):
    return jsonify(errors=[f'Resource "{error.resource_name}" with id "{error.id}" was not found.']), 404

def handle_validation_error(error):
    return jsonify(errors=[error.errors]), 400

app.register_error_handler(NotFoundException, handle_not_found)
app.register_error_handler(ValidationException, handle_validation_error)

if __name__ == "__main__":
    socketio.run(app)