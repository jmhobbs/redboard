import json
from redis import Redis, from_url
from flask import g, request, Blueprint, current_app, render_template, redirect, url_for
from .stats import Memory, Connections


dashboard = Blueprint('redboard', __name__, template_folder='templates', static_folder='static')


@dashboard.before_request
def setup_redis_connection():
    if current_app.config.get('REDIS_URL'):
        g.redboard_redis_conn = from_url(current_app.config.get('REDIS_URL'))
    else:
        g.redboard_redis_conn = Redis(host=current_app.config.get('REDIS_HOST', 'localhost'),
                                      port=current_app.config.get('REDIS_PORT', 6379),
                                      password=current_app.config.get('REDIS_PASSWORD', None),
                                      db=current_app.config.get('REDIS_DB', 0))


@dashboard.route('/')
def index():
    keys = g.redboard_redis_conn.info()

    db_index = 0
    total_keys = 0
    while 1:
        try:
            total_keys += keys['db%d' % db_index]['keys']
            db_index += 1
        except KeyError:
            break

    keys['total_keys'] = total_keys
    keys['db_index'] = db_index

    try:
        memory_time, memory_values = zip(*Memory(g.redboard_redis_conn).get())
        keys['memory'] = json.dumps(map(lambda x: x / 1024, memory_values))
    except ValueError:
        pass

    try:
        connections_time, connections_values = zip(*Connections(g.redboard_redis_conn).get())
        keys['connections'] = json.dumps(connections_values)
    except ValueError:
        pass

    return render_template('index.html', page="index", **keys)


@dashboard.route('/info')
def info():
    info = g.redboard_redis_conn.info()
    return render_template('info.html', page="info", info=info)


@dashboard.route('/keys/')
@dashboard.route('/keys/<path:pattern>')
def keys(pattern=None):
    if not pattern:
        if request.args.get('pattern', None):
            return redirect(url_for('redboard.keys', pattern=request.args.get('pattern')))
    else:
        pattern = pattern.strip()
        if 0 == len(pattern):
            pattern = None

    keys = {"pattern": pattern}

    if pattern:
        keys["keys"] = g.redboard_redis_conn.keys(pattern)

    return render_template('keys.html', page="keys", **keys)


@dashboard.route('/key')
@dashboard.route('/key/<path:key>')
def key(key=None):
    if not key:
        if request.args.get('key', None):
            return redirect(url_for('redboard.key', key=request.args.get('key')))
        return redirect(url_for('redboard.keys'))

    key_type = g.redboard_redis_conn.type(key)
    keys = {"key": key, "type": key_type}
    if "string" == key_type:
        keys['value'] = g.redboard_redis_conn.get(key)
    elif "set" == key_type:
        keys['members'] = g.redboard_redis_conn.smembers(key)
    elif "hash" == key_type:
        keys['fields'] = g.redboard_redis_conn.hgetall(key)
    elif "list" == key_type:
        keys['values'] = g.redboard_redis_conn.lrange(key, 0, -1)
    elif "zset" == key_type:
        keys['members'] = g.redboard_redis_conn.zrange(key, 0, -1, withscores=True)

    return render_template('key/%s.html' % key_type, page="keys", **keys)
