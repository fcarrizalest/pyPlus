import importlib
import pkgutil
import os
import os.path
from apiclient import errors
from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from flask import Blueprint
import httplib2
from oauth2client.client import SignedJwtAssertionCredentials
from pyPlus.settings import SERVICE_ACCOUNT_EMAIL, \
    SERVICE_ACCOUNT_PKCS12_FILE_PATH

from flask.json import JSONEncoder as BaseJSONEncoder


class DriveServices:
    service = None
    def __init__(self):
        self.service = self.createDriveServices()


    def createDriveServices(self ):
        current_dir =os.path.dirname(__file__)
        parent = os.path.join(current_dir, "../"+SERVICE_ACCOUNT_PKCS12_FILE_PATH) # construct a path to its parent

        f = file(parent, 'rb')
        key = f.read()
        f.close()

        credentials = SignedJwtAssertionCredentials(SERVICE_ACCOUNT_EMAIL, key,scope='https://www.googleapis.com/auth/drive')
        http = httplib2.Http()
        http = credentials.authorize(http)

        return build('drive', 'v2', http=http)
    def create_folder(self , title, description, parent_id ):
        body = {'title': title,'description': description,'mimeType': "application/vnd.google-apps.folder"}
        if parent_id:
            body['parents'] = [{'id': parent_id}]
        try:
            fileT = self.service.files().insert(body=body).execute()

            return fileT
        except errors.HttpError, error:
            print 'An error occured: %s' % error
        return None


    def insert_file(self , title, description, parent_id, mime_type, filename):

        media_body = MediaFileUpload(filename, mimetype=mime_type, resumable=True)
        body = {'title': title,'description': description,'mimeType': mime_type}
        if parent_id:
            body['parents'] = [{'id': parent_id}]
        try:
            fileT = self.service.files().insert(body=body,media_body=media_body).execute()

            return fileT
        except errors.HttpError, error:
            print 'An error occured: %s' % error
        return None



    def update_folder(self, file_id, new_title, new_description, new_revision = True):
        try:
            fileT = self.service.files().get(fileId=file_id).execute()
            # File's new metadata.
            fileT['title'] = new_title
            fileT['description'] = new_description
            fileT['mimeType'] = "application/vnd.google-apps.folder"
            # File's new content.

            # Send the request to the API.
            updated_file = self.service.files().update(fileId=file_id,body=fileT,newRevision=new_revision).execute()
            return updated_file
        except errors.HttpError, error:
            print 'An error occurred: %s' % error
        return None


    def update_file(self, file_id, new_title, new_description, new_mime_type, new_filename, new_revision):
        try:
            fileT = self.service.files().get(fileId=file_id).execute()
            # File's new metadata.
            fileT['title'] = new_title
            fileT['description'] = new_description
            fileT['mimeType'] = new_mime_type
            # File's new content.
            media_body = MediaFileUpload(new_filename, mimetype=new_mime_type, resumable=True)
            # Send the request to the API.
            updated_file = self.service.files().update(fileId=file_id,body=fileT,newRevision=new_revision,media_body=media_body).execute()
            return updated_file
        except errors.HttpError, error:
            print 'An error occurred: %s' % error
        return None


    def retrieve_all_files(self):
        result = []
        page_token = None
        while True:
            try:
                param = {}
                if page_token:
                    param['pageToken'] = page_token
                files = self.service.files().list(**param).execute()
                result.extend(files['items'])
                page_token = files.get('nextPageToken')
                if not page_token:
                    break
            except errors.HttpError, error:
                print 'An error occurred: %s' % error
                break
        return result


    def delete_file(self, file_id):
        try:
            self.service.files().delete(fileId=file_id).execute()
        except errors.HttpError, error:
            print 'An error occurred: %s' % error


    def print_files_in_folder(self, folder_id):
        page_token = None
        while True:
            try:
                param = {}
                if page_token:
                    param['pageToken'] = page_token
                    children = self.service.children().list(folderId=folder_id, **param).execute()
                    for child in children.get('items', []):
                        print 'File Id: %s' % child['id']
                        page_token = children.get('nextPageToken')
                        if not page_token:
                            break
            except errors.HttpError, error:
                print 'An error occurred: %s' % error
                break


    def print_about(self):
        try:
            about = self.service.about().get().execute()
            print 'Current user name: %s' % about['name']
            print 'Root folder ID: %s' % about['rootFolderId']
            print 'Total quota (bytes): %s' % about['quotaBytesTotal']
            print 'Used quota (bytes): %s' % about['quotaBytesUsed']
        except errors.HttpError, error:
                print 'An error occurred: %s' % error



def register_blueprints(app, package_name, package_path):
    """Register all Blueprint instances on the specified Flask application found
    in all modules for the specified package.

    :param app: the Flask application
    :param package_name: the package name
    :param package_path: the package path
    """
    rv = []
    for _, name, _ in pkgutil.iter_modules(package_path):
        m = importlib.import_module('%s.%s' % (package_name, name))
        for item in dir(m):
            item = getattr(m, item)
            if isinstance(item, Blueprint):
                app.register_blueprint(item)
            rv.append(item)
    return rv


class JSONEncoder(BaseJSONEncoder):
    """Custom :class:`JSONEncoder` which respects objects that include the
    :class:`JsonSerializer` mixin.
    """
    def default(self, obj):
        if isinstance(obj, JsonSerializer):
            return obj.to_json()
        return super(JSONEncoder, self).default(obj)


class JsonSerializer(object):
    """A mixin that can be used to mark a SQLAlchemy model class which
    implements a :func:`to_json` method. The :func:`to_json` method is used
    in conjuction with the custom :class:`JSONEncoder` class. By default this
    mixin will assume all properties of the SQLAlchemy model are to be visible
    in the JSON output. Extend this class to customize which properties are
    public, hidden or modified before being being passed to the JSON serializer.
    """

    __json_public__ = None
    __json_hidden__ = None
    __json_modifiers__ = None

    def get_field_names(self):
        for p in self.__mapper__.iterate_properties:
            yield p.key

    def to_json(self):
        field_names = self.__dict__

        public = self.__json_public__ or field_names
        hidden = self.__json_hidden__ or []
        modifiers = self.__json_modifiers__ or dict()

        rv = dict()
        for key in public:
            rv[key] = getattr(self, key)
        for key, modifier in modifiers.items():
            value = getattr(self, key)
            rv[key] = modifier(value, self)
        for key in hidden:
            rv.pop(key, None)
        return rv