
class Player():
    """
    This class is intended to be used as an abstract class for all player subclasses (e.g. Quarter-
    back). The primary purpose of this class is to organize common implementation details for
    payer sub classes.

    Args:
        positional args:
            name (str):     player's name

        key word args:
            ID (str):       unique identification number for each player (for database use)
            position (str): player's position (default = None)
            team (str):     player's real-world team  (default = None)
            number (int):   player's jersey number (default = None)
            status (str):   player's status (e.g. healthy/questionable/etc.) (default = "Healthy")

    Attributes:
        _name (str):     where player's name is stored, accessed/modified using the @property
                             and @[attribute].setter decorators

        _ID (str):       where the player's unique identification number is stored,
                             accessed/modified using the @property & @[attribute].setter decorators

        _position (str): where player's position is stored, accessed/modified using the @property
                             and @[attribute].setter decorators

        _team (str):     where player's team is stored, accessed/modified using the @property
                             and @[attribute].setter decorators

        _number (int):   where player's jersey number is stored, accessed/modified using the
                             @property and @[attribute].setter decorators

        _status (str):   where the player's status is stored, accessed/modified using the @property
                             and @[attribute].setter decorators

        _rank (int):     where the player's rank is stored, accessed/modified using the @property
                             and @[attribute].setter decorators

        _points (int):   where the player's current fantasy points are stored, accessed/modified
                             using the @property and @[attribute].setter decorators

        _points_history (dict): where the player's fantasy points are stored for previous weeks,
                                    accessed/modified using @property & @[att].setter decorators

        _stats (dict):   where the player's current stats are stored, sub classes will add
                             additional keys to this dictionary depending on player position,
                             accessed/modified using @property & @[attribute].setter decorators

        _stat_history (list): where the player's stats for previous weeks are stored as a list
                                  of stats dictionaries, accessed/modified using @property,
                                  @[attribute].setter, and @[attribute].deleter decorators


        Methods:
            In addition to getter & setter methods (and occasional deleter methods), this class
            implements the following methods

            touchdown(self): None

            fumble(self): None


    """

    def __init__(self, name, ID=None, position=None, team=None, number=None, status="Healthy"):
        self._name          = name
        self._ID            = ID
        self._position      = position
        self._team          = team
        self._number        = number
        self._status        = status
        self._rank          = None
        self._points        = None
        self._point_history = {None: None}
        self._stats         = {"TD": 0, "Fumbles": 0}
        self._stat_history  = [None]

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        self._name = name

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def position(self):
        return self._position

    @position.setter
    def points(self, value):
        self._position = value

    @property
    def team(self):
        return self._team

    @team.setter
    def team(self, value):
        self._team = value

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        self._rank = value

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, value):
        self._points = value

    @property
    def point_history(self):
        """:obj: 'dict':

           setter accepts a key as arguments,
           sets the :obj: 'dict' [key] value to 'value'

           raises KeyError if key is not present

        """
        return self._point_history

    @point_history.setter
    def point_history(self, key, value):
        if 1 > int(key) > 17:
            raise KeyError("Cannot set points for week '{}.' Please set the points for week in\
                              range: 1-17.".format(key))
        else:
            self._point_history[key] = value

    @point_history.deleter
    def point_history(self, key):
        try:
            del self._point_history[key]

        except KeyError as ke:
            raise KeyError("Cannot delete point history for '{},' not found".format(key))

            logging.log_error(ke)

    @property
    def stats(self):
        return self._stats

    @stats.setter
    def stats(self, key, value):
        self._stats[key] = value

    @property
    def stat_history(self):
        """:obj: 'list' of :obj: 'dict':

           setter accepts an index and a value as arguments,
           sets the :obj: 'dict' at list[index] to the 'value'

           raises IndexError if index is out of range

        """
        return self._stat_history

    @stat_history.setter
    def stat_history(self, index, value):
        if 1 > int(index) > 17:
            logging.log_error("Index Error", "stat_history.setter", self, index, value)
            raise IndexError("Cannot set stats for week '{}.' Please set the stats for week in\
                              range: 1-17.".format(index))
        else:
            self._stat_history[index] = value

    @stat_history.deleter
    def stat_history(self, index):
        try:
            del self._stat_history[index]

        except IndexError as ie:
            logging.log_error(ie, "stat_history.deleter", self, index)
            raise IndexError("Stat history for '{}' not found".format(key))

    def touchdown(self):
        """Used to increment touchdown stat by 1 and points by number specified in league rules

        returns None
        """
        self._stats["TD"] += 1
        self._points += leagueRules.Points.touchdown()

    def fumble(self):
        """Used to increment fumbles stat by 1 and points by number specified in league rules

        returns None
        """
        self._stats["Fumbles"] += 1
        self._points += leagueRules.Points.fumble()



class OffensivePlayer(Player):
    pass


class Quarterback(OffensivePlayer):
    def __init__(self, name):
        super().__init__(name, "QB")
        self._completions = 0



