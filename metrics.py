from prometheus_client import Summary, Gauge, Counter, Enum, make_wsgi_app
from flask import g, request
import time


ACTIVE_WEBSOCKETS = Gauge('active_websockets', 'Total Active sockets')
REQUEST_LATENCY = Summary('request_latency_milliseconds', "Request latency", labelnames=['method', 'path'])
ERROR_500_COUNTER = Counter('internal_error_counter', 'Count of internal server error responses', labelnames=['method', 'path'])

def current_millis():
    return int(round(time.time() * 1000))

def create_metrics(app, socketio):

    @app.before_request
    def before_all():
        g.begin_timestamp = current_millis()

    @app.after_request
    def after_all(response):            
        if 'begin_timestamp' in g:
            REQUEST_LATENCY.labels(method=request.method, path=request.url_rule.rule).observe(current_millis() - g.begin_timestamp)
        
        return response

    @app.errorhandler(500)
    def internal_server_error_handler(error):
        ERROR_500_COUNTER.labels(method=request.method, path=request.url_rule.rule).inc()
        return error

    @socketio.on('connect',namespace="/boards")
    def connect():
        ACTIVE_WEBSOCKETS.inc()
    
    @socketio.on('disconnect', namespace="/boards")
    def disconnect():
        ACTIVE_WEBSOCKETS.dec()

    return make_wsgi_app()