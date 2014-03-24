import os
from flask import Blueprint, request
from werkzeug import secure_filename
from . import route
from ..forms import FileForm,NewObjectForm
from ..settings import FILESTORETMP
from ..services import objects
bp = Blueprint('objects', __name__, url_prefix='/objects')

@route(bp, '/')
def list():
    """Returns a list of product instances."""
    return objects.all()

@route(bp, '/', methods=['POST'])
def create():
    """Creates a new product. Returns the new product instance."""
    print "antes de validar"
    print request.args.get('name', '')
    form = NewObjectForm()
    print form.validate_on_submit()
    print "Entramos a create"
    if form.validate_on_submit():
        
        print "Todo correcto"
        print request.json
        
        return objects.create(**request.json)



@route(bp, '/upload/' , methods=['POST'])
def upload():
    form = FileForm()
    if form.validate_on_submit():
        print "es valido"
        print form.file
        filed = request.files['file']
        print request.files['file']
        filename = secure_filename(filed.filename)
        filed.save(os.path.join( FILESTORETMP ,filename))