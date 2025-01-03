import pygame
from pygame.sprite import Sprite

class Player(Sprite):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.original_image = pygame.image.load(config.player_image)
        self.image = pygame.transform.scale(self.original_image, (160, 80))  # Измените размер на нужный вам
        self.rect = self.image.get_rect()
        self.rect.centerx = config.width // 2
        self.rect.bottom = config.height - 10
        self.speed = config.player_speed
        self.health = config.player_health  # Исполь уем значение здоровья из конфигурации

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Ограничение движения в пределах окна
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.config.width:
            self.rect.right = self.config.width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.config.height:
            self.rect.bottom = self.config.height

    def shoot(self, bullets):
        bullet = Bullet(self.config, self.rect.centerx, self.rect.top)
        bullets.add(bullet)

    def draw(self, window):
        window.blit(self.image, self.rect)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.kill()

class Bullet(Sprite):
    def __init__(self, config, x, y):
        super().__init__()
        self.config = config
        self.original_image = pygame.image.load(config.bullet_image)
        self.image = pygame.transform.scale(self.original_image, (40, 60))  # Измените размер на нужный вам
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = config.bullet_speed

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()
