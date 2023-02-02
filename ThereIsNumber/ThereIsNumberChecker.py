x = int(input("Enter the quantity of the words(Min is 6): "))

numbers = []

if x >= 6:
    for i in range(1,x+1):
        n = int(input("Enter the number: "))
        if n in numbers:
            print("yes")
            continue
        else:
            print("No")
        numbers.append(n)

else:
    print("Minimum is 6")

    