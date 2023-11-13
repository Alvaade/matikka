from matplotlib import pyplot as plt, patches
import numpy as np
from fractions import Fraction as fr

import matplotlib as mpl

fig = plt.figure(figsize=(6.4*3, 4.8))
ax = fig.subplots()

ymp = patches.Circle((0, 0), radius=1, fill=False, linestyle='dashed', color='blue', label='Yksikköympyrä')
ax.add_patch(ymp)

# Move left y-axis and bottom x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.axis('equal')

plt.xticks([-3*np.pi, -2*np.pi, -1*np.pi, 0, np.pi, 2*np.pi, 3*np.pi], ['-3π', '-2π', '-π', '0', 'π', '2π', '3π'])
plt.yticks([-1, 0, 1])

pist_xy=np.array([np.pi/6, np.pi/4, np.pi/3, np.pi/2, 2*np.pi/3, 5*np.pi/6, np.pi, 3*np.pi/2])
text = ['π/6', 'π/4', 'π/3', 'π/2', '2π/3', '5π/6', 'π', '3π/2']
varit=np.array(['red', 'green', 'blue', 'yellow', 'cyan', 'pink', 'brown', 'purple'])

x = np.cos(pist_xy)
y = np.sin(pist_xy)

plt.scatter(x, y, color=varit, marker='X')

for angle, label, color in zip(pist_xy, text, varit):
    plt.annotate(fr'${label}$',
                 xy=(np.cos(angle), np.sin(angle)), xycoords='data',
                 xytext=(+30, +0), textcoords='offset points', fontsize=12,
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))

plt.legend()
plt.show()