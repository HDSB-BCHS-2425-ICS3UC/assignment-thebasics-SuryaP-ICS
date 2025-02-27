# om
import math
pi = math.pi

dim = input ("2d or 3d: ")
if dim == "2d":
    S = input("shape? circle,rectangle or right angled triangle, if none input none!: ")
 # Circle
    if S== ("circle"):
        radius = float(input("enter the radius of the circle:"))

        C = input("area or perimiter?:")
        if C == "area":
            area= (math.pi)*(pow(radius,2))
            print(("This is the area of your circle:"),area)
        elif C == ("perimiter:"):
            perimiter = 2*(math.pi)*(radius)
            print ("this is your perimiter:", perimiter)
# Rectangle
    elif S==("rectangle"):
        SL = float(input('enter the side length of the rectangle:'))
        W = float(input("enter the width:"))
        G = input("area or perimiter:")
        if G == ("area"):
            area = SL*W
            print("this is your area:",area)
        elif G == ("perimiter"):
            perimiter = 2*(SL+W)
            print ("here is your perimiter:",perimiter)
# Right Angle Triangle
    elif S==("triangle"):
        As = float(input("enter the height of your triangle:"))
        Bs = float(input("enter the length of your triangle:"))
        PY= input("do you know all sides?:")
        if PY == ("yes"):
            Cs = float(input("enter the hypotenuse/slope of your triangle:"))
        elif PY == ("no"):
            pytha = (pow(As,2))+(pow(Bs,2))
            pylol = math.sqrt(pytha)
            pytho = (pylol)+As+Bs
            print ("this is the missing side:",pytho)
            area=(As*Bs)/2
            perimiter=As+Bs+(math.sqrt((pow(As,2)+(pow(Bs,2)))))
        K = input("area or perimiter?:")
        if K == ("area"):
            area=(As*Bs)/2
            print("this is your area!:", area)
        if K == ("perimiter"):
            perimiter=As+Bs+(math.sqrt((pow(As,2)+(pow(Bs,2)))))
            print("this is your perimiter!:",perimiter)
        
        
        
# Cube
elif dim == "3d":
    O = input("shape? cube,cylinder, cone or pyramid?: ")
    if O==("cube"):
        L = input("area or volume?")
        B= float(input("enter the base:"))
        area = 6*(pow(B,2))
        volume = (pow(B,3))
        if L ==("area"):
            print ("this is your area:",area)
        elif L ==("volume"):
            print ("this is your volume:",volume)
# Cylinder
    elif O ==("cylinder"):
        Hei = float(input("enter the height of your cylinder:"))
        Rad = float(input("enter the radius of the cylinder:"))
        areab = (math.pi*(pow(Rad,2)))
        arealat = 2*(math.pi*(Rad*Hei))
        areatot = 2*areab + arealat
        vol = (areab*Hei)
        D = input("surface area or volume?:")
        if D == ("surface area"):
            A = input("base, lateral surface or total?:")
            if A == ("base"):
                print("this is your area", areab)
            elif A== ("lateral surface"):
                print("this is the area", arealat)
            elif A==("total"):
                print("this is your area", areatot)
        elif D ==("volume"):
            print("this is your volume",vol)
# Cone
    elif O ==("cone"):
        Hei = float(input("enter the height of your cone:"))
        Rad = float(input("enter the radius of the cone:"))
        Slop = float(input("enter the hypotenuse/slope of your cone:"))
        ab = (math.pi(pow(Rad,2)))
        als = (math.pi*(Rad,Slop))
        alt = ab+als
        volume = (ab*Hei)/3
        Q = input("surface area or volume:")
        if Q== ("surface area"):
            T = input("base, lateral surface or total?:")
            if T== ("base"):
                print("this is your area:", ab)
            elif T== ("lateral surface"):
                    print("this is the area:", als)
            elif T==("total"):
                    print("this is your area:", alt)
        if Q== ("volume"):
            print("this is your volume",volume)
                
# Square based pyramid
    elif O==("pyramid"):
        ba= float(input("what is the base of the pyramid:"))
        hi = float(input("what is the height?:"))
        so= float(input("what is the slope of the pyramid?:"))
        H = input("surface area or volume?:")
        if H== ("surface area"):
            arb = (pow(ba,2))
            artri = (ba*so)/2
            arto = (arb)*2 + (artri)*4
            volum = (arb*hi)/3
            Y = input("base, triangles or total?:")
            if Y == ("base"):
                arb = (pow(ba,2))
                print("this is your base:",arb)
            elif Y == ("triangles"):
                artri = (ba*so)/2
                print("this is your triangle area",artri)
            elif Y == ("total"):
                arto = (arb)*2 + (artri)*4
                print("this is your total area",arto)
        elif H==("volume"):
            arb = (pow(ba,2))
            volum = (arb*hi)/3
            print("this is your volume", volum)

