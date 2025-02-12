from flask_socketio import join_room

def create_boards_socket_api(socketio):
    print("Registering todo event listener")

    @socketio.on('board_subscribe', namespace="/boards")
    def handle_connect(data):
        id = data.get('id')
        join_room(id)

def emit_board_update(socketio, board_id, data):
    socketio.emit('board_update', data, to=str(board_id), namespace='/boards')