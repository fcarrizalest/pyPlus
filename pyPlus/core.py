from apiclient import errors
from apiclient.discovery import build
from apiclient.http import MediaFileUpload
import httplib2
from oauth2client.client import SignedJwtAssertionCredentials
import redis


r = redis.StrictRedis(host='localhost', port=6379, db=0)

class Service(object):

    __model__ = None

    def _preprocess_params(self, kwargs):
        """Returns a preprocessed dictionary of parameters. Used by default
        before creating a new instance or updating an existing instance.

        :param kwargs: a dictionary of parameters
        """
        kwargs.pop('csrf_token', None)
        return kwargs

    def _isinstance(self, model, raise_error=True):
        """Checks if the specified model instance matches the service's model.
        By default this method will raise a `ValueError` if the model is not the
        expected type.

        :param model: the model instance to check
        :param raise_error: flag to raise an error on a mismatch
        """
        rv = isinstance(model, self.__model__)
        if not rv and raise_error:
            raise ValueError('%s is not of type %s' % (model, self.__model__))
        return rv


    def save(self, model ):
        print "entramos a save"
        print model
        self._isinstance(model)
        model.save()


    def all(self):

        return self.__model__.all()


    def get(self , id):

        return self.__model__.get(id)


    def update(self, model, **kwargs):

        self._isinstance(model)
        for k, v in self._preprocess_params(kwargs).items():
            setattr(model, k, v)
        model.update()
        return model


    def delete(self , model):
        self._isinstance(model)
        model.delete()


    def create(self,**kwargs):
        return self.save(self.new(**kwargs))

    def new(self, **kwargs):
        """Returns a new, unsaved instance of the service's model class.

        :param **kwargs: instance parameters
        """
        return self.__model__.new(**self._preprocess_params(kwargs))