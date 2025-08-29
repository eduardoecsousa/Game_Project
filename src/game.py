import pygame

from src.Const import MENU_OPTION
from src.Level import Level
from src.Menu import Menu


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))

    def run(self, ):

        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                level = Level(self.window, 'Level1')
                level_return = level.run()
            elif menu_return == MENU_OPTION[2]:
                pygame.quit()
                quit()
