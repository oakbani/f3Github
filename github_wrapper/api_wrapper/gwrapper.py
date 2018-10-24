import requests

class GWrapper():
    def __init__(self, url):
        self.url = url

    #to list all pull requests made to a repos
    def list_pulls(self, **params):
        r = requests.get(self.url, params=params)
        return print(r.text)

    #to list a pull rquest by id
    def list_pull(self, pull_id):
        r = requests.get(self.url+'/'+str(pull_id))
        return print(r.text)
