from gwrapper import wrapper

request = wrapper.GWrapper(
    '''{
        "url": ["https://api.github.com/repos/oakbani/f3Github"],
        "credentials":[
            {
                "username": "1234",
                "pwd": "1234"
            }
        ],

        "version": 2
    }'''
)


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


def get_pr_by_commits():
    request.get_pr_with_num_of_commits(100, 'lt', state="closed")


def get_pr_by_files():
    request.get_pr_with_num_of_files(80, 'lt', state="closed")


# request.get_pr_by_commit_text(['check', 'abc'], 'all', state="closed")
# request.get_pr_by_file_name(['.gitignore', 'green'], 'all', state='closed')
