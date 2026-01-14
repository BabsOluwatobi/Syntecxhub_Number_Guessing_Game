import random

def choose_difficulty():
    print("\nSelect Difficulty Level:")
    print("1. Easy (1 to 10)")
    print("2. Medium (1 to 50)")
    print("3. Hard (1 to 100)")

    while True:
        level = input("Enter 1, 2, or 3: ")

        if level == "1":
            return 10
        elif level == "2":
            return 50
        elif level == "3":
            return 100
        else:
            print("Invalid choice. Try again.")

def play_game():
    max_number = choose_difficulty()
    secret_number = random.randint(1, max_number)
    attempts = 0

    print(f"\n You have chosen a number between 1 and {max_number}.")
    print("Try to guess it!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Sorry, too low!")
            elif guess > secret_number:
                print("Sorry, too high!")
            else:
                print(f" Correct! You guessed it in {attempts} attempts.")
                return attempts

        except ValueError:
            print("Please enter a valid number.")

def main():
    best_score = None

    print("Welcome to the Number Guessing Game!")

    while True:
        attempts = play_game()

        if best_score is None or attempts < best_score:
            best_score = attempts
            print("🏆 New best score!")

        print(f"Best score so far: {best_score} attempts")

        replay = input("\nDo you want to play again? (yes/no): ").lower()
        if replay != "yes":
            print("Thanks for playing! Goodbye 👋")
            break

main()
