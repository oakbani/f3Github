import fastjsonschema
from gwrapper import logger_interface
from gwrapper import wrapper
import mock
from nose.tools import assert_true
import requests
from tests import const
import unittest

mock_pull_response = const.mock_response
list_pulls_response = const.pull_response
pr_by_commits = const.pr_commits
pr_by_file_num = const.pr_file_numbers


class TestWrapper(unittest.TestCase):

    def test_invalid_repo_url(self):
        with mock.patch(
            'gwrapper.logger_interface.ChildLogger.log',
        ) as mock_client_log:
            invalid_url = "https://api.github.com/repos/oakbani/fGithub"
            test_client = wrapper.GWrapper(
                '''{
                    "url": "https://api.github.com/repos/oakbani/fGithub",
                    "username": "MariamJamal32",
                    "pwd": "Mariam1374",
                    "version": 1
                }''',
                logger=logger_interface.ChildLogger()

            )
            print(test_client)
            self.assertIsNone(test_client)
            self.assertRaises(ValueError)
        mock_client_log.assert_called_with(
            40, "No repository exists with url: {}".format(invalid_url)
        )

    def test_invalid_json_versions(self):
        with mock.patch(
            'gwrapper.logger_interface.ChildLogger.log',
        ) as mock_client_logger:
            test_client = wrapper.GWrapper(
                '''{
                    "url": "https://api.github.com/repos/oakbani/f3Github",
                    "username": "MariamJamal32",
                    "pwd": "Mariam1374",
                    "version": 5
                }''',
                logger=logger_interface.ChildLogger()

            )
            self.assertIsNone(test_client)
            self.assertRaises(fastjsonschema.JsonSchemaException)
        mock_client_logger.assert_called_with(
            40, "data.version must be one of [1, 2]"
        )

    def test_invalid_json_v1(self):
        with mock.patch(
            'gwrapper.logger_interface.ChildLogger.log',
        ) as mock_client_logger:
            test_client = wrapper.GWrapper(
                '''{
                    "url":[ "https://api.github.com/repos/oakbani/f3Github"],
                    "username": "MariamJamal32",
                    "pwd": "Mariam1374",
                    "version": 1
                }''',
                logger=logger_interface.ChildLogger()
            )
            self.assertIsNone(test_client)
            self.assertRaises(fastjsonschema.JsonSchemaException)
        mock_client_logger.assert_called_with(40, "data.url must be string")

    def test_invalid_json_v2(self):
        test_client = wrapper.GWrapper(
            '''{
                "url":[ "https://api.github.com/repos/oakbani/f3Github"],
                "username": "MariamJamal32",
                "pwd": "Mariam1374",
                "version": 2
            }''',
            logger=logger_interface.ChildLogger()
        )
        self.assertIsNone(test_client)
        self.assertRaises(fastjsonschema.JsonSchemaException)

    def test_get_pulls_response(self):
        test_client = wrapper.GWrapper(
            '''{
                "url": "https://api.github.com/repos/oakbani/f3Github",
                "username": "MariamJamal32",
                "pwd": "Mariam1374",
                "version": 1
            }''',
            logger=logger_interface.ChildLogger()
        )
        response = requests.get(test_client.url, auth=test_client.auth)
        assert_true(response.ok)

    def test_list_pulls(self):
        # test_client = wrapper.GWrapper(
        #     '''{
        #         "url": "https://api.github.com/repos/oakbani/f3Github",
        #         "username": "MariamJamal32",
        #         "pwd": "Mariam1374",
        #         "version": 1
        #     }''',
        #     logger=logger_interface.ChildLogger()
        # )
        # self.assertEqual(
        #     test_client.list_pulls(),
        #     list_pulls_response
        # )
        pass

    def test_filter_pull_requests(self):
        test_client = wrapper.GWrapper(
            '''{
                "url": "https://api.github.com/repos/oakbani/f3Github",
                "username": "MariamJamal32",
                "pwd": "Mariam1374",
                "version": 1
            }''',
            logger=logger_interface.ChildLogger()
        )
        with mock.patch(
            'gwrapper.wrapper.GWrapper.list_pulls',
            return_value=mock_pull_response
        ) as mock_list_pulls:
            self.assertIsInstance(
                test_client.get_pr_with_num_of_commits(
                    2, 'gt', state="closed"
                ),
                list
            )
            self.assertListEqual(
                test_client.get_pr_with_num_of_commits(
                    2, 'gt', state="closed"
                ),
                pr_by_commits
            )
            self.assertIsInstance(
                test_client.get_pr_by_commit_text(
                    ['check', 'abc'], 'any', state="closed"
                ),
                list
            )
            self.assertEqual(
                test_client.get_pr_by_commit_text(
                    ['check', 'abc'], 'any', state="closed"
                ),
                pr_by_commits
            )

            self.assertIsInstance(
                test_client.get_pr_with_num_of_files(2, 'lt', state="closed"),
                list
            )
            self.assertEqual(
                test_client.get_pr_with_num_of_files(2, 'gt', state="closed"),
                pr_by_file_num
            )
            self.assertIsInstance(
                test_client.get_pr_by_file_name(
                    ['.gitignore', 'green'], 'all', state='closed'
                ),
                list
            )
            self.assertListEqual(
                test_client.get_pr_by_file_name(
                    ['.gitignore', 'green'], 'all', state='closed'
                ),
                []
            )
        self.assertTrue(mock_list_pulls.called)
        mock_list_pulls.assert_called_with({"state": "closed"})


if __name__ == '__main__':
    unittest.main()
