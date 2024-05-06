import numpy as np

def f(x):
    return np.sin(x)

dx = 0.001
x = 0.5

d1 = (f(x + dx) - f(x))/dx
d2 = (f(x + dx) - f(x))/(2*dx)
er1 = np.abs(d1-4)
er2 = np.abs(d2-4)

print(f'kaksipistekaava: {d1:.2f}   virhe: {er1:.2f}')
print(f'kolmipistekaava: {d2:.2f}   virhe: {er2:.2f}')
