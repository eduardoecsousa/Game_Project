from src.Const import WIN_HIGTH
from src.EnemyShot import EnemyShot
from src.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = 30

    def move(self, ):
        self.rect.centery += 1

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = 100
            return EnemyShot('EnemyShot', position=(self.rect.centerx - 4, self.rect.centery))
