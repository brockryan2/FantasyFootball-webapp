
class Stats():
    def __init__(self, player):
        self.TD = 0
        self.fumbles = 0

        if hasattr(player, '_position_type') and getattr(player, '_position_type') == "Offense":
            print("this is working!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            self.rush_attempts      = None
            self.rush_yards         = None
            self.pass_attempts      = None
            self.pass_yards         = None
            self.pass_completions   = None
            self.pass_interceptions = None
            self.reception_attempts = None
            self.receptions         = None
            self.reception_yards    = None
            self.safeties           = None
            self.pass_TD            = None

        if hasattr(player, '_position') and getattr(player, '_position') == "QB":
            self.qb_rating = 0

        if hasattr(player, '_position') and getattr(player, '_position') == "D/ST":
            self.points_allowed          = None
            self.yards_allowed           = None
            self.interceptions_recovered = None
            self.fumbles_recovered       = None
            self.sacks                   = None
            self.safety                  = None
            self.blocked_PAT_FG          = None

        if hasattr(player, '_position') and getattr(player, '_position') == "K":
            self.FG_made     = None
            self.FG_attempts = None
            self.XP_made     = None
