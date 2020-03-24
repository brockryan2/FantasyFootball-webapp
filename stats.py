
class Stats():
  def __init__(self, player):
    self.TD = 0
    self.fumbles = 0

    if hasattr(player, 'position'):
        if getattr(player, 'position') == "RB":
            print("Runningback")
            self.rush_yards = 0
            self.rush_att   = 0
            self.

        if getattr(player, 'position') == "QB":
            print("Quarterback")
            self.pass_yards = 0
            self.qb_rating = 0
