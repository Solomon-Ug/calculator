print("🎮 Welcome to the Number Guessing Game! 🎮")
print("I have picked a secret number between 1 and 100.")
print("You have 4 attempts to guess it.\n")

secret_number = 67
attempts = 10

for attempt in range(1, attempts + 1):
    try:
        guess = int(input(f"Attempt {attempt}/{attempts} - Enter your guess: "))

        if guess < 1 or guess > 100:
            print(" Please enter a number between 1 and 100!")
            continue

        if guess == secret_number:
            print(f" Congratulations! You guessed it right. The number was {secret_number}!")
            break

        elif guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number. ️")

    except ValueError:
        print("Invalid input! Please enter a valid number.")
        continue

else:
    # This runs only if the loop completes without breaking (all attempts used)
    print(f"\n Game Over! You ran out of attempts.")
    print(f"The secret number was {secret_number}.")

print("\nThanks for playing!")