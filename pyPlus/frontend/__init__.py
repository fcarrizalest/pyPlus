from functools import wraps

from . import assets
from .. import factory


def create_app(settings_override=None):
    app = factory.create_app(__name__, __path__, settings_override)
    assets.init_app(app)
    return app


def route(bp, *args, **kwargs):
    def decorator(f):
        @bp.route(*args, **kwargs)
        @wraps(f)
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)
        return f

    return decorator