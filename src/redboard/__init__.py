# Modules/blueprints
from .dashboard import dashboard


class RedBoard(object):
    def __init__(self, app, url_prefix='/redboard'):
        self.init_app(app, url_prefix)

    def init_app(self, app, url_prefix='/redboard'):
        app.register_blueprint(dashboard, url_prefix=url_prefix)
