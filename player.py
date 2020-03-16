
class Player():
    """
    This class is intended to be used as an abstract class for all player subclasses (e.g. Quarter-
    back). The primary purpose of this class is to organize common implementation details for sub-
    classes.

    Args:
        positional args:
            name (str):     player's name

        key word args:
            ID (str):       unique identification number for each player (for database use)
            position (str): player's position (default = None)
            team (str):     player's real-world team  (default = None)
            number (int):   player's jersey number (default = None)
            status (str):   player's status (e.g. healthy/questionable/etc.) (default = "Healthy")
            points (int):   player's current fantasy points (default = 0)

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


    """

    def __init__(self, name, ID=None, position=None, team=None, number=None, status="Healthy", points=0):
        self._name          = name
        self._position      = position
        self._team          = team
        self._number        = number
        self._status        = status
        self._rank          = "Not Ranked"
        self._points        = points
        self._point_history = {
                                "1" :0,
                                "2" :0,
                                "3" :0,
                                "4" :0,
                                "5" :0,
                                "6" :0,
                                "7" :0,
                                "8" :0,
                                "9" :0,
                                "10":0,
                                "11":0,
                                "12":0,
                                "13":0,
                                "14":0,
                                "15":0,
                                "16":0}
        self._stats         = {
                                ""
        }


    def get_points(self):
        return self._points

    def set_points(self, points):
        self._points = points
        return str(points)

    def update_position(self, position):
        self._position = position


class Quarterback(Player):
    def __init__(self, name):
        super().__init__(name, "QB")
        self._completions = 0


    def points(self):
        set_points(self.pass_yards() * 0.04 + self.rush_yards() * 0.1 + self.touchdowns() * 6)
