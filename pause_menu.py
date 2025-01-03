import pygame
import sys

class PauseMenu:
    def __init__(self, config):
        self.config = config
        self.window = pygame.display.set_mode((config.width, config.height))
        pygame.display.set_caption(config.title)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 48)
        self.buttons = [
            {"text": "Resume", "rect": pygame.Rect(300, 200, 200, 50)},
            {"text": "Main Menu", "rect": pygame.Rect(300, 300, 200, 50)},
            {"text": "Quit", "rect": pygame.Rect(300, 400, 200, 50)}
        ]
        self.next_state = None

    def run(self):
        running = True
        while running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.buttons[0]["rect"].collidepoint(event.pos):
                        self.next_state = 'resume'
                        running = False
                    elif self.buttons[1]["rect"].collidepoint(event.pos):
                        self.next_state = 'menu'
                        running = False
                    elif self.buttons[2]["rect"].collidepoint(event.pos):
                        self.next_state = 'quit'
                        running = False

            self.draw()

    def draw(self):
        self.window.fill(self.config.white)
        for button in self.buttons:
            pygame.draw.rect(self.window, self.config.blue, button["rect"])
            text_surf = self.font.render(button["text"], True, self.config.black)
            text_rect = text_surf.get_rect(center=button["rect"].center)
            self.window.blit(text_surf, text_rect)
        pygame.display.flip()
