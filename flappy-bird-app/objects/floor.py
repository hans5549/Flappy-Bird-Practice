import pygame
import assets


class Floor(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self.image = assets.get_sprite("floor")
        self.rect = self.image.get_rect(topleft=(0, 0))
        super().__init__(*groups)