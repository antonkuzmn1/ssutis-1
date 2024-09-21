import math

def f(x):
    return x**2 - math.sqrt(x)

def bisection_method(a, b, tol=1e-6):
    iterations = 0

    while (b - a) / 2.0 > tol:
        midpoint = (a + b) / 2.0
        if f(midpoint) == 0:
            print('if', midpoint)
            return midpoint, iterations
        elif f(a) * f(midpoint) < 0:
            print('elif', midpoint)
            b = midpoint
        else:
            print('else', midpoint)
            a = midpoint
        iterations += 1

    return (a + b) / 2.0, iterations

def calc():
    a = 0.1
    b = 1.5
    tolerance = 1e-5

    solution, num_iterations = bisection_method(a, b, tolerance)

    if solution is not None:
        print(f"Приближенное решение уравнения: {solution:.5f}")
        print(f"Количество итераций: {num_iterations}")
    else:
        print("Решение не найдено.")

def main():
    print('lab1')
    calc()