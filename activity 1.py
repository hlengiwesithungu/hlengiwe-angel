print("Simple Calculator")

try:
    num1 = float(input("Enter first number: "))
    
    num2 = float(input("Enter second number: "))

    print("Choose an operator: +, -, *, /")
    operator = input("Enter operator: ")

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
    
        if num2 == 0:
            print("Error: Cannot divide by zero!")
            exit()
        else:
            result = num1 / num2
    else:
        print("Invalid operator selected!")
        exit()

    print("Result:", result)

except ValueError:
    print("Error: Please enter a valid number only.")