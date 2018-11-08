from gwrapper import logger_interface
from gwrapper import wrapper
import logging


# request = wrapper.GWrapper(
#     '''{
#         "url": ["https://api.github.com/repos/oakbani/f3Github"],
#         "credentials":[
#             {
#                 "username": "1234",
#                 "pwd": "1234"
#             }
#         ],
#         "version": 2
#     }'''
# )

class ClientLogger(logger_interface.ExampleLogger):
    def __init__(
        self,
        handler=logging.StreamHandler(),
        logger_name=__name__,
        min_level=logging.INFO
    ):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(min_level)
        self.logger.handlers = [handler]
        self.min_level = min_level

    def log(self, lvl, msg):
        self.logger.log(lvl, msg)


request = wrapper.GWrapper(
    '''{
        "url": "https://api.github.com/repos/oakbani/f3Github",
        "username": "MariamJamal32",
        "pwd": "Mariam1374",
        "version": 1
    }''',
    logger=ClientLogger()
)


def get_all_pulls(**params):
    request.list_pulls(params)


def get_pull(id):
    request.list_pull(id)


def get_pull_commits(pull_id):
    request.list_pull_commits(pull_id)


def get_pull_files(pull_id):
    request.list_pull_files(pull_id)


def get_pr_by_commits():
    request.get_pr_with_num_of_commits(2, 'gt', state="closed")


def get_pr_by_files():
    request.get_pr_with_num_of_files(80, 'lt', state="closed")


get_pr_by_commits()
# request.get_pr_by_commit_text(['check', 'abc'], 'all', state="closed")
# request.get_pr_by_file_name(['.gitignore', 'green'], 'all', state='closed')
