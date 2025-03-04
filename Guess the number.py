import random

def choose_difficulty():
    """Ask the user to choose a difficulty level and return the number of attempts allowed."""
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
        if difficulty in ["easy", "hard"]:
            return 10 if difficulty == "easy" else 5
        print("Invalid choice. Please type 'easy' or 'hard'.")

def get_user_guess():
    """Prompt the user to enter a valid number between 1 and 100."""
    while True:
        try:
            guess = int(input("Make a guess: "))
            if 1 <= guess <= 100:
                return guess
            print("Out of bounds! Please guess a number between 1 and 100.")
        except ValueError:
            print("Invalid input! Please enter an integer.")

def play_game():
    """Main game function to handle number guessing logic."""
    print("\n🎯 Welcome to the Number Guessing Game! 🎯")
    print("I'm thinking of a number between 1 and 100.")
    
    num_to_guess = random.randint(1, 100)
    attempts = choose_difficulty()

    while attempts > 0:
        print(f"\n🔢 You have {attempts} attempts remaining.")
        guess = get_user_guess()

        if guess == num_to_guess:
            print("\n🎉 Congratulations! You guessed the number! 🎉")
            return
        
        attempts -= 1
        if attempts == 0:
            print(f"\n😢 You're out of guesses. The correct number was {num_to_guess}.")
        elif guess < num_to_guess:
            print("📉 Too low. Try again!")
        else:
            print("📈 Too high. Try again!")

def main():
    """Run the game loop, allowing users to play multiple times."""
    while True:
        play_game()
        play_again = input("\n🔄 Do you want to play again? Type 'again' or 'stop': ").strip().lower()
        if play_again == "stop":
            print("\n👋 Goodbye! Thanks for playing!")
            break

if __name__ == "__main__":
    main()
