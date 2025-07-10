import random

def number_guess_game():
    secret_number = random.randint(1, 10)
    attempts = 0

    print("🎯 Welcome to the Number Guess Game!")
    print("Guess the number between 1 and 10.")  

    while True:
        guess = input("\nEnter your guess: ")

        if not guess.isdigit():
            print("⚠ Invalid input! Please enter a number between 1 and 10.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < 1 or guess > 10:
            print("⚠ Out of range! Guess a number between 1 and 10.")
        elif guess < secret_number:
            print("🔼 Too low! Try again.")
        elif guess > secret_number:
            print("🔽 Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed the number {secret_number} in {attempts} tries.")
            break

# Run the game
number_guess_game()