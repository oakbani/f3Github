import fastjsonschema
from gwrapper.number_filter import Filter
from gwrapper.string_filter import String_Filter
import json
import requests


class GWrapper(object):
    def __new__(cls, json_init):
        with open('gwrapper/schemas/wrapper_schema.json') as json_data:
            schema = json.load(json_data)

        try:
            validate = fastjsonschema.compile(schema)
            validate(json.loads(json_init))
            url = json.loads(json_init)['url']
            if(requests.get(url).headers['Status'][0:3] == '404'):
                raise ValueError()
            else:
                return super(GWrapper, cls).__new__(cls)
        except fastjsonschema.JsonSchemaException as e:
            print(e.message)
            return None
        except ValueError as v:
            print("No repository exists with url: ", url)
            return None

    def __init__(self, json_init):
        self.url = json.loads(json_init)['url']+'/pulls'
        self.auth = (
            json.loads(json_init)['username'],
            json.loads(json_init)['pwd']
        )

    # to list all pull requests made to a repos
    # params: base, state, sort, head, direction
    def list_pulls(self, params={}):
        return requests.get(self.url, params=params, auth=self.auth)

    # get pull requests by number of commits
    def get_pr_with_num_of_commits(self, num, filter, **params):
        pull_requests = self.list_pulls(params).json()
        f = Filter(pull_requests, num, filter, 'commits', self.auth)
        return print(f.filter_by_number())

    # get pull requests by number of files changed
    def get_pr_with_num_of_files(self, num, filter, **params):
        pull_requests = self.list_pulls(params).json()
        f = Filter(pull_requests, num, filter, 'files', self.auth)
        return print(f.filter_by_number())

    # get pull requests by commit message keywords
    def get_pr_by_commit_text(self, text_list, filter, **params):
        pull_requests = self.list_pulls(params).json()
        f = String_Filter(
            pull_requests, text_list, filter, 'commits', self.auth
        )
        return print(f.filter_by_string())

    # get pull requests by file name keywords
    def get_pr_by_file_name(self, name_list, filter, **params):
        pull_requests = self.list_pulls(params).json()
        f = String_Filter(
            pull_requests, name_list, filter, 'files', self.auth
        )
        return print(f.filter_by_string())
