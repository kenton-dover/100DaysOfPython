import random


def compare(guess: int, number: int):
    if guess > number:
        return 1
    if guess < number:
        return -1
    return 0


number = random.randint(1, 100)
guesses = 0
difficulty = input("Select your difficulty: hard/easy ").lower()
if difficulty == "hard":
    guesses = 5
else:
    guesses = 10
won = False

while guesses > 0 and not won:
    guesses -= 1
    guess = int(input("What is your number? "))
    result = compare(guess, number)
    if result > 0:
        print("Too high")
    if result < 0:
        print("Too low")
    if result == 0:
        print("Correct")
        won = True

if not won:
    print("You lost")
