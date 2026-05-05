firstItem = int(input("Enter the first number: ")) 
operation = str(input("Enter the operation (+, -, *, /): "))
secondItem = int(input("Enter the second number: "))
if operation == "+":
    print(firstItem + secondItem)
elif operation == "-":
    print(firstItem - secondItem)
elif operation == "*":
    print(firstItem * secondItem)
elif operation == "/":
    if secondItem != 0:
        print(firstItem / secondItem)
    else:
        print("Error: division by zero is not allowed.")
else:
    print("Error: invalid operation.")