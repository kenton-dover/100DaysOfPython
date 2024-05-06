import random


rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Write your code below this line 👇

action = input("Rock, Paper, or Scissors\n")
action = action.lower()

actions = ["rock", "paper", "scissors"]

gameConditions = {
    "rock,rock": "draw",
    "rock,paper": "lose",
    "rock,scissors": "win",
    "paper,rock": "win",
    "paper,paper": "draw",
    "paper,scissors": "lose",
    "scissors,rock": "lose",
    "scissors,paper": "win",
    "scissors,scissors": "draw",
}

systemAction = random.choice(actions)

game = action + "," + systemAction
print("The computer chose " + systemAction)

if game in gameConditions:
    print(gameConditions[game])
