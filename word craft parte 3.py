from logica.jugador import *
from logica.graficos import *
from logica.mundo import *

if __name__ == '__main__':
    # Validacion de CDIA
    saltarconsola(1)
    while True:
        print('\nCrear un código CDIA.\n'
              'El CDIA debe contener los siguientes caracteres:\n'
              '1. Debe contener 10 caracteres\n'
              '2. No puede contener números.\n'
              '3. en sexto carácter debe ser un "@".\n'
              '4. debe contener un "+".\n'
              '5. No debe contener mas de 3 veces la letra "k"\n'
              '6. Debe tener al menos uno de estos símbolos (‘?’,’=’,’&’) \n'
              '7. El primero y ultimo carácter deben ser diferentes\n')

        cdia_jugador = input('Ejemplo ( w+ert@ekk& ): ')
        if not validar_cdia(cdia_jugador):
            saltarconsola(100)
            texto(2, 'CDIA invalido.', 'Por favor,', 'ingresar CDIA valido')
        else:
            break

    # Validación Fecha de nacimiento Retorna edad en variable gloval "annio"
    saltarconsola(100)
    texto(1, 'Bienvenido a World craft.',
          'Para continuar con el registro por favor',
          'ingresa tu fecha de nacimiento (DD/MM/AAAA')
    while True:
        fecha_nacimiento = input('Fecha de nacimiento: ')
        if not validar_edad(fecha_nacimiento):
            saltarconsola(100)
            texto(2, 'Lo sentimos.', 'Formato de fecha invalido', '(DD/MM/AAA')
        elif validar_edad(fecha_nacimiento) == 'menor':
            saltarconsola(100)
            texto(2, 'Lo sentimos.', 'Debes ser mayor de 12 años', 'para jugar. Hasta luego')

        else:
            annio = validar_edad(fecha_nacimiento)
            break

    # Validacion de alias
    saltarconsola(100)
    texto(1, 'Es hora de colocarte un alias.', 'El alias debe:', 'Tener 5 caracteres y No debe tener espacios en blnaco')
    while True:
        alias = input('Alias: ')
        if validar_alias(alias):
            break
        else:
            saltarconsola(100)
            texto(2, 'Lo sentimos.', 'El alias debe:',
                  'Tener 5 caracteres y No debe tener espacios en blanco')

    # Validar si es jugador antiguo o no
    saltarconsola(100)
    texto(1, f'Hola. {alias}', '¿Ya has jugado WorldCraft antes?', '( Si o No ): ')
    while True:
        jugador_antiguo = input('( Si o No ): ')
        if validar_preguntaSioNo(jugador_antiguo) == 'error':
            saltarconsola(100)
            texto(2, 'Lo sentimos, La respuesta no es valida.', '¿Ya has jugado WorldCraft antes?', '( Si o No )')
        else:
            break

    # Validar si el nivel ingresado esta correcto
    while True:
        if validar_preguntaSioNo(jugador_antiguo):
            saltarconsola(100)
            texto(1, f'Hola. {alias}', '¿Hasta que nivel llegaste?', '(los niveles van desde 1 hasta 100): ')
            nivel = input('Nivel: ')
            if validar_nivel(nivel):
                n_nivel = posicioamiento_niveles(annio, nivel, jugador_antiguo)
                break
        elif not validar_preguntaSioNo(jugador_antiguo):
            nivel = 0
            n_nivel = posicioamiento_niveles(annio, nivel, jugador_antiguo)
            break

    # Validar numero de creaturas pasivas
    saltarconsola(100)
    texto(4, f'Hola. {alias}', 'Numero de criaturas pasivas', 'la suma de criaturas pasivas y hostiles no deben acceder los 50: ')
    while True:
        creaturasp = input('Número de criaturas pasivas: ')
        if not validar_ingreso_creaturas(creaturasp):
            saltarconsola(100)
            texto(2, 'Lo sentimos.', 'Respuesta no valida:',
                  'debe ingresar un numero')
        else: break

    # Validar numero de creaturas hostiles
    saltarconsola(100)
    texto(3, f'Hola. {alias}', 'Numero de creaturas hostiles',
          'la suma de creaturas pasivas y hostiles no deden eceder los 50: ')
    while True:
        creaturash = input('Numero de creaturas hostiles: ')
        if not validar_ingreso_creaturas(creaturash):
            saltarconsola(100)
            texto(2, 'Lo sentimos.', 'Respuesta no valida:',
                  'debe ingresar un numero')
        elif not generador_criaturas(int(creaturash), int(creaturasp)):
            saltarconsola(100)
            texto(2, 'Lo sentimos.', 'La suma de las entidades no debe superar los 50',
                  f'solo puede ingresar maximo {50 - int(creaturasp) } creaturas hostiles ')
        else:
            break


    #Imprecion final

    #jugador final
    saltarconsola(100)
    print('\nReporte del jugador')
    jugador = jugador_info(alias)
    reporte_jugador(jugador)
    n_nivel = posicioamiento_niveles(annio, nivel, jugador_antiguo)
    mundo = niveles_juego(annio, True, n_nivel)
    avatar(alias, n_nivel, mundo)

    #mods y mapa
    nuevo_mundo = crear_mundo()
    creaturas = generador_criaturas(int(creaturash), int(creaturasp))
    creaturas_activas = creaturas_activas(creaturas)
    insertar_creaturas_mapa(nuevo_mundo,creaturas_activas)
    insertar_jugador_mapa(nuevo_mundo,jugador)
    print('\nMundo')
    imprimir_mapa(nuevo_mundo)
    print('\nReporte de entidades')
    imprimir_registro_entidades(creaturas_activas)
