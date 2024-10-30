# Creating functions for the calculator that will perform the operation
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Adding these 4 functions to the dictionary as values.  Keys = "+", "-", "*", "/"
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

#Using dictionary operations to perform the calculations. Multiply 4*8.
import art
print(art.logo)
def calculator():
    first = float(input("Enter the first number:"))
    go_again =  True
    while go_again:
        for oper in operations:
            print(oper)
        choose = input("What would you like to do?")
        second = float(input("Enter the second number:"))
        result = operations[choose](first, second)
        print(f"{first} {choose}{second} = {result}")

        asking = input("Do you want to continue working on the previous result i.e ? 'y' or 'n'")
        if asking == "y":
            first = result
        else:
            print("\n"*100)
            go_again = False
            calculator()


calculator()
