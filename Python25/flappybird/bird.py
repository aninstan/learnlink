import pygame
from settings import import_sprite

class Bird(pygame.sprite.Spirte):
    def __init__(self,pos,size):
        super().__init__()

        self.frame_index = 0
        self.animation_delay = 3
        self.jump_move = -9

        self.bird_img = import_sprite("assets/bird")
        self.image = self.bird_img[self.frame_index]
        self.image = pygame.transform.scale(self.image, (size,size))
        self.rect = self.image.get_rect(topleft = pos)
        self.mask = pygame.mask.from_surface(self.image)

        self.direction = pygame.math.Vector2(0,0)
        self.score = 0

    def _animate(self):
        sprites = self.bird_img
        sprite_index = (self.frame_index // self.animation_delay) % len(sprites)
        self.image = sprites[sprite_index]
        self.frame_index += 1

        # continue here