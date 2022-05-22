from datetime import datetime
import random
from colorama import Fore, init


def creaturas_bd(tipo):
    pasivos = {
        'B': 'Burro',
        'N': 'Conejo',
        'G': 'Gallina',
        'C': 'Cerdo',
        'V': 'Vaca',
        'P': 'Panda',
        'L': 'Llama'

    }
    hostiles = {
        'A': 'Araña',
        'E': 'Enderman',
        'Z': 'Zombi',
        'B': 'Bruja',
        'O': 'Esqueleto',
        'W': 'Wither',
        'V': 'Vindicador'
    }
    if tipo == 'p':
        return pasivos
    if tipo == 'h':
        return hostiles


def generador_criaturas(hostil, pasiva):
    c_pasiva = list(creaturas_bd('p').keys()) #['B','N','G',...]
    c_hostiles = list(creaturas_bd('h').keys())
    pasivos = []
    hostiles = []
    if hostil + pasiva > 50:
        return False
    else:
        cont = 0
        cont2 = 0
        while pasiva > 0:
            pasivos.insert(cont, random.choice(c_pasiva))
            cont += 1
            pasiva -= 1

        while hostil > 0:
            hostiles.insert(cont2, random.choice(c_hostiles))
            cont2 += 1
            hostil -= 1

        return [pasivos, hostiles]


def creatura_info(tipo, nombre, simbolo, fila, columna, fecha):
    creatura = {
        'Tipo': tipo,
        'Nombre': nombre,
        'Simbolo': simbolo,
        'Fila': fila,
        'Columna': columna,
        'Fecha': fecha
    }
    return creatura


def creaturas_activas(creaturas):
    creaturasDBP = creaturas_bd('p')  # Datos de creaturas pasivas
    creaturasDBH = creaturas_bd('h')  # Datos de creaturas hostiles
    pasivos = creaturas[0] #['B','N','G']
    hostiles = creaturas[1]
    creaturas = []

    #{'B': 'Burro'}
    for i in range(0, len(pasivos)):
        codigo = dict(filter(lambda x: x[0] == pasivos[i], creaturasDBP.items()))

        cre = creatura_info('Pasivo', tuple(codigo.values()), tuple(codigo.keys()), random.randint(0, 17),
                            random.randint(0, 17), datetime.now())
        creaturas.append(cre)

    for i in range(0, len(hostiles)):
        codigo = dict(filter(lambda x: x[0] == hostiles[i], creaturasDBH.items()))
        cre = creatura_info('Hostil', tuple(codigo.values()), tuple(codigo.keys()), random.randint(0, 17),
                            random.randint(0, 17), datetime.now())
        creaturas.append(cre)

    # print(creaturas)
    return tuple(creaturas)


def insertar_creaturas(matriz, creatura, simbolo, tipo):
    for i in range(0, 18):
        for j in range(0, 18):
            # print(creatura)
            if creatura == (i, j):
                if tipo == 'Jugador':
                     matriz[i][j] = Fore.YELLOW + f'{simbolo}'
                elif tipo == 'Pasivo':
                    matriz[i][j] = Fore.BLUE + f'{simbolo}'
                else:
                    matriz[i][j] = Fore.RED + f'{simbolo}'


def imprimir_registro_entidades(creaturas_generadas):
    hostiles = 0
    pasivas = 0

    cont = 1
    for i in creaturas_generadas:
        if i["Tipo"] == 'Pasivo':
            print(cont,Fore.BLUE + f'Tipo: ',
                  Fore.WHITE + f'{i["Tipo"]}',
                  Fore.BLUE + f' Nombre: ',
                  Fore.WHITE + f'{i["Nombre"][0]}  ',
                  Fore.BLUE + f'Simbolo: ',
                  Fore.WHITE + f'{i["Simbolo"][0]} ',
                  Fore.BLUE + f'Cordenadas: ',
                  Fore.WHITE + f'({i["Fila"]},{i["Columna"]}) ',
                  Fore.BLUE + f'Fecha espaund:',
                  Fore.WHITE + f' {i["Fecha"]}')
            pasivas += 1
            cont += 1
        else:
            print(cont,Fore.RED + f'Tipo: ',
                  Fore.WHITE + f'{i["Tipo"]}',
                  Fore.RED + f' Nombre: ',
                  Fore.WHITE + f'{i["Nombre"][0]}  ',
                  Fore.RED + f'Simbolo: ',
                  Fore.WHITE + f'{i["Simbolo"][0]} ',
                  Fore.RED + f'Cordenadas: ',
                  Fore.WHITE + f'({i["Fila"]},{i["Columna"]}) ',
                  Fore.RED + f'Fecha espaund:',
                  Fore.WHITE + f' {i["Fecha"]}')
            hostiles += 1
            cont += 1

        print(f'-----------------------------------\n'
              f'hay {hostiles} hostiles en el mapa\n'
              f'hay {pasivas} pasivas en el mapa\n'
              f'-----------------------------------\n')


def validar_ingreso_creaturas(respuesta):
    if respuesta.isalpha():
        return False
    else:
        return True
