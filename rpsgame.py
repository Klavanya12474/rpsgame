import random

user_score = 0
computer_score = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Choose rock, paper, or scissors (or 'q' to quit): ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        print("Invalid input. Try again.")
        continue

    random_number = random.randint(0, 2)
    computer_input = options[random_number]
    print("Computer picked:", computer_input + ".")

    if user_input == "rock" and computer_input == "scissors":
        user_score += 1
        print("You win!")
    elif user_input == "scissors" and computer_input == "paper":
        user_score += 1
        print("You win!")
    elif user_input == "paper" and computer_input == "rock":
        user_score += 1
        print("You win!")
    elif user_input == computer_input:
        print("It's a tie!")
    else:
        computer_score += 1
        print("Computer wins. You lost.")

print("You won", user_score, "times.")
print("Computer won", computer_score, "times.")
