from copy import deepcopy


class BaseMatcher(object):
    def __init__(self, expectation):
        if not expectation:
            raise ValueError('expectation argument cannot be empty')
        self.expectation = expectation

    def match(self):
        raise NotImplemented('not implemented yet')

    @property
    def name(self):
        return self.__class__.__name__

    @property
    def expectation(self):
        return self._expectation if hasattr(self, '_expectation') else None

    @expectation.setter
    def expectation(self, value):
        self._expectation = value

    def match_regexp(self, re, value):
        try:
            return bool(re.compile(re).match(value))
        except re.error:
            return False

    def to_dict(self):
        return {self.name: deepcopy(self.expectation)}

    def __repr__(self):
        return '{}({})'.format(self.name, self.expectation)