"""
Juego: Memoria

Programador 1: Daniel Alejandro Martinez Rosete
Programador 2: Andrés Eugenio Martínez Sánchez 

Fecha:10/05/22...
"""

from random import *
from turtle import *

from freegames import path, vector

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
#Se crea vector contador para que se pueda usar dentro de 
#funciones aunque no sea variable local
counter = vector(0,0)
#Creamos una bandera para ver si ya gano el jugador 
#o no para solo imprimir una vez la frase ganadora y en una 
#lista para poder usarlo dentro de la función
hasWon = [False]



def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
    #Se agrega uno al contador cada que se haga un tap y se imprime.
    counter.x += 1
    print("Número de taps: " + str(counter.x))


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)


    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))
    
    #Aqui checamos si toda la listade hide es False, lo cual significa que el 
    #jugador gano e imprimimos solo una vez el mensaje marcando la bandera como 
    #verdadero
    if not any(hide):
        if not hasWon[0]:
            print("You did it in " + str(counter.x) + " taps, congratulations!!")
            hasWon[0] = True

    update()
    ontimer(draw, 100)
    


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
