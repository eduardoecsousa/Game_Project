import pygame

WIN_WIDTH = 600
WIN_HIGTH = 480

COLOR_BLUE = (7, 205, 167)
COLOR_WHITE = (255, 255, 255)
COLOR_GREEN = (0, 128, 0)
COLOR_CYAN = (0, 128, 128)

MENU_OPTION = ('New Game', 'Score', 'Quit')

COLOR_YELLOW = (214, 174, 14)

EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

ENTITY_HEAlTH = {
    'background-game': 999,
    'Principal': 300,
    'inimigo': 50,
    'inimigo2': 30,
    'PlayerShot': 1,
    'EnemyShot': 1
}

ENTITY_DAMAGE = {
    'background-game': 0,
    'Principal': 1,
    'inimigo': 1,
    'inimigo2': 1,
    'PlayerShot': 20,
    'EnemyShot': 20
}

ENTITY_SCORE = {
    'background-game': 0,
    'Principal': 0,
    'inimigo': 100,
    'inimigo2': 100,
    'PlayerShot': 0,
    'EnemyShot': 0
}
