from os import environ
from redis import Redis, from_url
from redboard.stats import Memory, Connections
from time import sleep

redis = None
if environ.get('REDIS_URL'):
    redis = from_url(environ.get('REDIS_URL'))
else:
    redis = Redis(host=environ.get('REDIS_HOST', 'localhost'),
                  port=environ.get('REDIS_PORT', 6379),
                  password=environ.get('REDIS_PASSWORD', None),
                  db=environ.get('REDIS_DB', 0))

memory = Memory(redis)
connections = Connections(redis)

while 1:
    try:
        info = redis.info()
        memory.update(info['used_memory'])
        connections.update(info['connected_clients'])
        sleep(1)
    except KeyboardInterrupt:
        print "Stopping..."
        break
