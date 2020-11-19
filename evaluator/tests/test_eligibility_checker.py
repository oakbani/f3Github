import criterion
import main
import unittest


class TestEligibilityChecker(unittest.TestCase):

    def test_multiple_attrs(self):
        test_client = main.Main(criterion.conditions)
        self.assertTrue(test_client.is_user_eligible(
            {
                'color': 'green',
                'browser': 'chrome'
            }
        ))

    def test_nonexisting_attrs(self):
        test_client = main.Main(criterion.conditions)
        self.assertFalse(test_client.is_user_eligible(
            {
                'color': 'green',
                'location': 'khi'
            }
        ))

    def test_nonexisting_single_attr(self):
        test_client = main.Main(criterion.conditions)
        self.assertFalse(test_client.is_user_eligible(
            {
                'location': 'khi'
            }
        ))

    def test_single_attr(self):
        test_client = main.Main(criterion.conditions)
        self.assertTrue(test_client.is_user_eligible(
            {
                'browser': 'chrome'
            }
        ))

    def test_multiple_conditions(self):
        test_client = main.Main(criterion.condition2)
        self.assertTrue(test_client.is_user_eligible(
            {
                'browser': 'chrome',
                'color': 'red'
            }
        ))
