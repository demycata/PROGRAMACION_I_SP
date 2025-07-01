import random

def mostrar_datos(lista_a:list, lista_b:list, lista_c:list) -> None:
    '''
    Función para mostrar los datos de tres listas en formato tabular.
    Args:
        lista_a: list: Primera lista de datos.
        lista_b: list: Segunda lista de datos.
        lista_c: list: Tercera lista de datos.
    '''

    for i in range(len(lista_a)):

        if len(lista_a[i]) < 8:
            print(f"{lista_a[i]}\t\t{lista_b[i]}\t{lista_c[i]}")
        else:
            print(f"{lista_a[i]}\t{lista_b[i]}\t{lista_c[i]}")    

def copiar_lista(lista_a:list, lista_b:list)->list:
    '''
    Función para copiar los elementos de dos listas en nuevas listas.
    Args:
        lista_a: list: Primera lista de datos.
        lista_b: list: Segunda lista de datos.
    Returns:
        tuple: Dos listas nuevas con los elementos de lista_a y lista_b.
    '''
    nombres_originales = [-1] * len(lista_a)
    edades_originales = [-1] * len(lista_b)

    for i in range(len(lista_a)):
        nombres_originales[i] = lista_a[i]
        edades_originales[i] = lista_b[i]
    
    return nombres_originales, edades_originales

def ordenar_ascendente(lista_a:list, lista_b:list, lista_c:list) -> None:
    '''
    Función para ordenar tres listas en orden ascendente según la tercera lista.
    Args:
        lista_a: list: Primera lista de datos.
        lista_b: list: Segunda lista de datos.
        lista_c: list: Tercera lista de datos.
    '''

    for i in range(0, len(lista_a)-1, 1):
        
        for j in range(i + 1, len(lista_a), 1):
            
            if lista_c[i] > lista_c[j]:
            
                edad_auxiliar = lista_b[i]
                lista_b[i] = lista_b[j]
                lista_b[j] = edad_auxiliar

                nombre_auxiliar = lista_a[i]
                lista_a[i] = lista_a[j]
                lista_a[j] = nombre_auxiliar

                genero_auxiliar = lista_c[i]
                lista_c[i] = lista_c[j]
                lista_c[j] = genero_auxiliar
#2 criterio 
            elif lista_c[i] == lista_c[j]:
                if lista_a[i] > lista_a[j]:
                    edad_auxiliar = lista_b[i]
                    lista_b[i] = lista_b[j]
                    lista_b[j] = edad_auxiliar

                    nombre_auxiliar = lista_a[i]
                    lista_a[i] = lista_a[j]
                    lista_a[j] = nombre_auxiliar

def ordenar_descendente(lista_a:list, lista_b:list, lista_c:list) -> None:
    '''
    Función para ordenar tres listas en orden descendente según la tercera lista.
    Args:
        lista_a: list: Primera lista de datos.
        lista_b: list: Segunda lista de datos.
        lista_c: list: Tercera lista de datos.
    '''

    for i in range(0, len(lista_a)-1, 1):
        
        for j in range(i + 1, len(lista_a), 1):
            
            if lista_c[i] < lista_c[j]:
            
                edad_auxiliar = lista_b[i]
                lista_b[i] = lista_b[j]
                lista_b[j] = edad_auxiliar

                nombre_auxiliar = lista_a[i]
                lista_a[i] = lista_a[j]
                lista_a[j] = nombre_auxiliar

                genero_auxiliar = lista_c[i]
                lista_c[i] = lista_c[j]
                lista_c[j] = genero_auxiliar
#2 criterio 
            elif lista_c[i] == lista_c[j]:
                if lista_a[i] < lista_a[j]:
                    edad_auxiliar = lista_b[i]
                    lista_b[i] = lista_b[j]
                    lista_b[j] = edad_auxiliar

                    nombre_auxiliar = lista_a[i]
                    lista_a[i] = lista_a[j]
                    lista_a[j] = nombre_auxiliar

def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any) -> list:
    '''
    Función para inicializar una matriz con un valor inicial.
    Args:
        cantidad_filas: int: Cantidad de filas de la matriz.
        cantidad_columnas: int: Cantidad de columnas de la matriz.
        valor_inicial: str | int: Valor inicial con el que se llenará la matriz.
    Returns:
        list: Matriz inicializada con el valor inicial.
    '''
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

