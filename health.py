from flask import Blueprint, jsonify

def create_health_check_api(sessionmaker, socketio, cache_client):
    health_api = Blueprint('healthcheck', __name__)

    def health_check_database():
        is_healthy = True

        try:
            session = sessionmaker()

            session.execute('SELECT 1')
        except Exception:
            is_healthy = False
        finally:
            session.close()

        return is_healthy
    
    def health_check_websockets():
        is_healthy = True

        try:
            socketio.emit('health_check')
        except Exception:
            is_healthy = False

        return is_healthy
    
    def health_check_redis():
        is_healthy = True

        try:
            cache_client.redis_client.ping()
        except Exception:
            is_healthy = False

        return is_healthy


    @health_api.route('/health', methods=['GET'])
    def health_check():
        health_object = {
            'db': health_check_database(),
            'sockets': health_check_websockets(),
            'cache': health_check_redis()
        }

        if False in health_object.values():
            return jsonify(success=False, info=health_object), 500

        return jsonify(success=True, info=health_object), 200

    return health_api