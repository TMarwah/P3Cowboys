class Calculator:
    list = []
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        return x / y

    print("Please select operation -\n" \
          "1. Add\n" \
          "2. Subtract\n" \
          "3. Multiply\n" \
          "4. Divide\n")


    select = int(input("Select operations form 1, 2, 3, 4 :"))

    numero_1 = int(input("Enter first number: "))
    numero_2 = int(input("Enter second number: "))

    if select == 1:
        print(numero_1, "+", numero_2, "=",
              add(numero_1, numero_2))

    elif select == 2:
        print(numero_1, "-", numero_2, "=",
              subtract(numero_1, numero_2))

    elif select == 3:
        print(numero_1, "*", numero_2, "=",
              multiply(numero_1, numero_2))

    elif select == 4:
        print(numero_1, "/", numero_2, "=",
              divide(numero_1, numero_2))
    else:
        print("Invalid input")



















    print ("[5]")
