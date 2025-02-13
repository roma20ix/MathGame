""""""


import pygame
import random

from src.settings import *
from src.object import Object
from src.levels import create_level


class Engine:
    """
    """
    
    def __init__(self) -> None:
        """"""
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        # ------------ Объекты ------------ #
        self.car = pygame.Rect(118, 618, 64, 64)

        # ------------ Спрайты ------------ #
        self.bg = pygame.image.load(BG_SPRITE)
        self.time_label = pygame.image.load(TIME_SPRITE)

        self.line1 = Object(LINE_SPRITE, 100, 100)
        self.line2 = Object(LINE_SPRITE, 200, 100)
        self.line3 = Object(LINE_SPRITE, 300, 100)

        self.left_button = Object(LEFT_BUTTON_SPRITE, 110, 710)
        self.up_button = Object(UP_BUTTON_SPRITE, 210, 710)
        self.right_button = Object(RIGHT_BUTTON_SPRITE, 310, 710)

        self.other_sprites = pygame.sprite.Group()
        self.other_sprites.add(self.line1)
        self.other_sprites.add(self.line2)
        self.other_sprites.add(self.line3)
        self.other_sprites.add(self.left_button)
        self.other_sprites.add(self.up_button)
        self.other_sprites.add(self.right_button)

        # Группа спрайтов с цифрами (Т.е спрайты, составляющие уровень)
        self.map = create_level("123412312731983197235425256123412312731983197235425256123412312731983197235425256123412312731983197235425256")
        self.map_sprites = pygame.sprite.Group()
        print(self.map)
        for digit, line in self.map:
            self.map_sprites.add(Object(digit, line * 100 + 18, random.randint(-10000, -200)))

        # ------------ Константы ------------ #
        self.__game_end = 0
        self.__digit_speed = 4

    def __del__(self) -> None:
        """Выход из игры."""
        pygame.quit()
    
    def __check_events(self) -> None:
        """Проверка всех происходящих событий в игре."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__game_end = 1

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:   # Движение влево
                print("LEFT")
                self.car.x -= 25
            if keys[pygame.K_UP]:     # Движение вверх
                print("UP")
                self.car.y -= 25
            if keys[pygame.K_RIGHT]:  # Движение вправо
                print("RIGHT")
                self.car.x += 25

    def __check_logic(self) -> None:
        """Проверка логики всех происходящих событий в игре."""
        pass

    def __draw(self) -> None:
        """Отрисовка всех объектов."""
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.time_label, (125, 25))

        self.other_sprites.update()
        self.other_sprites.draw(self.screen)

        for sprite in self.map_sprites:
            sprite.move(self.__digit_speed)

        self.map_sprites.update()
        self.map_sprites.draw(self.screen)

        pygame.draw.rect(self.screen, RED, self.car)
        pygame.display.flip()

    def run(self) -> None:
        """Запуск игры."""
        pygame.init()
        pygame.display.set_caption(TITLE)

        while not self.__game_end:
            self.__check_events()
            self.__check_logic()
            self.__draw()
            self.clock.tick(FPS)
