from django.core.files.storage import Storage
from django.conf import settings

from smartfile import BasicClient

class SmartFileStorage(Storage):

    def __init__(self):

        self.storage_api = BasicClient()      

    def _open(name, mode='rb'):

        return self.storage_api.download(name)

    def _save(name, content):

        return self.storage_api.upload(name, content)








