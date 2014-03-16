'''
Created on 16/03/2014

@author: fcarrizalest
'''

from wtforms import TextField
from flask_wtf import Form
from wtforms.validators import DataRequired
from wtforms.validators import Optional
from ..services import issues

__all__ = ['NewIssueForm', 'UpdateIssueForm']


class IssuesFormMixin(object):

    def __init__(self, *args, **kwargs):
        super(IssuesFormMixin, self).__init__(*args, **kwargs)



class NewIssueForm(IssuesFormMixin, Form):
    name = TextField('Name', validators=[DataRequired()])
    description = TextField('Description', validators=[DataRequired()])
    order = TextField('order', validators=[DataRequired()])



class UpdateIssueForm(IssuesFormMixin, Form):
    name = TextField('Name', validators=[Optional()])
    description = TextField('Description', validators=[Optional()])
    order = TextField('Order', validators=[Optional()])

