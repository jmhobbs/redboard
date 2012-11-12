import time


class Series (object):

    name = 'series'
    seconds = 60

    def __init__(self, redis):
        self.redis = redis

    def update(self, value, now=None):
        if not now:
            now = int(time.time())
        score = "%d.%d" % (now, value)
        self.redis.zadd('redboard:%s' % self.name, score, now)
        self.redis.zremrangebyrank('redboard:%s' % self.name, 0, -1 * self.seconds)

    def get(self):
        return tuple(map(lambda x: tuple(map(int, x[0].split('.'))), self.redis.zrangebyscore('redboard:%s' % self.name, int(time.time()) - self.seconds, '+inf', withscores=True)))


class Memory (Series):
    name = 'memory'


class Connections (Series):
    name = 'connections'
