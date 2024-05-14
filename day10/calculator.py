import os
clear = lambda: os.system('cls')
from art import logo

def add(n1: float, n2: float):
    return n1 + n2

def subtract(n1: float, n2: float):
    return n1 - n2

def multiply(n1: float, n2: float):
    return n1 * n2

def divide(n1: float, n2: float):
    return n1 / n2

operations ={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
    num1 = float(input("Whats the first number: "))

    for op in operations:
        print(op)
        

    should_continue = True

    while should_continue:
        symbol = input("Pick an peration from the lines above: ")
        num2 = float(input("Whats the next number: "))
        


        
        

        answer = operations[symbol](num1, num2)

        print(f"{num1} {symbol} {num2} = {answer}")
        
        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to exit: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()
            
calculator()