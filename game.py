import pygame
import sys
from player import Player
from enemy import Enemy
from pygame.sprite import Group
from pause_menu import PauseMenu
from upgrade_menu import UpgradeMenu

class Game:
    def __init__(self, config):
        self.config = config
        self.window = pygame.display.set_mode((config.width, config.height))
        pygame.display.set_caption(config.title)
        self.clock = pygame.time.Clock()
        self.player = Player(config)
        self.enemies = Group()
        self.bullets = Group()
        self.score = 0
        self.last_enemy_spawn = pygame.time.get_ticks()
        self.paused = False
        self.pause_menu = PauseMenu(config)
        self.upgrade_menu = UpgradeMenu(config)
        self.next_state = None
        self.enemies_killed = 0
        self.enemies_to_upgrade = config.enemies_to_upgrade

    def run(self):
        running = True
        while running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.shoot(self.bullets)
                    elif event.key == pygame.K_ESCAPE:
                        self.paused = not self.paused
                        if self.paused:
                            self.pause_menu.run()
                            if self.pause_menu.next_state == 'menu':
                                self.next_state = 'menu'
                                running = False
                            elif self.pause_menu.next_state == 'quit':
                                self.next_state = 'quit'
                                running = False
                            elif self.pause_menu.next_state == 'resume':
                                self.paused = False

            if not self.paused:
                self.update()
            self.draw()

        return self.next_state

    def update(self):
        self.player.update()
        self.bullets.update()
        self.enemies.update()

        # Спавн врагов
        current_time = pygame.time.get_ticks()
        if current_time - self.last_enemy_spawn > self.config.enemy_spawn_interval:
            self.spawn_enemy()
            self.last_enemy_spawn = current_time

        # Проверка столкновений
        for bullet in self.bullets:
            enemy_hit_list = pygame.sprite.spritecollide(bullet, self.enemies, False)
            for enemy in enemy_hit_list:
                enemy.take_damage(self.config.bullet_damage)  # Используем значение урона из конфигурации
                bullet.kill()
                self.score += 10
                if enemy.health <= 0:
                    self.enemies_killed += 1
                    if self.enemies_killed >= self.enemies_to_upgrade:
                        self.show_upgrade_menu()

        for enemy in self.enemies:
            if pygame.sprite.collide_rect(self.player, enemy):
                self.player.take_damage(20)  # Урон от столкновения с врагом
                enemy.kill()
                if self.player.health <= 0:
                    running = False

    def spawn_enemy(self):
        enemy = Enemy(self.config)
        self.enemies.add(enemy)

    def show_upgrade_menu(self):
        self.upgrade_menu.run()
        if self.upgrade_menu.choice == 'damage':
            self.config.bullet_damage += self.config.damage_increase
        elif self.upgrade_menu.choice == 'health':
            self.player.health += self.config.health_increase
        self.enemies_to_upgrade += self.config.enemies_to_upgrade_increase
        self.enemies_killed = 0

    def draw(self):
        self.window.fill(self.config.white)
        self.player.draw(self.window)
        self.enemies.draw(self.window)
        self.bullets.draw(self.window)
        self.draw_score()
        self.draw_health()
        pygame.display.flip()

    def draw_score(self):
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {self.score}", True, self.config.black)
        self.window.blit(score_text, (10, 10))

    def draw_health(self):
        font = pygame.font.SysFont(None, 36)
        health_text = font.render(f"Health: {self.player.health}", True, self.config.black)
        self.window.blit(health_text, (10, 50))
