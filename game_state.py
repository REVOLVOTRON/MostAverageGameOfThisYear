import pygame
import sys
from menu import Menu
from game import Game

class GameState:
    def __init__(self, config):
        self.config = config
        self.window = pygame.display.set_mode((config.width, config.height))
        pygame.display.set_caption(config.title)
        self.clock = pygame.time.Clock()
        self.menu = Menu(config)
        self.game = Game(config)
        self.current_state = self.menu

    def run(self):
        running = True
        while running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            next_state = self.current_state.run()
            if next_state == 'game':
                self.current_state = self.game
            elif next_state == 'menu':
                self.current_state = self.menu
            elif next_state == 'quit':
                running = False

        sys.exit()
