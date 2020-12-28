from flask import Blueprint, request, jsonify, g

from boards.model import Board
from exceptions import NotFoundException, ValidationException

from boards.validators import CreateBoardSchema

def create_boards_api(sessionmaker):
    boards_api = Blueprint("boards", __name__)

    @boards_api.before_request
    def create_session():
        g.session = sessionmaker()
    
    @boards_api.teardown_request
    def close_session(ctx):
        g.session.close()

    @boards_api.route('/boards/<int:id>', methods=['GET'])
    def get_board(id):
        board = g.session.query(Board).filter(Board.id == id).one_or_none()
        if not board:
            raise NotFoundException("Board", id)

        return jsonify(board.to_json()), 200

    @boards_api.route('/boards', methods=['GET'])
    def get_boards():
        boards = g.session.query(Board).order_by(Board.id).all()
        return jsonify(list(board.to_json() for board in boards)), 200

    @boards_api.route('/boards', methods=['POST'])
    def create_board():
        inputs = CreateBoardSchema(request)
        if not inputs.validate():
            raise ValidationException(inputs.errors)

        title = request.json.get('title')

        board = Board(
            title=title
        )
        g.session.add(board)
        g.session.commit()    
        
        return jsonify(board.to_json()), 200

    return boards_api

