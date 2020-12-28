from todos.controller import create_todos_api

def create_todos_app(app, sessionmaker, socketio, cache_client):
    todos_api = create_todos_api(sessionmaker, socketio, cache_client)
    app.register_blueprint(todos_api)