from Point import Point
from math import floor
import random as rnd
import matplotlib.pyplot as plt

def determinant(p, p1, p2):  # p относительно p1p2
    return (p2.x - p1.x) * (p.y - p1.y) - (p.x - p1.x) * (p2.y - p1.y)

def det(a, b, c, d):
    return a * d - b * c

def initPoints(n) -> list:
    X = [rnd.randint(0, 10) for _ in range(n)]
    Y = [rnd.randint(0, 10) for _ in range(n)]
    points = []
    for i in range(len(X)):
        el = Point(X[i], Y[i])
        points.append(el)
    return points

def areIntersect(P1: Point, P2: Point, P3: Point, P4: Point) -> bool:
    d1 = det(P4.x - P3.x, P4.y - P3.y, P1.x - P3.x, P1.y - P3.y)
    d2 = det(P4.x - P3.x, P4.y - P3.y, P2.x - P3.x, P2.y - P3.y)
    d3 = det(P2.x - P1.x, P2.y - P1.y, P3.x - P1.x, P3.y - P1.y)
    d4 = det(P2.x - P1.x, P2.y - P1.y, P4.x - P1.x, P4.y - P1.y)

    c1 = (P3.x - P1.x) * (P4.x - P1.x) + (P3.y - P1.y) * (P4.y - P1.y)
    c2 = (P3.x - P2.x) * (P4.x - P2.x) + (P3.y - P2.y) * (P4.y - P2.y)

    if d1 == d2 == d3 == d4 == 0:
        if c1 > 0 and c2 > 0:
            return False
        else:
            return True
    elif d1 * d2 <= 0 and d3 * d4 <= 0:
        return True
    else:
        return False

def isSimplePolygon(points: list) -> bool:
    n = len(points)
    t = len(points) - 1
    for i in range(len(points) - 2):
        for j in range(i + 2, t):
            if areIntersect(points[i % n], points[(i + 1) % n], points[j % n], points[(j + 1) % n]):
                return False
        t += 1
    return True

def gabaritTest(points, p0) -> bool:
    xMax = points[0].x
    yMax = points[0].y
    xMin = points[0].x
    yMin = points[0].y
    for i in range(0, len(points)):
        if xMax < points[i].x:
            xMax = points[i].x
        if yMax < points[i].y:
            yMax = points[i].y
        if xMin > points[i].x:
            xMin = points[i].x
        if yMin > points[i].y:
            yMin = points[i].y
    if p0.x > xMax or p0.y > yMax or p0.x < xMin or p0.y < yMin:
        return False  # не в многоугольнике
    else:
        return True  # в многоугольнике

def next(i, n):
    return i + 1 if i < n - 1 else 0

def prev(i, n):
    return i - 1 if i > 0 else n - 1

def checkPositionOfPoint(p0, p1, p2):
    d = determinant(p0, p1, p2)
    if d > 0:
        return 1  # левее
    elif d < 0:
        return -1  # правее
    else:
        return 0  # на отрезке

def isOnLine(p0, p1, p2):  #принадлежность точки р0 отрезку р1р2
    if checkPositionOfPoint(p0, p1, p2) == 0:
        return True
    return False

def rayTest(points, p0):
    if gabaritTest(points, p0) == False:
        return False
    else:
        xMin = points[0].x
        for i in range(0, len(points)):
            if xMin > points[i].x:
                xMin = points[i].x
        q = Point(xMin-1, p0.y)
        s = 0
        i = 0
        n = len(points)
        while i < n:
            j = next(i, n)
            if isOnLine(p0, points[i], points[j]):  # если на ребрах, то "в многоугольнике"
                return True
            if areIntersect(p0, q, points[i], points[j]):
                if isOnLine(points[i], q, p0) or isOnLine(points[j], q, p0):
                    if isOnLine(points[i], q, p0):
                        k = next(i, n)
                        while isOnLine(points[k], q, p0):
                            k += 1
                        l = prev(i, n)
                        while isOnLine(points[l], q, p0):
                            l -= 1
                        if determinant(points[k], q, p0) * determinant(points[l], q, p0) < 0:
                            s += 1
                        i = k - 1
                    if isOnLine(points[j], q, p0):
                        continue
                else:
                    s += 1
            i += 1

        if s % 2 == 0:
            return False
        else:
            return True


def drawPolygon(points: list, p0: Point):
    for i in range(0, len(points)):
        if i + 1 == len(points):
            k = 0  # k - индекс последней точки
        else:
            k = i + 1
        plt.scatter(points[i].x, points[i].y)
        plt.scatter(p0.x, p0.y)
        plt.text(points[i].x + 0.1, points[i].y + 0.1, 'P{}'.format(i+1))
        plt.text(p0.x + 0.1, p0.y + 0.1, 'P0')
        plt.plot([points[i].x, points[k].x], [points[i].y, points[k].y])
    grid = plt.grid(True)

