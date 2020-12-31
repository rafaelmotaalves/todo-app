import os
import eventlet
from werkzeug.middleware.dispatcher import DispatcherMiddleware


from flask import Flask, jsonify, g
from flask_cors import CORS
from flask_socketio import SocketIO

from db import create_tables, create_sessionmaker

from exceptions import NotFoundException, ValidationException

from boards import create_boards_app
from todos import create_todos_app
from health import create_health_check_api
from metrics import create_metrics

from cache import cache_client

create_tables()
sessionmaker = create_sessionmaker()

app = Flask(__name__)

eventlet.monkey_patch() # this is needed so SocketIO will work with Redis
socketio = SocketIO(
    app,
    cors_allowed_origins='*', 
    message_queue="redis://" + os.environ.get('REDIS_HOST')
)
CORS(app)

create_boards_app(app, sessionmaker, socketio)
create_todos_app(app, sessionmaker, socketio, cache_client)
app.register_blueprint(create_health_check_api(sessionmaker, socketio, cache_client))

def handle_not_found(error):
    return jsonify(errors=[f'Resource "{error.resource_name}" with id "{error.id}" was not found.']), 404

def handle_validation_error(error):
    return jsonify(errors=[error.errors]), 400

app.register_error_handler(NotFoundException, handle_not_found)
app.register_error_handler(ValidationException, handle_validation_error)

if __name__ == "__main__":
    app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
        '/metrics': create_metrics(app, socketio)
    })
    socketio.run(app, host='0.0.0.0')