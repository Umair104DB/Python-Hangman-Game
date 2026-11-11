import random

WORDS = ["python", "stream", "planet", "coding", "garden"]
MAX_WRONG_GUESSES = 6


def play_game():
    secret = random.choice(WORDS)
    guessed = set()
    wrong = 0
    print("\nWelcome to Hangman!")
    print("Guess the hidden word one letter at a time.")
    while wrong < MAX_WRONG_GUESSES:
        display = " ".join(letter if letter in guessed else "_" for letter in secret)
        print(f"\nWord: {display} | Wrong guesses left: {MAX_WRONG_GUESSES - wrong}")
        if all(letter in guessed for letter in secret):
            print("Congratulations! You guessed the word.")
            return
        guess = input("Enter one letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one alphabetic letter.")
            continue
        if guess in guessed:
            print("You already tried that letter.")
            continue
        guessed.add(guess)
        if guess not in secret:
            wrong += 1
            print("That letter is not in the word.")
        else:
            print("Good guess!")
    print(f"Game over. The word was: {secret}")


if __name__ == "__main__":
    while True:
        play_game()
        if input("Play again? (y/n): ").strip().lower() != "y":
            print("Thanks for playing!")
            break
