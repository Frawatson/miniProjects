print("+++++++++++++++++++++++++++++")
print("P12 Calculator")
print("+++++++++++++++++++++++++++++")
print("P12 allows for Addition, Subtraction, Division, Multiplication, and Exponential")
print("+++++++++++++++++++++++++++++")
print("input 1 for Addition, 2 for Subtraction, 3 for Division, 4 for Multiplication, and 5 for Exponential")
print("+++++++++++++++++++++++++++++")

while True:
    cal = int(input("Choose your tool: " ))

    def add(x, y):
        return x + y

    def sub(x, y):
        return x - y

    def div(x, y):
        return x / y

    def mul(x, y):
        return x * y

    def expo(x, y):
        return x ** y


    if cal == 1:
        add1 = int(input("Input first number: "))
        add2 = int(input("Input second number: "))
        print("===================")
        print(add(add1, add2))
        print("===================")
    elif cal == 2:
        sub1 = int(input("Input first number: "))
        sub2 = int(input("Input second number: "))
        print("===================")
        print(sub(sub1, sub2))
        print("===================")
    elif cal == 3:
        div1 = int(input("Input first number: "))
        div2 = int(input("Input second number: "))
        print("===================")
        print(div(div1, div2))
        print("===================")
    elif cal == 4:
        mul1 = int(input("Input first number: "))
        mul2 = int(input("Input second number: "))
        print("===================")
        print(mul(mul1, mul2))
        print("===================")
    elif cal == 5:
        expo1 = int(input("Input first number: "))
        expo2 = int(input("Input second number: "))
        print("===================")
        print(expo(expo1, expo2))
        print("===================")
    else:
        print("===================")
        print("Invalid!! Enter one of the above value.")
        print("===================")
        print("***************************")
    useCalculator = input("Play again? (y/n)")
    print("***************************")
    if useCalculator.lower() != "y":
        break