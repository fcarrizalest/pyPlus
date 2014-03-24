
from flask_wtf.file import FileField
from flask_wtf import Form
from wtforms.validators import DataRequired
from wtforms.validators import Optional
from wtforms import TextField


__all__ = ['FileForm', 'NewObjectForm']

class ObjectsFormMixin(object):

    def __init__(self, *args, **kwargs):
        super(ObjectsFormMixin, self).__init__(*args, **kwargs)


class FileForm(Form):
    file = FileField('file')
    
class NewObjectForm(ObjectsFormMixin,Form):
    name = TextField('Name', validators=[DataRequired()])
    description = TextField('Description', validators=[DataRequired()])
    _typeO = TextField('_typeO', validators=[DataRequired()])
    issue = TextField('Issue', validators=[DataRequired()])
    category = TextField('Category', validators=[DataRequired()])
    path = TextField('Path', validators=[Optional()])