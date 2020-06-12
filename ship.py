import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self,ai_settings,screen):
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        # 加载飞船的图像，获取图像的边框矩形，获取屏幕的边框矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 图像位置信息，将每艘飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # center只是个中间量，用来接收小数
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """
        根据移动的标志来更新位置
        四个标志都是同一优先级的，可以同时操作
        """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def center_ship(self):
        """让飞船放在屏幕上居中"""
        self.center = self.screen_rect.centerx

    def blitme(self):
        self.screen.blit(self.image,self.rect) # 图像及位置