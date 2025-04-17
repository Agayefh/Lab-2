import math

x = 0.2
a = 1
epsilon = 0.01

ax = a * x
term = math.log(ax)
P = 1 + term
n = 2

while abs(term / n) >= epsilon:
    term = (math.log(ax ** n) ** n) / n
    P += term
    n += 1

print(f"P ≈ {P:.4f}")
