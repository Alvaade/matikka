import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(-1,1, 10)
y1 = np.full_like(x1, 4)
x2 = np.linspace(1,3, 10)
y2 = -2*x2 + 6

plt.plot(x1,y1)
plt.plot(x2,y2)

plt.grid(True)
plt.show()
