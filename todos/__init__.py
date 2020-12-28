from todos.controller import create_todos_api

def create_todos_app(app, sessionmaker, socketio):
    todos_api = create_todos_api(sessionmaker, socketio)
    app.register_blueprint(todos_api)