from flask import Blueprint, render_template
import redis

from . import route
from ..forms import NewIssueForm

bp = Blueprint('index', __name__)

@route(bp, '/')
def index():
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.set('foo', 'bar')
    form = NewIssueForm()

    return render_template('index.html' , form = form)