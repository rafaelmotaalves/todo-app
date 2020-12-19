from flask import Flask, jsonify
from flask_cors import CORS

from todos.controller import todos_api
from exceptions import NotFoundException, ValidationException

app = Flask(__name__)
CORS(app)

app.register_blueprint(todos_api, url_prefix='/todos')

def handle_not_found(error):
    return jsonify(errors=[f'Resource "{error.resource_name}" with id "{error.id}" was not found.']), 404

def handle_validation_error(error):
    return jsonify(errors=[error.errors]), 400

app.register_error_handler(NotFoundException, handle_not_found)
app.register_error_handler(ValidationException, handle_validation_error)