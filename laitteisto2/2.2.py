import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(-5,0, 10)
y1 = 3/5*x1 + 3
x2 = np.linspace(0,4, 10)
y2 = np.full_like(x2, 3)
x3 = np.linspace(4,8, 10)
y3 = -3/4*x3 + 6
x4 = np.linspace(8,10, 10)
y4 = 1/2*x4 - 4

plt.plot(x1,y1)
plt.plot(x2,y2)
plt.plot(x3,y3)
plt.plot(x4,y4)

plt.grid(True)
plt.show()
