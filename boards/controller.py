from flask import Blueprint, request, jsonify

from db import create_session
from boards.model import Board
from exceptions import NotFoundException, ValidationException

from boards.validators import CreateBoardSchema

boards_api = Blueprint("boards", __name__)

@boards_api.route('/boards/<int:id>', methods=['GET'])
def get_board(id):
    session = create_session()

    board = session.query(Board).filter(Board.id == id).one_or_none()
    if not board:
        raise NotFoundException("Board", id)

    return jsonify(board.to_json()), 200

@boards_api.route('/boards', methods=['GET'])
def get_boards():
    session = create_session()

    boards = session.query(Board).order_by(Board.id).all()
    return jsonify(list(board.to_json() for board in boards)), 200

@boards_api.route('/boards', methods=['POST'])
def create_board():
    inputs = CreateBoardSchema(request)
    if not inputs.validate():
        raise ValidationException(inputs.errors)

    title = request.json.get('title')

    session = create_session()
    board = Board(
        title=title
    )
    session.add(board)
    session.commit()    
    return '', 204

