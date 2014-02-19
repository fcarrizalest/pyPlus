import httplib2
import pprint
import sys
import json
import random
import string


from flask import Flask
from flask import make_response
from flask import render_template
from flask import request
from flask import session

from simplekv.memory import DictStore
from flaskext.kvsession import KVSessionExtension

from apiclient.discovery import build
from oauth2client.client import SignedJwtAssertionCredentials


APPLICATION_NAME = 'Google+ Python Quickstart'

app = Flask(__name__)

# See the simplekv documentation for details
store = DictStore()


# This will replace the app's session handling
KVSessionExtension(store, app)


# Email of the Service Account.
SERVICE_ACCOUNT_EMAIL = '464235206596-l8h7irh5drhrmqqbugaj4atrmnurhm3c@developer.gserviceaccount.com'

# Path to the Service Account's Private Key file.
SERVICE_ACCOUNT_PKCS12_FILE_PATH = '0ab8bdfaa0f13511e3d404377a363ae160eca697-privatekey.p12'

def createDriveService():
  """Builds and returns a Drive service object authorized with the given service account.

  Returns:
    Drive service object.
  """
  f = file(SERVICE_ACCOUNT_PKCS12_FILE_PATH, 'rb')
  key = f.read()
  f.close()

  credentials = SignedJwtAssertionCredentials(SERVICE_ACCOUNT_EMAIL, key,"https://www.googleapis.com/auth/plus.login")
  http = httplib2.Http() 
  http = credentials.authorize(http)

  return build('plus', 'v1', http = http)

@app.route('/', methods=['GET'])
def index():

	response = make_response(render_template('index.html') )
	response.headers['Content-Type'] = 'text/html'



	return response


@app.route('/activities/<id>' )
def activities_user(id):
	service = createDriveService()
	activities_resource = service.activities()
	request = activities_resource.list( userId=id, collection='public')
	activities_document = request.execute()

	response = make_response( json.dumps(activities_document) , 200)
	response.headers['Content-Type'] = 'application/json'
	return  response


@app.route( '/search/p/<search>' )
def search_user(search):

	service = createDriveService()
	people_resource = service.people()
	people_document = people_resource.search(  maxResults = 10 , query=search  ) . execute()

	response = make_response( json.dumps(people_document) , 200)
	response.headers['Content-Type'] = 'application/json'
	return  response

@app.route('/', methods=['GET'])
def d():
	
	service =  createDriveService()

	activities_resource = service.activities()
	request = activities_resource.list( userId='108250612542617275436' , collection='public' , maxResults=20 )
	L = []
	returnD = {}

	while request != None:
		
		activities_document = request.execute()
		
		if 'items' in activities_document:
			
			returnD['nextPageToken'] = activities_document['nextPageToken']

			for activity in activities_document['items']:

				L.append(activity)

		request = None #"""request = service.activities().list_next(request, activities_document)"""
		returnD['items'] =  L

	response = make_response( json.dumps(returnD) , 200)
	response.headers['Content-Type'] = 'application/json'
		
	return response
	

if __name__ == "__main__":
	app.debug = True
	app.run()
