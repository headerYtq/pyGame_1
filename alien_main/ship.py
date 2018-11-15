import pygame
import sys


class Ship():
    def __init__(self, ai_settings, screen):
        # 初始化飞船设置初始位置
        self.screen = screen

        self.ai_settings = ai_settings

        self.image = pygame.image.load("C:\\Users\\Administrator\\Desktop\\gane\\allien.jpg")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将没收新飞船放在屏幕底中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # 在飞船中存储你最小值
        self.center = float(self.rect.centerx)
        self.move_right = False
        self.move_left = False

    def update(self):
        # 根据飞船的标志调整飞船的位置
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.move_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        # 在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx
