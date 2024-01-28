# 1. Määrittele ja esitä 5-alkioinen kokonaislukutaulukko numpyn avulla. Luvut
# voivat olla satunnaisia.

import numpy as np

table = np.random.randint(0,50,5)
print(f"1. Kokonaislukutaulukko\n\n{table}")

print()

# 2. Sinulla on vektorit a) u = 2i + 3j, v =4i - 7j b) uu= i + j + k, vv 3i -3j + 2k.
# Määrittele nämä numpy taulukon avulla.

u = np.array([2, 3])
v = np.array([4, -7])

print("2.")
print("a)")
print(f"u = {u}")
print(f"v = {v}")

print()

uu = np.array([1, 1, 1])
vv = np.array([3, -3, 2])

print("b)")
print(f"uu = {uu}")
print(f"vv = {vv}")

print()

# 3. Laske kunkin vektorin normi.

print("3. Vektorien normit\n")
print(f"u = {np.linalg.norm(u):.2f}")
print(f"v = {np.linalg.norm(v):.2f}")
print(f"uu = {np.linalg.norm(uu):.2f}")
print(f"vv = {np.linalg.norm(vv):.2f}")