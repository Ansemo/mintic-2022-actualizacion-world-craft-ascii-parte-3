from datetime import *
import random
from colorama import Fore

from .graficos import saltarconsola

def validar_cdia(cdia):
    if len(cdia) == 10:
        mas = 0
        k = 0
        sinb = 0
        for cont in cdia:
            if cont == '+': mas += 1
            if cont == 'k': k += 1
            if cont == '?' or cont == '=' or cont == '&': sinb += 1
        if cdia.find('@') + 1 == 6 and cdia[0] != cdia[9] and mas >= 1 and k <= 3 and sinb >= 1:
            if not any(chr.isdigit() for chr in cdia):
                return True
    return False

#
# def validar_inscritos(nuevo_jugador):
#     nuevo_jugador = nuevo_jugador.swapcase()
#     jugadores_all = {
#         # 'qwertf@fgh': True,
#         '+wert@ekk&': True,
#         '+wert@ekk=': True,
#         # 'qwert@efgh': True,
#         # 'qwer1@efgh': True,
#         # '+wert@ekkk': True,
#     }
#     jugadores_inscritos = {}
#
#     for players in jugadores_all:
#         if validar_cdia(players):
#             jugadores_inscritos[players.swapcase()] = validar_cdia(players)
#
#     for inscritos in jugadores_inscritos:
#         if inscritos == nuevo_jugador:
#             saltarconsola(100)
#             return False
#         else:
#             return True
#     # print(jugadores_inscritos)
#

def validar_edad(edad):
    edad_limpia = ''.join(filter(str.isalnum, edad))
    if len(edad) == 10 and edad_limpia.isdigit():
        fecha_nacimiento = datetime.strptime(edad, '%d/%m/%Y')
        hoy = datetime.today()
        annio = hoy.year - fecha_nacimiento.year - (
                    (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        if annio > 12:
            return annio
        else:
            saltarconsola(100)
            return 'menor'
    return False


def validar_alias(alias):
    cont_spacios = 0
    for espacios in alias:
        if espacios == ' ':
            cont_spacios = cont_spacios + 1

    if len(alias) == 6 and not cont_spacios >= 1:
        return True
    else:
        return False


def validar_preguntaSioNo(respuesta):
    if respuesta.swapcase() == 'SI':
        return True
    elif respuesta.swapcase() == 'NO':
        return False
    else:
        return 'error'


def validar_nivel(nivel):
    if nivel.isalpha():
        return False
    elif nivel:
        if int(nivel) > 1 or int(nivel) < 100:
            return True
    else:
        return 'error'


def niveles_juego(edad, jugador_antiguo, nivel):
    if 12 < edad <= 20 and jugador_antiguo == False:
        return 'Mundo 1'
    elif 12 < edad <= 20 and jugador_antiguo == True and nivel < 50:
        return 'Mundo 2'
    elif 12 < edad <= 20 and jugador_antiguo == True and nivel > 50:
        return 'Mundo 3'
    elif edad >= 20 and jugador_antiguo == False:
        return 'Mundo 4'
    elif edad >= 20 and jugador_antiguo == True and nivel < 50:
        return 'Mundo 5'
    elif edad >= 20 and jugador_antiguo == True and nivel > 50:
        return 'Mundo 6'
    else:
        return 'Mundo magico'


def posicioamiento_niveles(edad, nievel_actual, jugador_antiguo):
    nievel = int(nievel_actual)
    if edad < 16:
        if not validar_preguntaSioNo(jugador_antiguo):
            return 2
        elif validar_preguntaSioNo(jugador_antiguo):
            return nievel

    if edad >= 16:
        if not validar_preguntaSioNo(jugador_antiguo):
            return 1
        elif validar_preguntaSioNo(jugador_antiguo):
            nuevo_nievel = nievel + 2
            if nuevo_nievel > 100:
                return 100
            else:
                return nuevo_nievel


def jugador_info(alias):
    jugador = {
        'Tipo': 'jugador',
        'Alias': alias,
        'Fila': random.randint(0, 17),
        'Columna': random.randint(0, 17),
        'Fecha': datetime.now(),
        'Vida': 10
    }
    return jugador


def reporte_jugador(jugador):
    print(Fore.YELLOW + f'Tipo {jugador["Tipo"]}\n'
                        f'Alias {jugador["Alias"]}\n'
                        f'Cordenadas ({jugador["Fila"]},{jugador["Columna"]})\n'
                        f'Fecha espaund {jugador["Fecha"]}\n'
                        f'Vida {jugador["Vida"]} Corazones')


