import random

# Visual representation of the Hangman stages (0 to 6 incorrect guesses)
HANGMAN_PICS = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

# Predefined list of 5 words (as per task specifications)
WORDS = ["python", "codealpha", "developer", "internship", "programming"]

MAX_INCORRECT_GUESSES = 6


def display_game_status(secret_word, guessed_letters, incorrect_guesses):
    """
    Displays the current hangman visual, the word with revealed letters,
    and remaining attempts.
    """
    print(HANGMAN_PICS[incorrect_guesses])
    
    # Reveal guessed letters, display underscores for unrevealed letters
    word_display = [letter if letter in guessed_letters else "_" for letter in secret_word]
    print(f"Word: {' '.join(word_display)}")
    print(f"Incorrect guesses left: {MAX_INCORRECT_GUESSES - incorrect_guesses}")
    
    # Show all guessed letters
    if guessed_letters:
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
    print("-" * 40)


def play_hangman():
    """Main game function to run a round of Hangman."""
    # Concept: random selection from a list
    secret_word = random.choice(WORDS).lower()
    
    # Concept: lists and strings for state tracking
    guessed_letters = []
    incorrect_guesses = 0
    
    print("\n" + "=" * 40)
    print("   WELCOME TO THE CODEALPHA HANGMAN GAME!   ")
    print("=" * 40)
    print(f"I have chosen a word with {len(secret_word)} letters.")
    print(f"You are allowed up to {MAX_INCORRECT_GUESSES} incorrect guesses. Good luck!\n")
    
    # Concept: while loop for game progression
    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        display_game_status(secret_word, guessed_letters, incorrect_guesses)
        
        # Concept: input handling
        guess = input("Enter a letter to guess: ").strip().lower()
        
        # Concept: if-else statements for validation & game logic
        if len(guess) != 1 or not guess.isalpha():
            print("\n>> Invalid input! Please enter a single alphabetical letter.\n")
            continue
            
        if guess in guessed_letters:
            print(f"\n>> You already guessed '{guess}'. Try a different letter!\n")
            continue
            
        guessed_letters.append(guess)
        
        if guess in secret_word:
            print(f"\n>> Great job! '{guess}' is in the word!")
            # Check if player has guessed all letters in the secret word
            if all(letter in guessed_letters for letter in secret_word):
                print(HANGMAN_PICS[incorrect_guesses])
                print(f"Word: {' '.join(list(secret_word))}")
                print("\n" + "*" * 40)
                print("   CONGRATULATIONS! YOU WON! 🎉")
                print(f"   You guessed the word: '{secret_word.upper()}'")
                print("*" * 40 + "\n")
                return
        else:
            incorrect_guesses += 1
            print(f"\n>> Sorry, '{guess}' is not in the word.")
    
    # If the loop finishes because attempts reached 0
    print(HANGMAN_PICS[incorrect_guesses])
    print("\n" + "!" * 40)
    print("   GAME OVER! YOU RAN OUT OF ATTEMPTS! 💀")
    print(f"   The secret word was: '{secret_word.upper()}'")
    print("!" * 40 + "\n")


def main():
    try:
        while True:
            play_hangman()
            replay = input("Do you want to play again? (y/n): ").strip().lower()
            if replay != 'y':
                print("\nThank you for playing! Goodbye!\n")
                break
    except (KeyboardInterrupt, EOFError):
        print("\n\nGame exited. Thank you for playing!\n")


if __name__ == "__main__":
    main()

