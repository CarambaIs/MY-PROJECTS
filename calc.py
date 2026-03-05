def main():
    print("Welcome to my calculator\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
   
    while True:
        try:
            temp = int(input("Choose 1-4: ").strip())
            if temp not in [1, 2, 3, 4]:
                print("Wrong input!")
                continue
            break
        except ValueError:
            print("Wrong input!")

    while True:
        try:
            a = float(input("Input first number: "))
            b = float(input("Input second number: "))
            break
        except ValueError:
            print("Wrong input! Enter numbers only.")

    print("Result:", end=" ")

    if temp == 1:
        print(a + b)
    elif temp == 2:
        print(a - b)
    elif temp == 3:
        print(a * b)
    elif temp == 4:
        if b == 0:
            print("You cant divide by zero!")
        else:
            print(a / b)

main()