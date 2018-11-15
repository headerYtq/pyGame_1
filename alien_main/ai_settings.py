class Settings():

    # 储存外星人的类
    def __init__(self):
        # 初始化游戏设置
        # 屏幕设置
        self.screen_width = 900
        self.screen_height = 700
        self.bg_color = (200, 20, 200)
        self.ship_speed_factor = 3

        self.bullet_speed_factor = 1
        self.ship_limit = 3
        self.bullet_width = 30
        self.bullet_height = 10
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5

        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 0.5


