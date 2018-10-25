import requests

class GWrapper():
    def __init__(self, url, username, pwd):
        self.url = url
        self.auth = (username, pwd)

    #to list all pull requests made to a repos
    #params: base, state, sort, head, direction
    def list_pulls(self, params):
        print(params)
        return print(requests.get(self.url, params=params).text)

    #to list a pull rquest by id
    #pull_id required
    def list_pull(self, pull_id):
        print(requests.get(self.url+'/'+str(pull_id)).text)

    #list commits on a pull request
    #pull_id required
    def list_pull_commits(self, pull_id):
        print(requests.get(self.url+'/'+str(pull_id)+'/commits').text)

    #list files on a pull request
    #pull_id required
    def list_pull_files(self, pull_id):
        print(requests.get(self.url+'/'+str(pull_id)+'/files').text)

    #post pull request
    #required payload: base, title, head, pull_id
    def post_pull_request(self, params):
        required_params = ['base','title', 'head']
        if not all(x in params.keys() for x in required_params):
            print('Insufficient parameters. Required Params:')
            for x in required_params:
                print(x)
        else:
            return print(requests.post(self.url, json=params, auth=self.auth).text)

    #update pull request
    def update_pull_request(self, pull_id, params):
        return print(requests.patch(self.url+'/'+str(pull_id), json=params, auth=self.auth).text)
