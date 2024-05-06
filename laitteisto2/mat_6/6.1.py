from sympy import symbols, diff

x = symbols('x')
derivative = diff((2*x**2)-3, x)
print(derivative)