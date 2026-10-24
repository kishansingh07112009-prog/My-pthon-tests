import math 
R1 = float(input())

X1 = float(input())

R2 = float(input())

X2 = float(input())


real = R1 + R2

imaginary = X1 + X2


magnitude = math.sqrt(real**2 + imaginary**2)


print(f"{real:.2f}")

print(f"{imaginary:.2f}")

print(f"{magnitude:.2f}")