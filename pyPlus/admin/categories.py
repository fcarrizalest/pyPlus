from flask import Blueprint, request

from . import route
from ..services import categories
from ..forms import NewCategoryForm, UpdateCategoryForm

bp = Blueprint('categories', __name__, url_prefix='/categories')


@route(bp, '/')
def list():
    """Returns a list of product instances."""
    return categories.all()


@route(bp, '/', methods=['POST'])
def create():
    """Creates a new product. Returns the new product instance."""
    form = NewCategoryForm()
    print form.validate_on_submit()
    if form.validate_on_submit():
        print "Adrea"
        print request.form.to_dict()
        return categories.create(**request.form.to_dict())

@route(bp, '/<issue_id>', methods=['PUT'])
def update(issue_id):
    """Updates a product. Returns the updated product instance."""

    print "vv"

    form = UpdateCategoryForm(csrf_enabled=False)

    print form.validate_on_submit()
    if form.validate_on_submit():
        return categories.update(categories.get(issue_id), **request.json)



@route(bp, '/<issue_id>', methods=['GET'])
def show(issue_id):
    """Returns a product instance."""
    print "vvaaaa"
    return categories.get(issue_id)


@route(bp, '/<issue_id>', methods=['DELETE'])
def delete(issue_id):
    """Deletes a product. Returns a 204 response."""
    categories.delete(categories.get(issue_id))
    return None, 204