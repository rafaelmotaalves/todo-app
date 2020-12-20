from flask import Blueprint, request, jsonify, g

from db import create_session
from exceptions import NotFoundException, ValidationException

from todos.model import Todo, StatusEnum
from todos.validators import CreateTodoSchema, UpdateTodoSchema

from boards.model import Board

todos_api = Blueprint('todos', __name__)

@todos_api.url_value_preprocessor
def add_board(endpoint, values):
    if 'board_id' in values:
        board_id = values.get('board_id')

        session = create_session()

        board = session.query(Board).filter(Board.id ==  board_id).one_or_none()
        if not board:
            raise NotFoundException(resource_name="Board", id=board_id)
        g.board = board
    
@todos_api.route('/boards/<int:board_id>/todos', methods=["GET"])
def get_todos(board_id):
    todos = g.board.todos

    return jsonify(list(todo.to_json() for todo in todos)), 200

@todos_api.route('/boards/<int:board_id>/todos', methods=["POST"])
def create_todo(board_id):
    inputs = CreateTodoSchema(request)
    if not inputs.validate():
        raise ValidationException(inputs.errors)

    title = request.json.get('title')
    description = request.json.get('description')
    session = create_session()

    td = Todo(
        title=title, 
        description=description,
        board_id=g.board.id
    )
    session.add(td)
    session.commit()

    return '', 204

@todos_api.route("/boards/<int:board_id>/todos/<int:id>", methods=["PUT"])
def update_todo(board_id, id):
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