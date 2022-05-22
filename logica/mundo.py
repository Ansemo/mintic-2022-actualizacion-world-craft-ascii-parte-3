from .mods import *
from colorama import Fore, init

def cordenadas_aleatorias():
    filas = [[random.choice([i for i in range(0, 10)]) for i in range(0, 4)] for i in range(0, 4)]
    return filas


def crear_mundo():
    init()
    # print(cordenadas)
    filas = cordenadas_aleatorias()[0]
    columnas = cordenadas_aleatorias()[1]
    anchos = cordenadas_aleatorias()[2]
    largos = cordenadas_aleatorias()[3]
    # listas
    #
    # filas = [0, 3, 5, 6]
    # columnas = [1, 3, 11, 12]
    # anchos = [2, 9, 1, 4]
    # largos = [5, 2, 2, 1]

    # matriz
    matriz = []
    cont = 0
    for i in range(0, 18):
        matriz.append([0] * 18)
        for j in range(0, 18):

            if filas[0] <= i <= filas[0] + (largos[0] - 1) and columnas[0] <= j <= columnas[0] + (anchos[0] - 1):
                matriz[i][j] = Fore.GREEN + '#'
            elif filas[1] <= i <= filas[1] + (largos[1] - 1) and columnas[1] <= j <= columnas[1] + (anchos[1] - 1):
                matriz[i][j] = Fore.GREEN + '#'
            elif filas[2] <= i <= filas[2] + (largos[2] - 1) and columnas[2] <= j <= columnas[2] + (anchos[2] - 1):
                matriz[i][j] = Fore.GREEN + '#'
            elif filas[3] <= i <= filas[3] + (largos[3] - 1) and columnas[3] <= j <= columnas[3] + (anchos[3] - 1):
                matriz[i][j] = Fore.GREEN + '#'
            else:
                matriz[i][j] = Fore.WHITE + '-'

    return matriz



def insertar_creaturas_mapa(matriz,creaturas_generadas):
    entidades = creaturas_generadas
    # entidades = creaturas_activas(creaturas_generadas)
    cordenadas = []

    #"{'Tipo': 'Pasivo', 'Nombre': ('Gallina',), 'Simbolo': ('G',), 'Fila': 8, 'Columna': 11,'Fecha': datetime.datetime(2022, 5, 21, 18, 16, 32, 366122)}
    for i in entidades:
        cordenadas.append(((i["Fila"], i["Columna"]), i["Simbolo"][0], i["Tipo"]))

    for i in range(0, len(cordenadas)):
        print(cordenadas[i][0],' ',cordenadas[i][1])
        insertar_creaturas(matriz, cordenadas[i][0], cordenadas[i][1], cordenadas[i][2])

    return matriz

def insertar_jugador_mapa(matriz,jugador):
    cordenadas = []
    cordenadas.append(((jugador["Fila"], jugador["Columna"]), '𓀝'))
    insertar_creaturas(matriz, cordenadas[0][0], cordenadas[0][1], 'Jugador')
    return matriz



def imprimir_mapa(matriz):
    for fila in matriz:
        for valor in fila:
            print(valor, end="  ")
        print()

