from flask import Blueprint, request, jsonify

from db import create_session
from exceptions import NotFoundException, ValidationException

from todos.model import Todo, StatusEnum
from todos.validators import CreateTodoSchema, UpdateTodoSchema

todos_api = Blueprint('todos', __name__)

@todos_api.route('', methods=["GET"])
def get_todos():
    session = create_session()

    todos = session.query(Todo).order_by(Todo.title).all()
    return jsonify(list(todo.to_json() for todo in todos)), 200

@todos_api.route('', methods=["POST"])
def create_todo():
    inputs = CreateTodoSchema(request)
    if not inputs.validate():
        raise ValidationException(inputs.errors)

    title = request.json.get('title')
    description = request.json.get('description')

    session = create_session()
    td = Todo(
        title=title, 
        description=description
    )
    session.add(td)
    session.commit()

    return '', 204

@todos_api.route("/<int:id>", methods=["PUT"])
def update_todo(id):
    inputs = UpdateTodoSchema(request)
    if not inputs.validate():
        raise ValidationException(inputs.errors)

    title = request.json.get('title')
    description = request.json.get('description')
    status = request.json.get('status')

    session = create_session()
    todo = session.query(Todo).filter(Todo.id == id).one_or_none()
    if not todo:
        raise NotFoundException(resource_name="Todo", id=id)

    if title:
        todo.title = title
    if description:
        todo.description = description
    if status:
        todo.status = StatusEnum(status)
    
    session.commit()

    return '', 204