class CheckEligibility(object):

    def __init__(self, conditions):
        self.condition_set = conditions

    def evaluate(self, conditions, attrs):
        print('in evaluate')
        if isinstance(conditions, list):
            if(conditions[0] == 'and'):
                return self.and_evaluator(conditions[1:], attrs)
            elif(conditions[0] == 'or'):
                return self.or_evaluator(conditions[1:], attrs)
        else:
            return conditions['value'] == attrs.get(conditions['name'])

    def and_evaluator(self, conditions, attrs):
        print('in and')
        for cond in conditions:
            print(cond)
            eligible = self.evaluate(cond, attrs)
            if not eligible:
                return False
        else:
            return True

    def or_evaluator(self, conditions, attrs):
        print('in or')
        for cond in conditions:
            print(cond)
            eligible = self.evaluate(cond, attrs)
            if eligible:
                return True
        else:
            return False
