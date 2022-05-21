# RETO 3: POBLANDO AL WORLDCRAFT ASCII
![image](https://user-images.githubusercontent.com/104838545/169629324-457d4f08-4323-4438-a8f1-2a867d1b59a3.png)
![image](https://user-images.githubusercontent.com/104838545/169629329-e3d6574a-6af7-4cb8-a21b-a4a2d3034d6a.png)
![image](https://user-images.githubusercontent.com/104838545/169629334-cb28e4e1-c81d-4169-afda-dcac9800abba.png)
![image](https://user-images.githubusercontent.com/104838545/169629343-6761f83a-e9a2-452d-b5f6-c76f4741ea1b.png)



Este reto se trata de implementar un programa que permita poblar al mundo WorldCraft ASCII.
<h1>RACIÓN DE CRIATURAS</1>
Esta funcionalidad tiene como objetivo generar un numero dado de criaturas pasivas y otro de criaturas hostiles.
  
<h2>Se debe implementar una función que permita:</h2>
<lu>
  <li>Recibir como parámetros el numero de criaturas pasivas y el numero de criaturas hostiles
  <li>Validar que: Los numeros ingresados sean mayores a cero y no sumen mas de 50 entre ambos
  <li>Retornar dos colas (FIFO) una para las criaturas pasivas y otra para las criaturas hostiles que deben haber sido generadas de manera aleatoria, es decir cada que se llama a la función debe retornar criaturas distintas
<lu>
<h1>APARICIÓN DE CRIATURAS</h1>
Esta función se encarga de obtener criaturas pasivas y hostiles para que aparezcan en el juego, cada criatura debe tener los siguientes datos.
<lu>
<li>Tipo (Pasiva / Hostil)
<li>Nombre
<li>símbolo (carácter que lo representa)
<li>Fila donde debe aparecer (generada aleatoriamente)
<li>Columna donde debe aparecer (generada aleatoriamente)
<li>Fecha y hora en la que aparece (tomada del sistema)
  </lu>
<h2>Se debe implementar una función que permita:</h2>
<lu>
<li>Recibir como parámetros la cola de la que se desea obtener una criatura
<li>Retornar una estructura de datos (¿tupla?, ¿diccionario?) con la información retornada
<li>La criatura que aparece debe ser almacenada en una lista que debe contener todas las criaturas que se encuentran en el juego.
</lu>

<h1>¿Y EL JUGADOR?</h1>


Se debe tener una función que genere una estructura de datos similar a la pedida en el punto anterior para la criatura (¿tupla?,
¿diccionario?) que tenga los datos del jugador
<lu>
<li>Tipo (Jugador)
<li>Alias
<li>Fila donde debe aparecer (generada aleatoriamente)
<li>Columna donde debe aparecer (generada aleatoriamente)
<li>Fecha y hora en la que aparece (tomada del sistema)
<li>Numero de corazones (inicia con 10)
</lu>
  
  <h2>Se debe implementar una función que permita:</h2>
•	Recibir como parámetro el alias del jugador
•	Retornar una estructura de datos (¿tupla?, ¿diccionario?) con la información retornada


<h1>REPORTE DEL JUEGO</h1>


Para esta parte vamos a implementar dos funciones:
 <h2>La primera función</h2>
•	Dadas:
o	La lista de muros
o	La lista de criaturas en el juego
o	La estructura con los datos del jugador
•	Dibuje en la consola el juego con muros, criaturas y jugador.


<h2>La segunda función</h2>
•	Debe calcular
o	Número total de muros
o	Vidas del jugador
o	Número total de criaturas en el juego
