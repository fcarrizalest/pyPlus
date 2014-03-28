import os
import os.path

DEBUG = True
SECRET_KEY = 's-secret-key'
# Email of the Service Account.
SERVICE_ACCOUNT_EMAIL = '464235206596-l8h7irh5drhrmqqbugaj4atrmnurhm3c@developer.gserviceaccount.com'

# Path to the Service Account's Private Key file.
SERVICE_ACCOUNT_PKCS12_FILE_PATH = '0ab8bdfaa0f13511e3d404377a363ae160eca697-privatekey.p12'
WTF_CSRF_ENABLED = False

current_dir =os.path.dirname(__file__)
parent = os.path.join(current_dir, "../tmp/")


FILESTORETMP = parent 