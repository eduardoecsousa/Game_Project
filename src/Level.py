import random
import sys

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from src.Const import COLOR_WHITE, WIN_WIDTH, EVENT_ENEMY, COLOR_GREEN, EVENT_TIMEOUT
from src.Enemy import Enemy
from src.Entity import Entity
from src.EntityFactory import EntityFactory
from src.EntityMediator import EntityMediator
from src.Player import Player


class Level:
    def __init__(self, window, name, player_score: int):
        self.timeout = 20000
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.append(EntityFactory.get_entity('background-game'))
        self.entity_list.append(EntityFactory.get_entity('Principal'))
        pygame.time.set_timer(EVENT_ENEMY, 4000)
        pygame.time.set_timer(EVENT_TIMEOUT, 100)

    def run(self, ):
        pygame.mixer_music.load('../assets/img/audio-game.wav')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.name == 'Principal':
                    self.level_text(14, f'Player 1 - Health: {ent.health} | Score: {ent.score}', COLOR_GREEN, (10, 16))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('inimigo', 'inimigo2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= 100
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Principal':
                                player_score = ent.score
                        return True

                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True

                if not found_player:
                    return False

            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(14, f'fps {clock.get_fps():.0f}', COLOR_WHITE, (10, 440))
            self.level_text(14, f'entidades {len(self.entity_list)}', COLOR_WHITE, (10, 455))
            pygame.display.flip()

            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
