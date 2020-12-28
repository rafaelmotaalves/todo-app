from boards.controller import create_boards_api
from boards.events import create_boards_socket_api

def create_boards_app(app, sessionmaker, socketio):
    boards_api = create_boards_api(sessionmaker)

    app.register_blueprint(boards_api)

    create_boards_socket_api(socketio)