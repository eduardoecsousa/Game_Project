from abc import ABC, abstractmethod

import pygame.image

from src.Const import ENTITY_HEAlTH


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('../assets/img/'+name+'.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEAlTH[self.name]

    @abstractmethod
    def move(self,):
        pass