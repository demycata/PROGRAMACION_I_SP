
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

def gen_cords(grid:list, CELLSIZE:int) -> list:
    """Genera una lista de coordenadas para cada celda de la cuadrícula.
    Args:
        grid: list: La cuadrícula que contiene los valores de las celdas.
        CELLSIZE: int: El tamaño de cada celda en píxeles.
    Returns:
        list: Una lista de listas que contiene las coordenadas (x, y) de cada celda.
    """
    cord = []
    start_x = 192
    start_y = 76
    for i in range(len(grid)):
        fila = []
        for j in range(len(grid[i])):
            pos_x = start_x + j * CELLSIZE # Calcula la posición x de la celda y cada iteración suma el tamaño de la celda, se va corriendo j celdas a la derecha
            pos_y = start_y + i * CELLSIZE # Calcula la posición y de la celda y cada iteración suma el tamaño de la celda, se va corriendo i celdas hacia abajo
            fila.append((pos_x, pos_y)) #agrega las coordenadas (pos_x, pos_y) a la fila
        cord.append(fila)
    return cord

def draw_grid(screen:any, cellsize:int, grid:list, cells_already_fire:list, successful_cells:list) -> None:
    '''
    Dibuja la cuadrícula del juego en la pantalla.
    Args:
        screen: pygame.Surface: La superficie donde se dibujará la cuadrícula.
        cellsize: int: El tamaño de cada celda en píxeles.
        grid: list: La cuadrícula que contiene los valores de las celdas.
        cells_already_fire: list: Lista de celdas que ya han sido disparadas.
        successful_cells: list: Lista de celdas que han sido impactadas exitosamente.
    '''
    cell = pg.transform.scale(assets.cell, (cellsize, cellsize))
    agua = pg.transform.scale(assets.agua, (cellsize, cellsize))
    ship = pg.transform.scale(assets.ship, (cellsize, cellsize))
    start_x = 192
    start_y = 76
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pos_x = start_x + j * cellsize # Calcula la posición x de la celda y cada iteración suma el tamaño de la celda, dibuja j celdas a la derecha
            pos_y = start_y + i * cellsize # Calcula la posición y de la celda y cada iteración suma el tamaño de la celda, dibuja i celdas hacia abajo
            if (pos_x, pos_y) in successful_cells: # ROJO si ya estan disparadas
                screen.blit(ship, (pos_x, pos_y))
            elif (pos_x, pos_y) in cells_already_fire: # AZUL si ya estan disparadas
                screen.blit(agua, (pos_x, pos_y))
            else:   # si no las pone en blanco
                screen.blit(cell, (pos_x, pos_y))

def cords_ship(grid:list, tam_ship:int, cord:list, COLS:int, ROWS:int) -> list:
    '''Genera las coordenadas de un barco en la cuadrícula.
    Args:
        grid: list: La cuadrícula que contiene los valores de las celdas.
        tam_ship: int: El tamaño del barco.
        cord: list: Lista de coordenadas de cada celda.
        COLS: int: Cantidad de columnas en la cuadrícula.
        ROWS: int: Cantidad de filas en la cuadrícula.
    Returns:
        list: Una lista de coordenadas (x, y) donde se colocará el barco.
    '''
    put = False
    coords_ship = []

    while put == False:
        fila = random.randint(0, ROWS - tam_ship) # Selecciona una fila aleatoria donde colocar el barco, el menos es porque el barco no puede salir de la cuadrícula
        col_inicio = random.randint(0, COLS - 1)
        # Verifica si hay espacio suficiente
        espacio_libre = check_space_free(tam_ship, grid, col_inicio, fila)
        if espacio_libre == True:
            for i in range(tam_ship):
                grid[fila + i][col_inicio] = 1
                coords_ship.append((cord[fila + i][col_inicio])) # agrega las coordenadas del barco a la lista con el indice de la fila y columna de la matriz
            put = True

    return coords_ship    
    
def gen_ships(grid:list, cord:list, tam_ship:int, cant:int, dificultad:int, ships:list, COLS:int, ROWS:int) -> None:
    '''Genera los barcos en la cuadrícula y genera un diccionario con sus coordenadas y tamaño, despues las agrega a la lista de barcos.
    Args:
        grid: list: La cuadrícula que contiene los valores de las celdas.
        cord: list: Lista de coordenadas de cada celda.
        ship: int: El tamaño del barco.
        cant: int: Cantidad de barcos a generar.
        dificultad: int: Nivel de dificultad del juego.
        ships: list: Lista donde se almacenarán los barcos generados.
        COLS: int: Cantidad de columnas en la cuadrícula.
        ROWS: int: Cantidad de filas en la cuadrícula.
    '''
    for i in range(cant*dificultad):
        ship_dic = {}
        cords = cords_ship(grid, tam_ship, cord, COLS, ROWS)
        ship_dic['Cords'] = cords
        ship_dic['Tam'] = tam_ship
        ship_dic['hp'] = tam_ship
        print(ship_dic)
        ships.append(ship_dic)

