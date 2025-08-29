import pygame.key

from src.Const import WIN_HIGTH, WIN_WIDTH
from src.Entity import Entity
from src.PlayerShot import PlayerShot


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = 20

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        print(pressed_key)
        if pressed_key[pygame.K_UP] and self.rect.top > 0:
            self.rect.centery -= 5
        if pressed_key[pygame.K_DOWN] and self.rect.bottom < WIN_HIGTH:
            self.rect.centery += 5
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= 5
        if pressed_key[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += 5
        pass

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = 20
            pressed_key = pygame.key.get_pressed()
            if pressed_key[pygame.K_LCTRL]:
                return PlayerShot('PlayerShot', position=(self.rect.centerx - 8, self.rect.centery))
