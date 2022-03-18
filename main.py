import matplotlib.pyplot as plt
from functions import *
from Point import Point

def init():
    n = 5
    points = initPoints(n)

    while isSimplePolygon(points) == False:
        points = initPoints(n)

    x = rnd.randint(0, 10)
    y = rnd.randint(0, 10)
    p0 = Point(x, y)

    answer = rayTest(points, p0)
    drawPolygon(points, p0)

    if answer:
        plt.suptitle('Точка в многоугольнике', fontsize=10)
    else:
        plt.suptitle('Точка не в многоугольнике', fontsize=10)

    plt.show()

init()