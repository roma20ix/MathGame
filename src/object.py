""""""


import pygame
from src.settings import *


class Object(pygame.sprite.Sprite):
    """
    """

    def __init__(self, image_name: str, x: int, y: int) -> None:
        """
        """
        super().__init__()

        self.image = self.load_image(image_name)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    @staticmethod
    def load_image(image_name: str) -> pygame.Surface:
        """
        """
        if image_name.isdigit():
            image_name = DIGITS[image_name]

        image = pygame.image.load(image_name)
        return image

    def move(self, speed: int) -> None:
        self.rect.y += speed
        