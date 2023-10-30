import numpy as np

print("Laske suorakulmaisen kolmion hypotenuusa\n")

# c)
kulma = 43.3
a = 17.5

rad = np.radians(kulma)

print(f"Hypotenuusa on {a / np.sin(rad):.2f}m")

# d)

kulma = 62.4
c = 112

rad = np.radians(kulma)

print(f"Hypotenuusa on {c * np.sin(rad):.2f}m")