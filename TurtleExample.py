from turtle import Turtle
t = Turtle()

def hexagon(t, length):
    """Draws a hexagon with the given length. """
    for count in range(6):
        t.forward(length)
        t.left(60)

def radialHexagons(t, n, length):
    """Draws a radial pattern of hexagons with the given length. """
    for count in range(n):
        hexagon(t, length)
        t.left(360 / n)

radialHexagons(t, 30, 45)
