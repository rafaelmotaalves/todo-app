from flask import Flask, jsonify
from flask_cors import CORS
from db import create_tables

from exceptions import NotFoundException, ValidationException

from todos.controller import todos_api
from boards.controller import boards_api

app = Flask(__name__)
CORS(app)

create_tables()
app.register_blueprint(todos_api)
app.register_blueprint(boards_api)


def handle_not_found(error):
    return jsonify(errors=[f'Resource "{error.resource_name}" with id "{error.id}" was not found.']), 404

def handle_validation_error(error):
    return jsonify(errors=[error.errors]), 400

app.register_error_handler(NotFoundException, handle_not_found)
app.register_error_handler(ValidationException, handle_validation_error)