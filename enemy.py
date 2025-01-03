import pygame
from pygame.sprite import Sprite
import random

class Enemy(Sprite):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.original_image = pygame.image.load(config.enemy_image)
        self.image = pygame.transform.scale(self.original_image, (50, 50))  # Измените размер на нужный вам
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, config.width - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speed = config.enemy_speed
        self.health = config.enemy_health  # Используем значение здоровья из конфигурации

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > self.config.height:
            self.kill()

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.kill()
