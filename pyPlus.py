import json
import pprint
import random
import string
import sys

from apiclient.discovery import build
from flask import Flask
from flask import make_response
from flask import render_template
from flask import request
from flask import session 
import httplib2
from oauth2client.client import SignedJwtAssertionCredentials
from simplekv.memory import DictStore

from driveServices import DriveServices
from flaskext.kvsession import KVSessionExtension


APPLICATION_NAME = 'Google Python Quickstart'

app = Flask(__name__)


# See the simplekv docume ntation for details
store = DictStore()


# This will replace the app's session handling
KVSessionExtension(store, app)


# Email of the Service Account.
SERVICE_ACCOUNT_EMAIL = '@developer.gserviceaccount.com'

# Path to the Service Account's Private Key file.
SERVICE_ACCOUNT_PKCS12_FILE_PATH = '-privatekey.p12'


def createDriveService():
  """Builds and returns a Drive service object authorized with the given service  account.

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


@app.route('/drive')
def drive():

	driveServices = DriveServices()
	services = driveServices.createDriveServices( SERVICE_ACCOUNT_EMAIL , SERVICE_ACCOUNT_PKCS12_FILE_PATH)
	listFiles = driveServices.retrieve_all_files(services)
	if len(listFiles) == 0:
		print "nada"
		print "nada"
		print listFiles
		title = "data.json" 
		description = "descriptio"
		parent_id = "root"
		mime_type = "application/json"
		filename = "data.json"
		driveServices.insert_file(services, title, description, parent_id, mime_type, filename)
	else:
		print "Encontre archivos "
		print len(listFiles)

	response = make_response(render_template('indexdrive.html') )
	return response


@app.route('/activity/<idA>')
def activity(idA):
	service = createDriveService()
	activities_resource = service.activities()
	activity = activities_resource.get( activityId=idA).execute()
	response = make_response( json.dumps(activity) , 200)
	response.headers['Content-Type'] = 'application/json'
	return  response


@app.route('/activity/<id>/comments')
def activity_comments(idC):
	service = createDriveService()
	comments_resource = service.comments()
	comments_document = comments_resource.list( maxResults=100,activityId=idC).execute()

	response = make_response( json.dumps(comments_document) , 200)
	response.headers['Content-Type'] = 'application/json'
	return  response

@app.route('/activities/<id>' )
def activities_user(idA):
	service = createDriveService()
	activities_resource = service.activities()
	request = activities_resource.list( userId=idA, maxResults= 23 , collection='public')
	activities_document = request.execute()

	response = make_response( json.dumps(activities_document) , 200)
	response.headers['Content-Type'] = 'application/json'
	return  response


@app.route( '/search/p/<search>' )
def search_user(search):

	service = createDriveService()
	people_resource = service.people()
	people_document = people_resource.search(  maxResults = 50 , query=search  ) . execute()

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
