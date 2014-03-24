from ..core import Service
from .models import Object



class ObjectsService(Service):
    __model__ = Object
    def __init__(self, *args, **kwargs):
        super(ObjectsService, self).__init__(*args, **kwargs)

    def _preprocess_params(self, kwargs):
        kwargs = super(ObjectsService, self)._preprocess_params(kwargs)
        return kwargs