import numpy as np

def f(x):
    return np.exp(-x**2)

dx = 0.001
x = 1.5

d = (f(x + dx) - f(x))/2*dx
er = np.abs(d-4)

print(f'derivaatta: {d:.2f}   virhe: {er:.2f}')
