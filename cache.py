import redis
import os
import marshal

class Cache():
    def __init__(self):
        self.redis_client = redis.Redis(
            host=os.environ.get('REDIS_HOST'), 
            port=os.environ.get('REDIS_PORT'), 
            db=0,
            socket_connect_timeout=5
        )

    def set_resource(self, resource_name, id, value):
        cache_key = self.get_cache_key(resource_name, id)
        marshalled_object = marshal.dumps(value)

        self.redis_client.set(cache_key, marshalled_object)

    def get_resource(self, resource_name, id):
        cache_key = self.get_cache_key(resource_name, id)
        cached_value = self.redis_client.get(cache_key)

        if cached_value:
            return marshal.loads(cached_value)
        return None

    def delete_resource(self, resource_name, id):
        self.redis_client.delete(self.get_cache_key(resource_name, id))

    def get_cache_key(self, resource_name, id):
        return resource_name + "_" + str(id)

cache_client = Cache()