def put_ships(dificultad:int, COLS:int, ROWS:int, grid:list, cord:list) -> list:
    '''Genera los barcos en la cuadrícula según el nivel de dificultad y los agreaga los diccionarios de barcos a una lista.
    Args:
        dificultad: int: Nivel de dificultad del juego.
        COLS: int: Cantidad de columnas en la cuadrícula.
        ROWS: int: Cantidad de filas en la cuadrícula.
        grid: list: La cuadrícula que contiene los valores de las celdas.
        cord: list: Lista de coordenadas de cada celda.
    Returns:
        list: Lista de barcos generados con sus coordenadas y tamaño.
    '''
    if dificultad == 4:
        dificultad = 3
    ships = [] #lista de diccionarios que contiene los barcos
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

def check_space_free(tam_ship:int, grid:list, col_inicio:int, fila:int) -> bool:
    """Verifica si hay espacio suficiente para colocar un barco en la cuadrícula.
    Args:
        tam_ship: int: El tamaño del barco.
        grid: list: La cuadrícula que contiene los valores de las celdas.
        col_inicio: int: La columna de inicio donde se intentará colocar el barco.
        fila: int: La fila donde se intentará colocar el barco.
    Returns:
        bool: True si hay espacio suficiente, False en caso contrario.
    """
    espacio_libre = True
    for i in range(tam_ship):
        if grid[fila + i][col_inicio] != 0:
            espacio_libre = False
            break
    return espacio_libre

def check_impact_ships(x_y:tuple, ships:list[dict], grid:list, cord:list, successful_cells:list) -> bool:
    """Verifica si el disparo impacta en un barco.
    Args:
        x_y: tuple: Coordenadas (x, y) del disparo.
        ships: list[dict]: Lista de barcos, cada uno representado por un diccionario
        grid: list: La cuadrícula que contiene los valores de las celdas.
        cord: list: Lista de coordenadas de cada celda.
        successful_cells: list: Lista de celdas que han sido impactadas exitosamente.
    Returns:
        bool: True si el disparo impacta en un barco, False en caso contrario.
    """
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

def check_impact(cord:list, posi:tuple, cells_already_fire:list, ships:list, CELLSIZE:list, grid:list, successful_cells:list) -> bool:
    """Verifica si el disparo impacta en un barco.
    Args:
        cord: list: Lista de coordenadas de cada celda.
        posi: tuple: Posición del disparo (x, y).
        cells_already_fire: list: Lista de celdas que ya han sido disparadas.
        ships: list[dict]: Lista de barcos, cada uno representado por un diccionario.
        CELLSIZE: int: Tamaño de cada celda en píxeles.
        grid: list: La cuadrícula que contiene los valores de las celdas.
        successful_cells: list: Lista de celdas que han sido impactadas exitosamente.
    Returns:
        bool: True si el disparo impacta en un barco, False en caso contrario.
    """
    impact = None
    for i in cord:
        for x_y in i: # cada celda es (x, y)
            rect = pg.Rect(x_y[0], x_y[1], CELLSIZE, CELLSIZE) # crea un rectangulo con las coordenadas de la celda y el tamaño de la celda
            if rect.collidepoint(posi): # verifica si el mouse esta dentro del rectangulo de la celda
                if x_y not in cells_already_fire:
                    impact = check_impact_ships(x_y, ships, grid, cord, successful_cells)
                    cells_already_fire.append(x_y)
                elif x_y in cells_already_fire: 
                    break
    return impact

def check_ships(ships:list) -> int:
    """Verifica el estado de los barcos y calcula los puntos obtenidos por los barcos hundidos.
    Args:
        ships: list[dict]: Lista de barcos, cada uno representado por un diccionario.
    Returns:
        int: Puntos obtenidos por los barcos hundidos.
    """
    points = 0
    for ship in ships:
        if ship['hp'] <= 0:
            points += ship['Tam'] * 10
            ships.remove(ship) 
    return points

def check_status(ships:list) -> bool:
    """Verifica si quedan barcos en el juego.
    Args:
        ships: list[dict]: Lista de barcos, cada uno representado por un diccionario.
    Returns:
        bool: True si no quedan barcos, False en caso contrario.
    """
    end = False
    if len(ships) == 0:
        end = True
    return end
    
def show_points(points:int, screen:any) -> None:
    """Muestra los puntos obtenidos en la pantalla.
    Args:
        points: int: Puntos obtenidos.
        screen: pygame.Surface: La superficie donde se dibujarán los puntos.
    """
    fuente = pg.font.Font("assets\BPdotsSquareBold.otf", 30)
    if points < 0:
        points = points * -1
        texto = fuente.render(f'-{points:04d}', True, (0, 255, 0))
    else:
        texto = fuente.render(f'{points:04d}', True, (0, 255, 0))
    screen.blit(texto, (25, 70))

def save_score(screen:any, points:int) -> bool:
    """Guarda el puntaje del jugador en un archivo CSV.
    Args:
        screen: pygame.Surface: La superficie donde se dibujará la interfaz de guardado.
        points: int: Puntos obtenidos por el jugador.
    Returns:
        bool: False si se guarda el puntaje, True si se cancela el guardado. Esto detrendra el juego
    """
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