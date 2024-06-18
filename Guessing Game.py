import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    guess = None
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100.")
    print("Try to guess it!\n")

    while guess != secret_number:
        try:
            # Get the user's guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Check if the guess is too high, too low, or correct
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")

if __name__ == "__main__":
    number_guessing_game()
