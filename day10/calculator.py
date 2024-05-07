import os
clear = lambda: os.system('cls')


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

num1 = int(input("Whats the first number: "))
num2 = int(input("Whats the second number: "))

for op in operations:
    print(op)
    
symbol = input("Pick an peration from the lines above: ")

answer = operations[symbol](num1, num2)

print(f"{num1} {symbol} {num2} = {answer}")