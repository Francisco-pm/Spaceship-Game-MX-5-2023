SPACESHIP GAME:
El juego es un loop de duracion infinita en el que van apareciendo 3 tipos de enemigos distintos en lo alto de la pantalla
despues de matar una cierta cantidad de enemigos aparece un jefe y cambia el fondo de la pantalla, despues de derrotar al jefe el loop vuelve a ser repetido.

Menu:
Al empezar el juego iniciamos con un menu que nos indica que podemos presionar cualquier tecla para comenzar, despues de morir 1 vez este menu cambia, el mensaje ahora pide presionar una tecla para reintentar y ademas aparece distinta informacion util que son: Score maximo alcanzado, Score del intento, Numbero de muertes


Jugador:
El jugador puede controlar una nave la cual aparece cerca del centro de la pantalla, la nave puede moverse con las flechas del teclado; pero no puede subir mas alla de la mitad de la pantalla de juego o salir por alguna de las orillas de la misma, y puede ademas disparar al presionar la tecla de espacio en el teclado.
La nave cuenta con 3 golpes antes de ser destruida, despues de cada golpe el jugador cuenta con un pequeño tiempo de invulnerabilidad el cual es visualizado por un parpadeo en la nave.
Un golpe a la nave ocurre de 2 maneras; la primera siendo al ser alcanzado por una bala enemiga y la segunda es chocando con cualquier enemigo o jefe.

PowerUp:
A la hora de estar jugando despues de un tiempo aleatorio aparecera un powerup en pantalla, si la nave toma el powerup obtiene ciertos beneficios.
Existe 1 tipo de powerup:
    -Shield: Al tomarlo el jugador obtiene un escudo que lo hacen invulnerable contra balas y choques con enemigos.

Enemigos:
Son objetos que hacen daño por contacto al jugador y ademas pueden disparar balas
Existen 3 tipos de enemigos en el juego:
Ship = consiste en una nave que baja a velocidad constante y que constantemente o al chocar con los limites de la pantalla cambia su direccion
Spider = Parecido al anterior esta nave baja a velocidad constante pero mas rapidamente y sus cambios de direccion son aleatorios, puede moverse tanto a izquierda como a derecha, lo cual la hace menos predecible, por su mayor dificultad tambien tiene una velocidad de disparo mas lenta
Alien = El enemigo mas sencillo, su unico movimiento es avanzar de izquierda a derecha y al tocar un limite de la pantalla bajar un poco, tiene la velocidad de ataque mas lenta de los 3 enemigos siendo raro verlos disparar antes de ser destruidos

Jefes:
Aparecen despues de destruir una cantidad de enemigos, parecidos a los enemigos los jefes hacen daño por contacto y ademas disparan, con la diferencia de que estos ademas tienen una cantidad de vida que los hace resistir varios impactos y cuentan con distintos patrones de movimiento y disparo.
su cantidad de vida se reduce en 5 por cada disparo o colision que reciban.
AlienLeader = El Lider de los Aliens tiene la nave mas grande del juego y esta equipada con dos modos distintos. 
                -En el primer modo se mueve en diagonal y rebota con las esquinas. Dispara desde su centro una bala hacia arriba y una hacia abajo
                -El segundo modo lo hace moverse solo en horizontal pero ahora disparando 3 balas hacia arriba y 3 hacia abajo las bala del centro sale desde un poco mas arriba que las otras dos lo que hace el patron mas dificil de predecir

Balas:
Las balas son aquellos projectiles producidos por cualquier nave, enemigo o jefe.
Existen 3 tipos principales de balas:
    Bala aliada: Son aquellas balas disparadas por la nave del jugador y que destruyen a los enemigos mientras que a los jefes solo les reducen algo de vida
    Bala enemiga y Bala de jefe: Son aquellas balas que disparan los enemigos y jefes estas solo afectan al jugador quien al ser golpeado pierde 1 de los golpes que puede recibir, la diferencia entre la bala de enigo y la de jefe es que la segunda tiene la posibilidad de ir hacia arriba.

Fondos:
Cuando nos encontramos enfrentandonos a enemigos solamente el juego presenta un fondo de estrellas azules, cuando el enfrentamiento cambia y hay que derrotar un jefe el fondo es cambiado a uno de estrellas rojas

Score:
El juego cuenta con un sistema de puntaje el cual funciona aumentando un punto de score por cada enemigo destruido y 100 puntos de score por cada jefe derrotado.
Ademas el juego tambien lleva el conteo de todos los scores de la sesion para mostrar el mas alto al final de cada menu

