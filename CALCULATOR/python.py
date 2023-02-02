# import math for sqrt
import math

while True:

    # Check if the user has entered an only integer
    try:
        num1 = float(input("\nFirst number:   "))
        num2 = float(input("Second number:  "))
    except ValueError:
        print("Input only integer!")
        continue
    
    option = input("\nOperation(+, -, *, /,**,sqrt) or type 'exit' to exit the menu: ")

    # If the user wants to exit, he can type just 'exit'
    if option.lower() == 'exit':
        print("bye\n")
        break

    elif option == "+":
        print(f"answer is {num1 + num2}")

    elif option == "-":
        print(f"answer is {num1 - num2}")

    elif option == "*":
        print(f"answer is {num1 * num2}")

    elif option == "**":
        print(f"answer is {num1**num2}")

    elif option.lower() == "sqrt":
        
        answer = input("Square root from which number (first, second or both)? ")
        if answer.lower() == "first":
            print(f"Square root from {num1} is {math.sqrt(num1)}")

        elif answer.lower() == "second":
            print(f"Square root from {num2} is {math.sqrt(num2)}")

        elif answer.lower() == "both":
            print(f"\nSquare root from {num1} is {math.sqrt(num1)}")
            print(f"Square root from {num2} is {math.sqrt(num2)}")    
        else:
            print("Incorrect!")

    elif option == "/":
        if num2 != 0:
            print(f"answer is {int(num1/num2)}")    
        else:
            print("UNDEFINED")
    else:
        print("incorrect reference")
