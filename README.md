# RETO 3: POBLANDO AL WORLDCRAFT ASCII <h1>!OJO EL CODIGO AUN NO ESTA TERMINADO, ESTAR ATENTO A ACTUALIZACIONES!</h1>


![image](https://user-images.githubusercontent.com/104838545/169082647-91d8f947-dc7c-49ba-b115-6740cd39e1de.png)
![image](https://user-images.githubusercontent.com/104838545/169082599-2c26b9c1-393d-4397-bbb7-e57f9429e4b5.png)<br>

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
