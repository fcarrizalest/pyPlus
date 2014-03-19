'''
Created on 16/03/2014

@author: fcarrizalest
'''

from wtforms import TextField
from flask_wtf import Form
from wtforms.validators import DataRequired
from wtforms.validators import Optional
from ..services import issues

__all__ = ['NewCategoryForm', 'UpdateCategoryForm']


class CategoryFormMixin(object):

    def __init__(self, *args, **kwargs):
        super(CategoryFormMixin, self).__init__(*args, **kwargs)



class NewCategoryForm(CategoryFormMixin, Form):
    name = TextField('Name', validators=[DataRequired()])
    description = TextField('Description', validators=[DataRequired()])
    order = TextField('order', validators=[DataRequired()])




class UpdateCategoryForm(CategoryFormMixin, Form):
    name = TextField('Name', validators=[Optional()])
    description = TextField('Description', validators=[Optional()])
    order = TextField('Order', validators=[Optional()])

