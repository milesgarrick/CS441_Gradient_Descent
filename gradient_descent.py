import sympy as sp
import random


def gradient_descent(x_value, y_value, step) -> (float, float):
    counter = 0
    print("x =", x_value, ", y =", y_value)
    x = sp.symbols('x')
    y = sp.symbols('y')
    f = sp.Lambda((x, y), (5 * (x ** 2)) + (40 * x) + (y ** 2) - (12 * y) + 127)
    while counter < 500:
        x_prime = f_x_prime(x_value)
        y_prime = f_y_prime(y_value)
        if x_prime < 0:
            x_value += step
        elif x_prime > 0:
            x_value -= step
        if y_prime < 0:
            y_value += step
        elif y_prime > 0:
            y_value -= step
        if x_prime == 0 and y_prime == 0:
            break
        counter += 1
    global_min = f(x_value, y_value)
    print("Global minimum at (%.3f,%.3f) = %.3f" % (x_value, y_value, global_min))
    return abs(-4 - x_value) + abs(6 - y_value)



def f_x_prime(x_value) -> float:
    return 10 * x_value + 40


def f_y_prime(y_value) -> float:
    return 2 * y_value - 12


step1 = 0.1
step2 = 0.01
step3 = 0.001
x1 = round(random.uniform(-10.00, 10.00))
y1 = round(random.uniform(-10.00, 10.00))
x2 = x1
x3 = x1
y2 = y1
y3 = y1
performance = 0

for i in range(10):
    print()
    temp_performance = gradient_descent(x1, y1, step2)
    print("Trial %d: %d" % (i+1, temp_performance))
    performance += temp_performance
    x1 = round(random.uniform(-10.00, 10.00))
    y1 = round(random.uniform(-10.00, 10.00))

print()
print("Average performance:", performance/10)
