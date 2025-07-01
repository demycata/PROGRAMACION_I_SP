import pygame as pg
import settings as config
import pygame.mixer as mixer

from interface.menu import *
from interface.menu_levels import *
from interface.menu_score import *

import functions.game as game
import data.assets as assets

# Inicializar Pygame
pg.init()
mixer.init()
clock = pg.time.Clock()

# Titulo 
pg.display.set_caption("BATTLESHIP PRO MAX")

# Icono
pg.display.set_icon(assets.icon)

# Creando la ventana
screen_resolution = (config.SCREENWIDTH, config.SCREENHEIGHT)
screen = pg.display.set_mode((screen_resolution))

dificult = 1

# Bucle principal del juego-----------------------------------------------------------------------------
while True:
    clock.tick(83)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

        opcion = menu(screen)

        match opcion:
            case 1:
                dificult = menu_levels(screen, clock)
            case 2:
                game.transicion_get_ready(screen)
                game.start(screen, dificult, config.CELLSIZE, config.ROWS, config.COLS)
            case 3:
                menu_score(screen)
        
    pg.display.flip()