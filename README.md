a = 2
b = 1.5

x_values = [round(i, 1) for i in list(frange(1, 2.1, 0.1))] 

results = []

for x in x_values:
    if x == a:
        z = 7 * (a ** 2) - 8 * x
    elif x > a:
        z = 3 * b + 7 * a * x
    else:  # x < a
        z = 9 * b - 14 * a
    
    results.append((x, z))
for x, z in results:
    print(f"x = {x}, z = {z}")
    
def frange(start, stop, step):
    while start < stop:
        yield start
        start += step
