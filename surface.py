print("WELCOME TO THE SURFACE AREA CALCULATOR") #welcome message
shape = str(input("Insert one of these shapes: S(square), R(rectangle), T(triangle), C(circle)"))
if shape == "S":
    side = int(input("Insert the side of the square: "))
    area = side*side
    print("The area of the square is: ", area)
elif shape == "R":
    base = int(input("Insert the base of the rectangle: "))
    height = int(input("Insert the height of the rectangle: "))
    area = base*height
    print("The area of the rectangle is: ", area)
elif shape == "T":
    base = int(input("Insert the base of the triangle: "))
    height = int(input("Insert the height of the triangle: "))
    area = (base*height)/2
    print("The area of the triangle is: ", area)
elif shape == "C":
    radius = int(input("Insert the radius of the circle: "))
    area = 3.14*radius*radius
    print("The area of the circle is: ", area)
else:
    print("Invalid shape, please insert one of the following: S, R, T, C")