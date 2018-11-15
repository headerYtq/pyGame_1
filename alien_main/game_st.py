class GameStats():
    def __init__(self, ai_settings):
        # 初始化信息
        self.ai_settings = ai_settings
        self.rest_stats()
        self.game_active = False

    def rest_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score  = 0
