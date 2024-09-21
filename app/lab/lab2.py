import numpy as np

def f(x):
    return x + np.sin(x) - 0.5

def simple_iteration(x0, epsilon, lambda_param):
    k = 0
    x_k = x0
    while True:
        x_k1 = x_k - (1 / lambda_param) * f(x_k)
        norm_r_k = np.abs(f(x_k))
        print("Iteration {}: x_k = {:.6f}, f(x_k) = {:.6f}".format(k, x_k, f(x_k)))
        if norm_r_k < epsilon:
            break
        x_k = x_k1
        k += 1
    return x_k, k


def calc():
    x0 = 0.5
    epsilon = 1e-6
    lambda_param = 1.0

    x_approx, num_iterations = simple_iteration(x0, epsilon, lambda_param)

    print("Approximate solution: x ≈ {:.6f}".format(x_approx))
    print("Количество итераций: {}".format(num_iterations))

def main():
    print('lab2')
    calc()