
#problem1 calculate distance between to points

import math

print("calculate distance between to points")

x1, y1, x2, y2 = map(int, input("Enter value in order x1, y1, x2, y2: ").split()) 

def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
    return distance

print("Distance between two given points is: ", calculate_distance(x1, y1, x2, y2))
