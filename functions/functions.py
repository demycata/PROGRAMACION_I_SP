
import pygame as pg 
import random
import data.assets as assets


def start_matriz(ROWS:int, COLS:int, val_ini:any) -> list:
    '''
    Función para inicializar una matriz con un valor inicial.
    Args:
        ROWS: int: Cantidad de ROWS de la matriz.
        COLS: int: Cantidad de COLS de la matriz.
        val_ini: str | int: Valor inicial con el que se llenará la matriz.
    Returns:
        list: Matriz inicializada con el valor inicial.
    '''
    matriz = []
    for i in range(ROWS):
        fila = [val_ini] * COLS
        matriz += [fila]
    return matriz

def show_matriz(matriz:list) -> None:
    """
    Función para mostrar una matriz en la consola.
    Args:
        matriz: list: Matriz a mostrar.
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end = " ")
        print("")

def gen_cords(grid, CELLSIZE):
    cord = []
    start_x = 192
    start_y = 76
    for i in range(len(grid)):
        fila = []
        for j in range(len(grid[i])):
            pos_x = start_x + j * CELLSIZE
            pos_y = start_y + i * CELLSIZE
            fila.append((pos_x, pos_y))
        cord.append(fila)
    return cord

def draw_grid(display, cellsize, grid, cells_already_fire, successful_cells):
    """Dibuja solo la cuadrícula del jugador en la pantalla"""
    cell = pg.transform.scale(assets.cell, (cellsize, cellsize))
    agua = pg.transform.scale(assets.agua, (cellsize, cellsize))
    ship = pg.transform.scale(assets.ship, (cellsize, cellsize))
    start_x = 192
    start_y = 76
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pos_x = start_x + j * cellsize
            pos_y = start_y + i * cellsize
            if (pos_x, pos_y) in successful_cells: # ROJO si ya estan disparadas
                display.blit(ship, (pos_x, pos_y))
            elif (pos_x, pos_y) in cells_already_fire: # AZUL si ya estan disparadas
                display.blit(agua, (pos_x, pos_y))
            else:   # si no las pone en blanco
                display.blit(cell, (pos_x, pos_y))

def cords_ship(grid, tam_ship, cord, COLS, ROWS):
    """
    Coloca un ship horizontal de tamaño tam_ship en una fila aleatoria,
    verificando que haya espacio suficiente (solo ceros).
    """
    put = False
    coords_ship = []

    while put == False:
        fila = random.randint(0, ROWS - tam_ship)
        col_inicio = random.randint(0, COLS - 1)
        # Verifica si hay espacio suficiente
        espacio_libre = check_space_free(tam_ship, grid, col_inicio, fila)
        if espacio_libre == True:
            for i in range(tam_ship):
                grid[fila + i][col_inicio] = 1
                coords_ship.append((cord[fila + i][col_inicio]))
            put = True

    return coords_ship    
    
def gen_ships(grid, cord, ship, cant, dificultad, ships, COLS, ROWS):
    for i in range(cant*dificultad):
        ship_dic = {}
        cords = cords_ship(grid, ship, cord, COLS, ROWS)
        ship_dic['Cords'] = cords
        ship_dic['Tam'] = ship
        ship_dic['hp'] = ship
        print(ship_dic)
        ships.append(ship_dic)

def put_ships(dificultad, COLS, ROWS, grid, cord):
    if dificultad == 4:
        dificultad = 3
    ships = []
    # CANTIDAD DE CASILLAS QUE OCUPAN
    submarionos = 1
    destructors = 2
    cruceros = 3
    acorazado = 4
    # CANTIDAD DE ships
    cant_submarionos = 4
    cant_destructors = 3
    cant_cruceros = 2
    cant_acorazado = 1
    gen_ships(grid, cord, submarionos, cant_submarionos, dificultad, ships, COLS, ROWS) #GENERA SUBMARINOS
    gen_ships(grid, cord, destructors, cant_destructors, dificultad, ships, COLS, ROWS) #GENERA DESTRUCTORES
    gen_ships(grid, cord, cruceros, cant_cruceros, dificultad, ships, COLS, ROWS) #GENERA CRUCEROS
    gen_ships(grid, cord, acorazado, cant_acorazado, dificultad, ships, COLS, ROWS) #GENERA ACORAZADOS
    return ships

def check_space_free(tam_ship, grid, col_inicio, fila):
        espacio_libre = True
        for i in range(tam_ship):
            if grid[fila + i][col_inicio] != 0:
                espacio_libre = False
                break
        return espacio_libre

def check_impact_ships(x_y, ships, grid, cord, successful_cells):
    impact = False
    for ship in ships:
        if x_y in ship['Cords'] and ship['hp'] > 0:
            print("¡El mouse está dentro de esta celda!")
            successful_cells.append(x_y)
            impact = True
            for i in range(len(grid)):              #esto hace cambio el 1 del grid a 0 si toca la celda
                for x in range(len(grid[i])):
                    if cord[i][x] == x_y:
                        grid[i][x] = 0 
            ship['hp'] -= 1
    return impact

def check_impact(cord, posi, cells_already_fire, ships, CELLSIZE, grid, successful_cells):
    impact = None
    for i in cord:
        for x_y in i: # cada celda es (x, y)
            rect = pg.Rect(x_y[0], x_y[1], CELLSIZE, CELLSIZE)
            if rect.collidepoint(posi):
                if x_y not in cells_already_fire:
                    impact = check_impact_ships(x_y, ships, grid, cord, successful_cells)
                    cells_already_fire.append(x_y)
                elif x_y in cells_already_fire:
                    print('Ya disparaste')  
                    break
     
    return impact

def check_ships(ships):
    """
    Verifica si la partida ha terminado.
    Retorna True si todos los ships han sido hundidos, False en caso contrario.
    """
    points = 0
    for ship in ships:
        if ship['hp'] <= 0:
            points += ship['Tam'] * 10
            ships.remove(ship) 
    return points

def check_status(ships):
    end = False
    if len(ships) == 0:
        end = True
    return end
    
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
    
def show_points(points, display):
    fuente = pg.font.Font("assets\BPdotsSquareBold.otf", 30)
    if points < 0:
        points = points * -1
        texto = fuente.render(f'-{points:04d}', True, (0, 255, 0))
    else:
        texto = fuente.render(f'{points:04d}', True, (0, 255, 0))
    display.blit(texto, (25, 70))

def save_score(screen, points):
    name = ''
    font = pg.font.Font("assets\BPdotsSquareBold.otf", 50)
    cuadro = pg.image.load('assets\cuadro.png')
    run = True
    while run:
        screen.blit(cuadro, (100, 0))
        text = font.render(f"{name}", True, (0, 255, 0))
        screen.blit(text, (200, 300))
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE:
                    name = name[0:-1] 
                elif event.key == pg.K_RETURN:
                    run = False
                else:
                    if len(name) <= 6:
                        name += event.unicode # unicode contiene el caracter que el usuario presiono con el teclado
        pg.display.flip()

    with open('data\puntos.csv', 'a') as score:
        score.write(f'{name},{points}\n')
    return False