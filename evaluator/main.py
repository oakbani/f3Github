import check_eligibility
from criterion import conditions


class Main(object):

    def __init__(self, conditions):
        self.conditions = conditions

    def is_user_eligible(self, attributes=None):
        if attributes:
            e = check_eligibility.CheckEligibility(self.conditions)
            return e.evaluate(conditions, attributes)


if __name__ == '__main__':
    m = Main()
    m.is_user_eligible(
        {
            'color': 'green',
            'browser': 'chrome'
        }
    )
