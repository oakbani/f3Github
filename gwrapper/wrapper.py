import fastjsonschema
from gwrapper import logger_interface
from gwrapper.number_filter import Filter
from gwrapper.string_filter import String_Filter
import json
import logging
import requests


class GWrapper(object):
    def __new__(cls, json_init, logger=None):

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
        except ValueError:
            print("No repository exists with url: ", url)
            return None

    def __init__(self, json_init, logger=None):
        self.logger = logger or logger_interface.NoOpLogger()
        self.level = logger.min_level
        self.url = json.loads(json_init)['url']+'/pulls'
        self.auth = (
            json.loads(json_init)['username'],
            json.loads(json_init)['pwd']
        )

    # to list all pull requests made to a repos
    # params: base, state, sort, head, direction
    def list_pulls(self, params={}):
        response = requests.get(self.url, params=params, auth=self.auth)
        msg = str(len(response.json())) + ' pull requests fetched'
        self.logger.log(logging.INFO, msg)
        return response

    # get pull requests by number of commits
    def get_pr_with_num_of_commits(self, num, filter, **params):
        pull_requests = self.list_pulls(params).json()
        f = Filter(pull_requests, num, filter, 'commits', self.auth)
        response = f.filter_by_number()
        msg = str(len(response)) + ' pull requests found with commit filter'
        self.logger.log(logging.INFO, msg)
        return print(response)

    # get pull requests by number of files changed
    def get_pr_with_num_of_files(self, num, filter, **params):
        pull_requests = self.list_pulls(params).json()
        f = Filter(pull_requests, num, filter, 'files', self.auth)
        response = f.filter_by_number()
        msg = str(len(response)) + ' pull requests found with file filter'
        self.logger.log(logging.INFO, msg)
        return print(response)

    # get pull requests by commit message keywords
    def get_pr_by_commit_text(self, text_list, filter, **params):
        pull_requests = self.list_pulls(params).json()
        f = String_Filter(
            pull_requests, text_list, filter, 'commits', self.auth
        )
        response = f.filter_by_string()
        msg = str(len(response)) + ' pull requests' +
        'found with commit text filter'
        self.logger.log(logging.INFO, msg)
        return print(response)

    # get pull requests by file name keywords
    def get_pr_by_file_name(self, name_list, filter, **params):
        pull_requests = self.list_pulls(params).json()
        f = String_Filter(
            pull_requests, name_list, filter, 'files', self.auth
        )
        response = f.filter_by_string()
        msg = str(len(response)) + ' pull requests' +
        'found with file name filter'
        self.logger.log(logging.INFO, msg)
        return print(response)
