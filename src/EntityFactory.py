import random

from src.Background import Background
from src.Const import WIN_WIDTH, WIN_HIGTH
from src.Enemy import Enemy
from src.Player import Player


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'background-game':
                list_background = Background('background-game', position)
                return list_background
            case 'Principal':
                return Player('Principal', (WIN_WIDTH / 2, 400))
            case 'inimigo':
                return Enemy('inimigo', (random.randint(0, WIN_WIDTH-10), 0))
            case 'inimigo2':
                return Enemy('inimigo2', (random.randint(0, WIN_WIDTH-10), 0))
