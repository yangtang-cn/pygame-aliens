import pygame
import sys
from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    # 初始化游戏背景设置
    pygame.init()
    # 创建Settings的实例
    ai_settings = Settings()
    # 设置屏幕
    screen = pygame.display.set_mode((
        ai_settings.screen_width,ai_settings.screen_height
    ))
    pygame.display.set_caption("Alien invasion")
    # 创建PLAY按钮
    button = Button(ai_settings,screen,"Play")
    # 在屏幕上创建飞船的实例
    ship = Ship(ai_settings,screen)
    # 创建子弹实例
    bullets = Group()
    # 创建外星人实例
    aliens = Group()
    # 创建游戏统计信息的实例
    stats = GameStats(ai_settings)
    # 创建积分牌
    sb = Scoreboard(ai_settings,screen,stats)

    gf.create_fleet(ai_settings,screen,ship,aliens)

    while True:

        # 监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,stats,sb,button,ship,aliens,bullets)

        if stats.game_active:

            # 更新飞船的实时位置
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,sb,screen,ship,aliens,bullets)

        # 更新背景
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,button)


run_game()
