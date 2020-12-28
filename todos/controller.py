from flask import Blueprint, request, jsonify, g

from db import sessionmaker
from exceptions import NotFoundException, ValidationException

from todos.model import Todo, StatusEnum
from todos.validators import CreateTodoSchema, UpdateTodoSchema

from boards.model import Board
from boards.events import emit_board_update

def create_todos_api(sessionmaker, socketio):
    todos_api = Blueprint('todos', __name__)

    @todos_api.url_value_preprocessor
    def add_board(endpoint, values):
        g.session = sessionmaker()

        if 'board_id' in values:
            board_id = values.get('board_id')

            board = g.session.query(Board).filter(Board.id ==  board_id).one_or_none()
            if not board:
                raise NotFoundException(resource_name="Board", id=board_id)
            g.board = board

    @todos_api.after_request
    def after_request(response):
        if request.method in ['POST', 'PUT']:
            emit_board_update(socketio, g.board.id, response.get_json())
        return response

    @todos_api.teardown_request
    def teardown(ctx):
        g.session.close()
        
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

        todo = Todo(
            title=title, 
            description=description,
            board_id=g.board.id
        )
        g.session.add(todo)
        g.session.commit()

        return jsonify(todo.to_json()), 200

    @todos_api.route("/boards/<int:board_id>/todos/<int:id>", methods=["PUT"])
    def update_todo(board_id, id):
        inputs = UpdateTodoSchema(request)
        if not inputs.validate():
            raise ValidationException(inputs.errors)

        title = request.json.get('title')
        description = request.json.get('description')
        status = request.json.get('status')

        todo = g.session.query(Todo).filter(Todo.id == id).one_or_none()
        if not todo:
            raise NotFoundException(resource_name="Todo", id=id)

        if title:
            todo.title = title
        if description:
            todo.description = description
        if status:
            todo.status = StatusEnum(status)
        
        g.session.commit()
        
        return jsonify(todo.to_json()), 200
    
    return todos_api