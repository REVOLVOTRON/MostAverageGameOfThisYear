import pygame
from game_state import GameState
from config import Config

def main():
    # Инициализация Pygame
    pygame.init()

    # Создание экземпляра конфигурации
    config = Config()

    # Создание экземпляра состояния игры
    game_state = GameState(config)

    # Запуск игры
    game_state.run()

    # Завершение работы Pygame
    pygame.quit()

if __name__ == "__main__":
    main()
