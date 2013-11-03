"""Experiments with the Google Books API.

This sample requires the Google API client and gflags.
"""

import sys
import httplib2
from apiclient import discovery
from oauth2client import client as oauth2_client
from oauth2client import file as oauth2_file
from oauth2client import tools as oauth2_tools

# API Client ID and Secret created from API Console as an Installed
# Application. In this configuration, the API_CLIENT_SECRET isn't really a
# secret and will be managed by OAuth2.
API_CLIENT_ID = '254931442772.apps.googleusercontent.com'
API_CLIENT_SECRET = 'keFC5uuDhudWpzKUh1AwrI0T'

STORAGE_FILE = 'gbapi-experiments.dat'
BOOKS_API_NAME = 'books'
BOOKS_API_VERSION = 'v1'
BOOKS_API_SCOPE = 'https://www.googleapis.com/auth/books'


def main(argv=None):
  if argv is None:
    argv = sys.argv

  storage = oauth2_file.Storage(STORAGE_FILE)
  credentials = storage.get()
  if credentials is None or credentials.invalid:
    flow = oauth2_client.OAuth2WebServerFlow(
        client_id=API_CLIENT_ID,
        client_secret=API_CLIENT_SECRET,
        scope=BOOKS_API_SCOPE)
    credentials = oauth2_tools.run(flow, storage) 

  http = httplib2.Http()
  credentials.authorize(http)
  service = discovery.build(BOOKS_API_NAME, BOOKS_API_VERSION, http=http) 

  mylibrary = service.mylibrary()
  print mylibrary.bookshelves().list().execute()


if __name__ == '__main__':
    sys.exit(main())
