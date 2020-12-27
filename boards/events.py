from flask_socketio import join_room

def create_event_listener(socketio):
    print("Registering todo event listener")

    @socketio.on('board_subscribe', namespace="/boards")
    def handle_connect(data):
        id = data.get('id')
        print("Registered to " + id)
        join_room(id)

def emit_board_update(socketio, board_id):
    socketio.emit('board_update', { 'id': board_id }, to=str(board_id), namespace='/boards')