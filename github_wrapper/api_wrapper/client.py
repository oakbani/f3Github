import gwrapper

request = gwrapper.GWrapper("https://api.github.com/repos/oakbani/f3Github/pulls")

def get_all_pulls(**params):
    global request
    request.list_pulls(params)

def get_pull(id):
    request.list_pull(id)

def get_pull_commits(pull_id):
    global request
    request.list_pull_commits(pull_id)

def get_pull_files(pull_id):
    global request
    request.list_pull_files(pull_id)

def add_pull_request(**params):
    global request
    print(params)
    request.post_pull_request(params)

add_pull_request(base='Mariamjamal32-patch-1', title='Testing PR Creation', body='Reject this PR please', head='Mariam/ImplementGetApiWrappers')
