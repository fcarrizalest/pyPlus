from functools import wraps

from flask import jsonify

from .. import factory
from ..helpers import JSONEncoder


def create_app(settings_override=None, register_security_blueprint=False):
    app = factory.create_app(__name__, __path__, settings_override,
                             register_security_blueprint=register_security_blueprint)
    app.json_encoder = JSONEncoder
    return app


def route(bp, *args, **kwargs):
    kwargs.setdefault('strict_slashes', False)
    print "antes route"
    print  args
    print "an rou"
    print kwargs

    def decorator(f):
        @bp.route(*args, **kwargs)
        @wraps(f)
        def wrapper(*args, **kwargs):
            sc = 200
            print "argumeno"
            print args
            print "o"
            print kwargs
            rv = f(*args, **kwargs)
            print "decorador"
            print rv
            if isinstance(rv, tuple):
                sc = rv[1]
                rv = rv[0]
            return jsonify(dict(data=rv)), sc
        return f

    return decorator