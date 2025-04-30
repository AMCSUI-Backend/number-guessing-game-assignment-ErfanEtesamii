import random

def play_game():
    number = random.randint(1, 100)
    max_attempts = 5
    attempts = 0

    while attempts < max_attempts:
        user_input = input(f"Attempt {attempts + 1} of {max_attempts}. Guess a number between 1 and 100: ")

        try:
            guess = int(user_input)
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
            continue

        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Congratulations! You guessed it!")
            print(f"You guessed it in {attempts} attempts.")
            break
    else:
        print(f"Sorry, you've used all {max_attempts} attempts. The number was {secret_number}.")

while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again not in ('yes', 'y'):
        print("Thanks for playing!")
        break
