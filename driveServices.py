from apiclient.discovery import build
from apiclient.http import MediaFileUpload
import httplib2
from oauth2client.client import SignedJwtAssertionCredentials
from apiclient import errors

class DriveServices:

	def createDriveServices(self, SERVICE_ACCOUNT_EMAIL , SERVICE_ACCOUNT_PKCS12_FILE_PATH):
		f = file(SERVICE_ACCOUNT_PKCS12_FILE_PATH, 'rb')
		key = f.read()
		f.close()

		credentials = SignedJwtAssertionCredentials(SERVICE_ACCOUNT_EMAIL, key,
													scope='https://www.googleapis.com/auth/drive')
		http = httplib2.Http()
		http = credentials.authorize(http)

		return build('drive', 'v2', http=http)
	
	def insert_file(self , service, title, description, parent_id, mime_type, filename):
		media_body = MediaFileUpload(filename, mimetype=mime_type, resumable=True)
		body = {'title': title,'description': description,'mimeType': mime_type}
		if parent_id:
			body['parents'] = [{'id': parent_id}]
		try:
			fileT = service.files().insert(body=body,media_body=media_body).execute()
			
			return fileT
		except errors.HttpError, error:
			print 'An error occured: %s' % error
		return None


	def update_file(self, service, file_id, new_title, new_description, new_mime_type, new_filename, new_revision):
		try:
			fileT = service.files().get(fileId=file_id).execute()
			# File's new metadata.
			fileT['title'] = new_title
			fileT['description'] = new_description
			fileT['mimeType'] = new_mime_type
			# File's new content.
			media_body = MediaFileUpload(new_filename, mimetype=new_mime_type, resumable=True)
			# Send the request to the API.
			updated_file = service.files().update(fileId=file_id,body=fileT,newRevision=new_revision,media_body=media_body).execute()
			return updated_file
		except errors.HttpError, error:
			print 'An error occurred: %s' % error
		return None


	def retrieve_all_files(self, service):
		result = []
		page_token = None
		while True:
			try:
				param = {}
				if page_token:
					param['pageToken'] = page_token
					files = service.files().list(**param).execute()
					result.extend(files['items'])
					page_token = files.get('nextPageToken')
					if not page_token:
						break
			except errors.HttpError, error:
				print 'An error occurred: %s' % error
				break
		return result
	
	
	def print_files_in_folder(self, service, folder_id):
		page_token = None
		while True:
			try:
				param = {}
				if page_token:
					param['pageToken'] = page_token
					children = service.children().list(folderId=folder_id, **param).execute()
					for child in children.get('items', []):
						print 'File Id: %s' % child['id']
						page_token = children.get('nextPageToken')
						if not page_token:
							break
			except errors.HttpError, error:
				print 'An error occurred: %s' % error
				break


	def print_about(self, service):
		try:
			about = service.about().get().execute()
			print 'Current user name: %s' % about['name']
			print 'Root folder ID: %s' % about['rootFolderId']
			print 'Total quota (bytes): %s' % about['quotaBytesTotal']
			print 'Used quota (bytes): %s' % about['quotaBytesUsed']
		except errors.HttpError, error:
				print 'An error occurred: %s' % error
