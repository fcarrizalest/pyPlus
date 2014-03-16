from ..core import Service
from .models import Issue



class IssuesService(Service):
    __model__ = Issue
    def __init__(self, *args, **kwargs):
        super(IssuesService, self).__init__(*args, **kwargs)

    def _preprocess_params(self, kwargs):
        kwargs = super(IssuesService, self)._preprocess_params(kwargs)
        return kwargs