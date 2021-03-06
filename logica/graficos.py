def saltarconsola(cantidad):
    clearConsole = lambda: print('\n' * cantidad)
    clearConsole()
    print('─────────────────────█▄██▄█─────────────────────────\n'
          '────────────█▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█────────────────\n'
          '────────────███┼█████▐████▌█████┼███────────────────\n'
          '────────────█████████▐████▌█████████────────────────\n'
          '█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n'
          '█ █   █ █▀▀█ █▀▀▄ █  █▀▀▄    █▀▀ █▀▀▄ █▀▀█ █▀▀ ▀█▀ █\n'
          '█ █▄█▄█ █  █ █▄▄▀ █  █  █    █   █▄▄▀ █▀▀█ █▀▀  █  █\n'
          '█  ▀ ▀  ▀▀▀▀ ▀  ▀ ▀▀ ▀▀▀     ▀▀▀ ▀  ▀ ▀  ▀ ▀    ▀  █\n'
          '▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀')


def texto(estado, tex1, tex2, tex3):
    if estado == 2:
        print('     ▄▄▄▄▄ ▄ ▄ ▄ ▄\n'
              '▄▄▄▄██▄████▀█▀█▀█▀██\n▄'
              f'▀▄▀▄▀▄████▄█▄█▄█▄█████   {tex1}\n'
              f'▀▀▀▀▀▀▀▀██▀▀▀▀██▀  ▄██    {tex2}\n'
              f'       ▀▀    ▀▀ ▄▄██▀     {tex3}')
    elif estado == 1:
        print('     ▀▄▀     ▄     ▄\n'
              '  ▄███████▄  ▀██▄██▀\n'
              f'▄█████▀█████▄  ▄█    {tex1}.\n'
              f'███████▀████████▀    {tex2}\n'
              f' ▄▄▄▄▄▄███████▀      {tex3}')

    elif estado == 4:
        print('  ███▅▄▄▄▄▄▄▄▄▄\n'
              ' ██▐████████████\n'
              f'▐█▀████████████▌▌    {tex1}.\n'
              f'▐ ▀▀▀▐█▌▀▀███▀█ ▌    {tex2}.\n'
              f'▐▄   ▄█   ▄█▌▄█      {tex3}.')
    elif estado == 3:
        print('   ▄▀▀▀▀▀   ▄█▀▀▀█▄\n'
              '  ▐▄▄▄▄▄▄▄▄██▌▀▄▀▐██\n'
              f'  ▐▒▒▒▒▒▒▒▒███▌▀▐███    {tex1}.\n'
              f'   ▌▒▓▒▒▒▒▓▒██▌▀▐██     {tex2}.\n'
              f'   ▌▓▐▀▀▀▀▌▓ ▀▀▀▀▀      {tex3}.')



def avatar(nombre, nivel, mundo):
    if nivel <= 20:
        print(f'             █▀▄     ▄▀█        Mundo: {mundo}\n'
              f'            █░ ▀▄▄▄▀ ░█\n'
              f'            █░       ░█         Nombre: {nombre} \n'
              f'      ▄▄    █  ░   ░  █         Nivel: {nivel}\n'
              f'      █░█   █  █   █  █\n'
              f'     █░░█   █    ▄▄   █\n'
              f'    █░░█  ▄▀░░░░▄░░▄░░░▀▄       Inventario: \n'
              f'    █░░█  ▀▀▄▄░░░▀▀░ ▄▄▀▀         Cuchillo\n'
              f'   ▀▀████▄▄▄▄▄█▀▀▀▀▀█▄     \n'
              f'     █▄▄▄▄▄▄▄▄▄     ▄▄▀▀▄▄▄\n'
              f'     █ █      █ ░░░ █ ▀▀█▄▄█\n'
              f'      ▀▀      █ ░░░ █      \n'
              f'             █  ▄▄▄ █▄     \n'
              f'           █▀ ▄▀   ▀▄ ▀█   \n'
              f'           ▀▀▀       ▀▀▀')
    elif 20 <= nivel <= 60:
        print(f'       ▄▄   █▀▄     ▄▀█         Mundo: {mundo}\n'
              f'      █░█   █░ ▀▄▄▄▀ ░█\n'
              f'     █░░█   █░       ░█         Nombre: {nombre} \n'
              f'    █░░█    █  ░   ░  █         Nivel: {nivel}\n'
              f'    █░░█    █  █   █  █\n'
              f'    █░░█    █    ▄▄   █\n'
              f'    █░░█  ▄▀░░░░▄░░▄░░░▀▄       Inventario: \n'
              f'    █░░█  ▀▀▄▄░░░▀▀░ ▄▄▀▀         Espada \n'
              f'   ▀▀████▄▄▄▄▄█▀▀▀▀▀█▄   \n'
              f'     █▄▄▄▄▄▄▄▄▄     ▄▄▀▀▄▄▄\n'
              f'     █ █      █ ░░░ █ ▀▀█▄▄█\n'
              f'      ▀▀      █ ░░░ █      \n'
              f'             █  ▄▄▄ █▄     \n'
              f'           █▀ ▄▀   ▀▄ ▀█    \n'
              f'           ▀▀▀       ▀▀▀')
    elif 60 <= nivel <= 100:
        print(f'       ▄▄   █▀▄     ▄▀█         Mundo: {mundo}\n'
              f'      █░█   █░ ▀▄▄▄▀ ░█\n'
              f'     █░░█   █░       ░█         Nombre: {nombre} \n'
              f'    █░░█    █  ░   ░  █         Nivel: {nivel}\n'
              f'    █░░█    █  █   █  █\n'
              f'    █░░█    █    ▄▄   █\n'
              f'    █░░█  ▄▀░░░░▄░░▄░░░▀▄  ▄▄\n'
              f'    █░░█  ▀▀▄▄░░░▀▀░ ▄▄▀▀  █▒█  Inventario: \n'
              f'   ▀▀████▄▄▄▄▄█▀▀▀▀▀█▄     █▒░█    Espada\n'
              f'     █▄▄▄▄▄▄▄▄▄     ▄▄▀▀▄▄▄█▒░░█   Escudo\n'
              f'     █ █      █ ░░░ █ ▀▀█▄▄█▒░░█\n'
              f'      ▀▀      █ ░░░ █      █▒░█\n'
              f'             █  ▄▄▄ █▄     █▒█\n'
              f'           █▀ ▄▀   ▀▄ ▀█    ▀\n'
              f'           ▀▀▀       ▀▀▀')
