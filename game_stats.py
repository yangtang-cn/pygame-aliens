class GameStats():
    """跟踪游戏的统计信息"""
    def __init__(self,ai_settings):
        self.ai_settings = ai_settings
        # self.ship_left = 0
        self.reset_stats()
        self.game_active = False
        # 最高得分
        self.high_score = 0

    def reset_stats(self):
        """初始化游戏"""
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1