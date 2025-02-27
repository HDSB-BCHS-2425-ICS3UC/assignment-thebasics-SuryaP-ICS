import math

pi = math.pi

# Cube
O = input("shape? cube, cylinder, cone, or pyramid?: ")
if O == "cube":
    B = float(input("enter the base: "))
    volume = pow(B, 3)
    print("this is your volume:", volume)

# Cylinder
elif O == "cylinder":
    Hei = float(input("enter the height of your cylinder: "))
    Rad = float(input("enter the radius of the cylinder: "))
    areab = math.pi * pow(Rad, 2)  # Fixed error here with floats was stuck on this for 20 mins
    vol = areab * Hei
    print("this is your volume:", vol)

# Cone
elif O == "cone":
    Hei = float(input("enter the height of your cone: "))
    Rad = float(input("enter the radius of the cone: "))
    Slop = float(input("enter the hypotenuse/slope of your cone: "))
    ab = math.pi * pow(Rad, 2)  # Fixed error here with floats ;-;
    als = math.pi * Rad * Slop  # Fixed error here with floats ;-;
    alt = ab + als
    volume = (ab * Hei) / 3
    print("this is your volume:", volume)