import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 100, 100)
y = -0.0063*x**2 + 0.55*x

plt.plot(x, y)

plt.ylim([0, 15])

plt.grid(True)
plt.show()