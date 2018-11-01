from gwrapper import wrapper

request = wrapper.GWrapper(
    "https://api.github.com/repos/oakbani/f3Github",
    username='mariamjamal32',
    pwd='Mariam1374')


def get_all_pulls(**params):
    request.list_pulls(params)


def get_pull(id):
    request.list_pull(id)


def get_pull_commits(pull_id):
    request.list_pull_commits(pull_id)


def get_pull_files(pull_id):
    request.list_pull_files(pull_id)


def add_pull_request(**params):
    request.post_pull_request(params)


def edit_pull_request(pull_id, **params):
    request.update_pull_request(pull_id, params)
