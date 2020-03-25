from sport import Sport

class League():

    def __init__(self, sport=None, rules=None):
        self._sport = Sport(sport)
        self._rules = rules
        self.name   = None

    def name(self, name):
        self.name = name

    @property
    def sport(self):
        return self._sport

    @sport.setter
    def sport(self, sport):
        self._sport = sport

    @property
    def rules(self):
        return self._rules

    @rules.setter
    def rules(self, rules):
        self._rules = rules
