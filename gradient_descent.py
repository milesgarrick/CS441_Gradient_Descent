import numpy as np
import random


def gradient_descent(point, step):
    counter = 0
    print("Starting coordinates: (%.3f,%.3f)" % (point[0], point[1]))
    while counter < 500:
        next_point = point - np.multiply(gradient(point), step)
        point = next_point
        counter += 1
    return point


def gradient(point):
    new_x = 10 * point[0] + 40
    new_y = 2 * point[1] - 12
    return new_x, new_y


step1 = 0.1
step2 = 0.01
step3 = 0.001
x1 = round(random.uniform(-10.00, 10.00))
y1 = round(random.uniform(-10.00, 10.00))
performance = 0


for i in range(10):
    print()
    coordinates = np.array([x1, y1])
    coordinates = gradient_descent(coordinates, step3)
    temp_performance = (-4 - coordinates[0]) + abs(6 - coordinates[1])
    print(temp_performance)
    print("Global minimum at (%.3f,%.3f)" % (coordinates[0], coordinates[1]))
    del coordinates
    print("Trial %d: %.3f" % (i+1, temp_performance))
    performance += temp_performance
    x1 = round(random.uniform(-10.00, 10.00), 2)
    y1 = round(random.uniform(-10.00, 10.00), 2)

print()
print("Average performance: %.3f" % (performance/10))
