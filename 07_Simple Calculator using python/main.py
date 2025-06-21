try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    print("What kind of operator do you want to perform?.\nPress + for addition.\nPress - for subtraction.\nPress * for division.\nPress / for division.")

    o = input("Enter the operation you want to perform : ")
    match o:
        case "+":
            print(f"The result is {a + b}")
        case "-":
            print(f"The result is {a - b}")
        case "*":
            print(f"The result is {a * b}")
        case "/":
            print(f"The result is {a / b}")
        case default:
            print("Invalid Input")

except Exception as e:
    print("Enter a valid value of a and b")