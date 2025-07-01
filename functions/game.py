# Module Imports
import pygame as pg

import pygame.mixer as mixer

import functions.functions as functions 

import data.assets as assets    

# Game Variables

def transicion_get_ready(screen):
    from data.assets import background
    fade = pg.Surface((800, 600))
    fade.fill((0, 0, 0))
    for alpha in range(0, 255, 10):
        fade.set_alpha(alpha)
        screen.blit(background, (0, 0))
        screen.blit(fade, (0, 0))
        pg.display.update()
        pg.time.delay(20)
    # Mostrar mensaje "Get ready..."
    font = pg.font.Font("assets\BPdotsSquareBold.otf", 70)
    text = font.render("Get ready...", True, (0, 255, 0))
    screen.fill((0, 0, 0))
    screen.blit(text, (190, 250))
    pg.display.update()
    pg.time.delay(1500)
    pg.mixer.music.stop()
    pg.mixer.music.load("assets\musicajuego.mp3")
    pg.mixer.music.play(-1)
    pg.mixer.music.set_volume(0.2)

def refresh_grid(window, CELLSIZE, grid, cells_already_fire, successful_cells):
    # Dibuja solo la cuadrícula del jugador
    functions.draw_grid(window, CELLSIZE, grid, cells_already_fire, successful_cells)
    
'''
PARA PONER LAS IMAGENES Y QUE CUADRAN QUE LAS CORDENADAS DE LA POS, HACER QUE CUANDO HAGAMOS REC(IMAGEN), PONGASMOS LA POSICION INICIAL EN UNA POS RANDOM
Y QUE LA POS FINAL SEA, SI ES POR EJEMPLO EL BARCO X3, POS INICIAL.X + (50.3) INCLUSIVE
'''

# Player Initialization

# Main Game loop
def start(screen, dificult, CELLSIZE, ROWS, COLS):

    #ADAPTAR EL JUEGO A LA dificult
    CELLSIZE = (CELLSIZE//dificult)
    ROWS = ROWS * dificult
    COLS = COLS * dificult

    #FONDO
    background = pg.image.load('assets\playbackground.png').convert()
    background = pg.transform.scale(background, (820, 600))

    #FUNCIONES DEL JUEGO
    grid = functions.start_matriz(ROWS, COLS, 0)
    cells_already_fire = []
    successful_cells = []
    cord = functions.gen_cords(grid, CELLSIZE)
    ships = functions.put_ships(dificult, COLS, ROWS, grid, cord)  
    print(ships)
    functions.show_matriz(grid)

    POINTS = 0

    run = True
    #FUNCION MUTEAR
    muted = False

    while run == True:
        screen.blit(background, [0, 0])
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            posi = (0, 0)
            impact = None
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    posi = (event.pos)

                    impact = functions.check_impact(cord, posi, cells_already_fire, ships, CELLSIZE, grid, successful_cells)

                    if impact:
                        POINTS += 5
                        print("¡impact! POINTS:", POINTS)
                        assets.sonido_barco.play()
                        assets.sonido_barco.set_volume(0.1)

                    elif impact == False:
                        POINTS -= 1
                        print("Disparo fallido", POINTS)
                        assets.sonido_agua.play()
                        assets.sonido_agua.set_volume(0.1)

                #BOTONES
                    #RESTART
                    if 5 <= posi[0] <= 130 and 135 <= posi[1] <= 159:
                        grid = functions.start_matriz(ROWS, COLS, 0)
                        cells_already_fire = []
                        successful_cells = []
                        cord = functions.gen_cords(grid, CELLSIZE)
                        ships = functions.put_ships(dificult, COLS, ROWS, grid, cord)
                        POINTS = 0
                    #MENU
                    elif 5 <= posi[0] <= 130 and 165 <= posi[1] <= 189:
                        run = False
                    #SONIDO
                    if 0 <= posi[0] <= 40 and 560 <= posi[1] <= 600:
                        muted = not muted
                        if muted:
                            mixer.music.set_volume(0)
                        else:
                            mixer.music.set_volume(0.2)
                         
        POINTS += functions.check_ships(ships)
        functions.show_points(POINTS, screen)
        status = functions.check_status(ships)         
        refresh_grid(screen, CELLSIZE, grid, cells_already_fire, successful_cells)

        if status:
            run = functions.save_score(screen, POINTS)
        if muted:
            screen.blit(assets.logo_sonidono, (0, 560))
        else:
            screen.blit(assets.logo_sonidosi, (0, 560))
            
        pg.display.flip()
