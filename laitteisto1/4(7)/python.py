from sympy import symbols, solve

x, y, z = symbols('x y z')

# 1 a)

solution_1a = solve([x-2*y-2*z+0,
                    -2*x+y-z+3,
                    3*x+2*y+z-4], [x,y,z])
print(f"1 a) {solution_1a}")

# 1 b)

solution_1b = solve([x+y-1,
                    2*x+y-z-1,
                    3*x+y-2*z-1], [x,y,z])
print(f"1 b) {solution_1b}")

# 2 a)

solution_2a = solve([2*x+4*y-z-11,
                    6*x-y-3*z-7,
                    4*x+5*y-2*z-16], [x,y,z])
print(f"2 a) {solution_2a}")

# 2 b)

solution_2b = solve([4*x+2*y-2*z+0,
                    2*x+y-z-1,
                    3*x+y-2*z-1], [x,y,z])
print(f"2 b) {solution_2b}")

# K a)

solution_Ka = solve([5*x+3*y-9,
                    2*x+y-4], [x,y])
print(f"K a) {solution_Ka}")

# K b)

solution_Kb = solve([2*x+y+z-6,
                    x+3*y+z-2,
                    2*x+y+2*z-9], [x,y,z])
print(f"K b) {solution_Kb}")

# K c)

solution_Kc = solve([x+y+3*z+1,
                    3*x+y+z-5,
                    2*x+y+2*z-2], [x,y,z])
print(f"K c) {solution_Kc}")

