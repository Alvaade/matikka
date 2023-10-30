import numpy as np

print("1. Muunna asteiksi\n")

a = 2.493
b = 0.911

print(f"{a} = {np.degrees(a)}")
print(f"{b} = {np.degrees(b)}")

print("\n2. Muunna radiaaneiksi\n")

a = 137.7
b = 62.3

print(f"{a} = {np.radians(a)}")
print(f"{b} = {np.radians(b)}")

print("\n3. Laadi taulukko, joka esittää kulmat radiaaneina\n")

kulmat = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])

for kulma in kulmat:
    print(f"{kulma} = {np.radians(kulma)}")