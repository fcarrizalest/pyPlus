import os

from flask import Flask
import redis

from flaskext.kvsession import KVSessionExtension
from simplekv.memory.redisstore import RedisStore

from .helpers import register_blueprints
from .middleware import HTTPMethodOverrideMiddleware


from flask_wtf.csrf import CsrfProtect

def create_app(package_name, package_path, settings_override=None,
               register_security_blueprint=True):
    app = Flask(package_name, instance_relative_config=True)
    app.config.from_object('pyPlus.settings')
    app.config.from_pyfile('settings.cfg', silent=True)
    app.config.from_object(settings_override)
    CsrfProtect(app)
    register_blueprints(app, package_name, package_path)
    store = RedisStore(redis.StrictRedis())
    KVSessionExtension(store, app)


    app.wsgi_app = HTTPMethodOverrideMiddleware(app.wsgi_app)
    return app