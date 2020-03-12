

import sys
from point2d import Point2D
from math import pi, cos, sin
import random

trials = int(sys.argv[1])

totalSteps = 0

for i in range(trials):
    point = Point2D(0, 1)
    while point.r <= 1: #(distance from origin)
        theta = random.uniform(0, 2*pi)
        point.x = point.x + cos(theta)
        point.y = point.y + sin(theta)
        #print(str(point.x) +", "+ str(point.y))
        totalSteps += 1

    #print("Done.")

print("Average: "+str(totalSteps / trials))
    



