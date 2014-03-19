from ..core import Service
from .models import Category



class CategoriesService(Service):
    __model__ = Category
    def __init__(self, *args, **kwargs):
        super(CategoriesService, self).__init__(*args, **kwargs)

    def _preprocess_params(self, kwargs):
        kwargs = super(CategoriesService, self)._preprocess_params(kwargs)
        return kwargs