import math
import random

line = (input()).split()

point = []
points = []

for l in line:
    if len(point) == 2:

        points.append(tuple(point))
        point = [int(l)]
    else:
        point.append(int(l))

points.append(tuple(point))

def print_points(points):
    print("************************************")
    for p in points:
        print('{0:-2d} {1:2d}'.format(p[0], p[1]))


def line_equation(points):
    first_point = points[0]
    last_point = points[len(points)-1]
    print("Pick two points")
    print("First Point = " + str(first_point))
    print("Second Point = " + str(last_point))

    print("Finding Slope/m")
    print("last point y - first point y")
    print(str(last_point[1]) + " - " + str(first_point[1]) + " = " + str(last_point[1] - first_point[1]))
    numerator = last_point[1] - first_point[1]
    print("last point x - first point x")
    print(str(last_point[0]) + " - " + str(first_point[0]) + " = " + str(last_point[0] - first_point[0]))
    denumerator = last_point[0] - first_point[0]
    print("Slope is = " + str(numerator / denumerator))
    slope = numerator/denumerator

    print("Finding B")
    print("Using some point in the list of points we have")
    random_point = points[random.randint(0, len(points)-1)]
    print ("Let's use ")
    print(random_point)
    y = random_point[1]
    x = random_point[0]
    print("y = mx + b " + str(y) + " = m" + str(x) + " + b")
    print(str(y) + " = " + str(slope) + "*" + str(x) + " + b")
    print(str(y) + " = " + str(slope * x) + " + b")
    print(str(y - (-1 * (slope * x))) + " = b")
    b = y - (-1 * (slope * x))

    print("Final is y = " + str(slope) + "x + " + str(b));  


line_equation(points)