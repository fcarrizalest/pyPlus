from flask import Blueprint, request

from . import route
from ..services import issues
from ..forms import NewIssueForm, UpdateIssueForm

bp = Blueprint('issues', __name__, url_prefix='/issues')


@route(bp, '/')
def list():
    """Returns a list of product instances."""
    return issues.all()


@route(bp, '/', methods=['POST'])
def create():
    """Creates a new product. Returns the new product instance."""
    form = NewIssueForm()
    print form.validate_on_submit()
    if form.validate_on_submit():
        print "Adrea"
        print request.form.to_dict()
        return issues.create(**request.form.to_dict())




@route(bp, '/<issue_id>')
def show(issue_id):
    """Returns a product instance."""
    return issues.get(issue_id)


@route(bp, '/<issue_id>', methods=['DELETE'])
def delete(issue_id):
    """Deletes a product. Returns a 204 response."""
    issues.delete(issues.get(issue_id))
    return None, 204