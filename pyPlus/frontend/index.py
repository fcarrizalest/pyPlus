import redis
from flask import Blueprint, render_template

from . import route


bp = Blueprint('index', __name__)

@route(bp, '/')
def index():
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.set('foo', 'bar')

    return render_template('index.html')