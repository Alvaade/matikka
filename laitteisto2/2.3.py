import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 6, 100)
y = x**2 - 4*x + 3  # a)

plt.plot(x, y)

y2 = -1.5*x**2 - 3*x + 7  # b)

plt.plot(x, y2)

plt.ylim([-10, 10])

plt.grid(True)
plt.show()