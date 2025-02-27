import math

pi = math.pi

# Cube
O = input("shape? cube, cylinder, cone, or pyramid?: ")
if O == "cube":
    B = float(input("enter the base: "))
    volume = pow(B, 3)
    print("this is your volume:", volume)