def mostrar_matriz(matriz:list) -> None:
    """
    Función para mostrar una matriz en la consola.
    Args:
        matriz: list: Matriz a mostrar.
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end = " ")
        print("")

def buscar_datos(lista:list,ref:int) -> int:
    """
    Función para buscar un elemento en una lista y devolver su índice.
    Args:
        lista: list: Lista en la que se busca el elemento.
        ref: int: Elemento a buscar en la lista.
    Returns:
        int: Índice del elemento encontrado, o None si no se encuentra.
    """
    indice = None
    for index in range (len(lista)): 
        if lista[index] == ref:
            indice = index
            break
    return indice

def cargar_datos_secuencial(nombres: list, edades: list, generos: list, estaturas: list, dnis: list, tamano: int) -> None:
    '''
    Función para cargar datos de estudiantes en listas.
    Args:
        nombres: list: Lista de nombres de los estudiantes.
        edades: list: Lista de edades de los estudiantes.
        generos: list: Lista de géneros de los estudiantes.
        estaturas: list: Lista de estaturas de los estudiantes.
        dnis: list: Lista de DNIs de los estudiantes.
        tamano: int: Tamaño de las listas.
    '''
    for i in range(tamano):
        nombres[i] = input("Nombre: ")
        while nombres[i] == "x":
            nombres[i] = input("Nombre: ")

        edades[i] = int(input("Edad: "))
        while edades[i] < 0 or edades[i] > 100:
            edades[i] = int(input("Edad: "))

        generos[i] = input("Genero: ")
        estaturas[i] = input("Estatura: ")
        dnis[i] = input("DNI: ")

def suma_pares(lista:list) -> int:
    """
    Función para calcular la suma de los números pares en una lista.
    Args:
        lista: list[int]: Lista de números enteros.
    Returns:
        int: Suma de los números pares en la lista.
    """
    pares = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            pares += lista[i]
    return pares

def pares(lista:list) -> int:
    """
    Función para contar la cantidad de números pares en una lista.
    Args:
        lista: list[int]: Lista de números enteros. 
    Returns:
        int: Cantidad de números pares en la lista.
    """
    pares = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            pares += 1
    return pares

def neg(lista:list) -> int:
    """
    Función para contar la cantidad de números negativos en una lista.
    Args:
        lista: list[int]: Lista de números enteros.
    Returns:
        int: Cantidad de números negativos en la lista.
    """
    negativos = 0
    for i in range(len(lista)):
        if lista[i] < 0:
            negativos +1
    return negativos

def positivos(lista:list) -> int:
    """
    Función para contar la cantidad de números positivos en una lista.
    Args:
        lista: list[int]: Lista de números enteros.
    Returns:
        int: Cantidad de números positivos en la lista.
    """
    positivos = 0
    for i in range(len(lista)):
        if lista[i] > 0:
            positivos += 1
    return positivos

def mayor_inpar(lista:list) -> int | None:
    """
    Función para encontrar el número impar más grande en una lista.
    Args:
        lista: list[int]: Lista de números enteros.
    Returns:
        int | None: El número impar más grande en la lista, o None si no hay impares.
    """
    mayor = None
    for i in range(len(lista)):
        if lista[i] % 2 != 0:
            if mayor == None:
                mayor = lista[i]
            elif lista[i] > mayor:
                mayor = lista[i]
    return mayor

def get_int(mensaje: str, mensaje_error: str, minimo:int, maximo:int, reintentos:int) -> int | None:
    """
    Función para pedir un número entero dentro de un rango específico.
    Args:
        mensaje: str: Mensaje que se muestra al usuario para ingresar el número.
        mensaje_error: str: Mensaje de error que se muestra si la validación falla.
        minimo: int: Valor mínimo permitido.
        maximo: int: Valor máximo permitido.
        reintentos: int: Número de intentos permitidos para ingresar un valor válido.
    Returns:
        int | None: Devuelve el número entero ingresado si es válido, de lo contrario None.
    """
    flag = None
    for i in  range(reintentos):
        num = input(mensaje)
        flag, flag_2 = validate_number(num, maximo, minimo)
        if flag == None or flag_2 == True: 
            print(mensaje_error)
        else:
            break
    return flag

def validate_length(palabra:str, longitud:int) -> str | None:
    """
    Función para validar la longitud de una cadena de texto.
    Args:
        palabra: str: Cadena de texto a validar.
        longitud: int: Longitud exacta que debe tener la cadena.
    Returns:
        str | None: Devuelve la cadena si es válida, de lo contrario None.
    """
    flag = None
    letras = len(palabra)
    if letras == longitud:
        flag = palabra
    return flag

def validate_number(num:int, maximo:int, minimo:int,) -> int | None:
    '''
    Función para validar un número dentro de un rango específico.
    Args:
        num: str: Número a validar.
        maximo: int: Valor máximo permitido.
        minimo: int: Valor mínimo permitido.
    Returns:
        int | None: Devuelve el número entero si es válido, de lo contrario None.
    '''
    numero = None
    flag_2 = None
    no_digit = False
    for elemento in num:
        if elemento == '.':
            flag_2 = True
        if ord(elemento) < 44 or ord(elemento) > 57:
            no_digit = True   
            break
    if no_digit == False:
        if flag_2 == True:
            num = float(num)
        else:
            num = int(num)
        if num > maximo or num < minimo:
            numero = None
        else:
            numero = num
    return numero, flag_2

def get_float(mensaje: str, mensaje_error: str, minimo:int, maximo:int, reintentos:int) -> float | None:
    """
    Función para validar un número flotante dentro de un rango específico.
    Args:
        mensaje: str: Mensaje que se muestra al usuario para ingresar el número.
        mensaje_error: str: Mensaje de error que se muestra si la validación falla.
        minimo: int: Valor mínimo permitido.
        maximo: int: Valor máximo permitido.
        reintentos: int: Número de intentos permitidos para ingresar un valor válido.
    Returns:
        int | None: Devuelve el número flotante ingresado si es válido, de lo contrario None.
    """
    flag = None
    print(mensaje)
    for i in  range(reintentos):
        num = input(f'Ingrese un float entre {minimo} y {maximo}, tenes {reintentos} intentos: ')
        flag, flag_2 = validate_number(num, maximo, minimo)
        if flag == None:
            print(mensaje_error)
        else:
            flag = float(flag)
            break
    return flag
    
def get_str(mensaje:str, mensaje_error:str, longitud:int, reintentos:int) -> str |None: 
    """
    Función para validar una cadena de texto con una longitud específica.
    Args:
        mensaje: str: Mensaje que se muestra al usuario para ingresar la cadena.
        mensaje_error: str: Mensaje de error que se muestra si la validación falla.
        longitud: int: Longitud exacta que debe tener la cadena.
        reintentos: int: Número de intentos permitidos para ingresar un valor válido.
    Returns:
        str | None: Devuelve la cadena ingresada si es válida, de lo contrario None.
    """
    flag = None
    print(mensaje)
    for i in  range(reintentos):
        palabra = input(f'Ingrese una string con un maximo de {longitud} caracteres, tenes {reintentos} intentos: ')
        flag = validate_length(palabra, longitud)
        if flag == None:
            print(mensaje_error)
        else:
            break
    return flag

def crear_lista(tamano:int, valor_inicial:any) -> list:
    '''
    Función para crear una lista de un tamaño específico y llenarla con un valor inicial.
    Args:
        tamano: int: Tamaño de la lista a crear.
        valor_inicial: str | int: Valor inicial con el que se llenará la lista.
    Returns:
        list: Lista creada con el valor inicial.
    '''
    lista = [valor_inicial  ] * tamano
    return lista

def remplazar_nombres(lista_nombres, nombre_nuevo, nombre_viejo):
    remplace = 0
    for i in range(len(lista_nombres)):
        if lista_nombres[i] == nombre_viejo:
            lista_nombres[i] = nombre_nuevo
            remplace += 1
    print(lista_nombres)    
    return remplace

def indentificar_numeros(cadena:str)-> bool:
    '''
    Función para identificar si una cadena contiene solo números.
    Args:
        cadena: str: Cadena a verificar.
    Returns:
        bool: True si la cadena contiene solo números, False en caso contrario.
    '''
    hay = None
    for i in cadena:
        if ord(i) < 47 or ord(i) > 57:
            hay = False
        else:
            hay = True
    return hay

def es_cuadrado_magico(matriz:list) -> bool:
    '''
    Función para verificar si una matriz es un cuadrado mágico.
    Args:
        matriz: list[list[int]]: Matriz a verificar.
    Returns:
        bool: True si la matriz es un cuadrado mágico, False en caso contrario.
    '''
    es_magico = None
    n = len(matriz)
    constante_magica = n * (n**2 + 1) // 2

    # Suma de filas
    for fila in matriz:
        if sum(fila) != constante_magica:
            es_magico = False

    # Suma de columnas
    for columnas in range(n):
        if sum(matriz[fila][columnas] for fila in range(n)) != constante_magica:
            es_magico = False

    # Suma de diagonales
    if sum(matriz[i][i] for i in range(n)) != constante_magica:
        es_magico = False
    if sum(matriz[i][n - i - 1] for i in range(n)) != constante_magica:
        es_magico = False
    
    es_magico = True 

    return es_magico

def generar_lista_legajos()-> list:
    '''
    Genera una lista de legajos aleatorios entre 10000 y 99999.
    Devuelve una lista de legajos.
    '''
    lista_legajos = [0] * 30 

    for i in range(30):
        if lista_legajos[i] == 0:
            legajo = random.randint(10000, 99999)
            lista_legajos[i] = legajo
    return lista_legajos

def validar_legajo(legajo:int, legajos:list)-> bool:
    '''
    Función para validar si un legajo ya existe en la lista de legajos.
    Args:
        legajo: int: Legajo a validar.
        legajos: list: Lista de legajos existentes.
    Returns:
        bool: True si el legajo es válido (no existe en la lista), False si ya existe.
    '''
    valido = True
    for i in range(len(legajos)):
        if legajos[i] == legajo:
            valido = False
            break
    return valido

def lower(texto: str) -> str:
    '''
    Función para convertir una cadena de texto a minúsculas.
    Args:
        texto: str: Cadena de texto a convertir.
    Returns:
        str: Cadena de texto convertida a minúsculas.
    '''
    resultado = ""
    for letra in texto:
        codigo = ord(letra)
        if 65 <= codigo <= 90:
            resultado += chr(codigo + 32)
        else:
            resultado += letra
    return resultado

def upper(texto: str) -> str:
    '''
    Función para convertir una cadena de texto a mayúsculas.
    Args:
        texto: str: Cadena de texto a convertir.
    Returns:
        str: Cadena de texto convertida a mayúsculas.
    '''
    resultado = ""
    for letra in texto:
        codigo = ord(letra)
        if 97 <= codigo <= 122:
            resultado += chr(codigo - 32)
        else:
            resultado += letra
    return resultado

def get_name()-> str:
    '''
    Función para obtener el nombre del usuario.
    Devuelve el nombre ingresado por el usuario.
    '''
    while True:
        nombre = input("Nombre ➢  ")
        es_valido = indentificar_numeros(nombre)
        if es_valido == True:
                print('ERROR | Ingrese un Nombre valido.')
        else:
             break
    return nombre

def get_genero()-> str:
    '''
    Función para obtener el género del usuario.
    Devuelve 'M' para masculino, 'F' para femenino o 'X' para no binario.
    '''
    while True:
        genero = input("Genero ('M'/'F'/'X') ➢  ")
        genero = upper(genero)
        if genero == 'M' or genero == 'F' or genero == 'X':
            break
        else:
            print('Ingrese un genero valido')
    return genero

def get_legajo(legajos:list)-> int:
    '''
    Función para obtener un legajo único.
    Args:
        legajos: list: Lista de legajos existentes.
    Returns:
        int: Legajo único ingresado por el usuario.
    '''
    while True:
        legajo = get_int('Legajo ➢  ', 'ERROR AL INGRESAR TU DATO', 10000, 99999, 100)
        es_valido = validar_legajo(legajo, legajos)
        if es_valido == True:
            break
        else:
            print('ESE LEGAJO YA EXISTE\n')
    return legajo

def leer_csv(archivo):
    matriz = []

    for linea in archivo:

        linea = linea.rstrip('\n')
        fila = []
        valores = linea.split(',')

        for valor in valores:

            if valor.isdigit():
                fila.append(int(valor))
            else:
                fila.append(valor)

        matriz.append(fila)
        
    return matriz