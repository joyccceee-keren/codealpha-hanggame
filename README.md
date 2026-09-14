# 🎮 CodeAlpha Task 1: Hangman Game (Python)

A clean, interactive, text-based **Hangman Game** developed in Python as part of the **CodeAlpha Python Programming Internship (Month 1 - Task 1)**.

---

## 📌 Project Overview & Task Specifications

The goal of this task is to create a console-based Hangman game where the player attempts to guess a randomly chosen hidden word by guessing one letter at a time.

### 📋 Requirements Met:
- **Predefined Word List**: Contains 5 predefined words (`"python"`, `"codealpha"`, `"developer"`, `"internship"`, `"programming"`).
- **Guess Limit**: Strictly limited to **6 incorrect guesses** (standard Hangman rules).
- **Pure Console Interface**: Clean text-based interface featuring ASCII art for the hangman gallows.
- **Key Concepts Demonstrated**:
  - `random` module for selecting words.
  - `while` loop for managing turn-based game progression.
  - `if-else` statements for validation and conditional branching.
  - `strings` and `lists` for tracking guessed letters and masked display.

---

## ✨ Features

- 🎨 **Visual ASCII Gallows**: Dynamic hangman visual stages update after every incorrect guess (from 0 to 6 mistakes).
- 🛡️ **Robust Input Validation**:
  - Rejects numbers, special characters, and multi-letter inputs.
  - Alerts the user if a letter has already been guessed without penalizing attempts.
- 🔄 **Replay System**: Option to play multiple rounds seamlessly.
- ⚡ **Graceful Termination**: Handles keyboard interrupts (`Ctrl+C`) cleanly.

---

## 🚀 How to Run

### Prerequisites
- Python 3.x installed on your system.

### Running the Game
1. Open a terminal / command prompt in the project folder.
2. Run the following command:
   ```bash
   python hangman.py
   ```

---

## 🧪 Running Unit Tests

To run the automated test suite verifying game logic:
```bash
python -m unittest test_hangman.py
```

---

## 🕹️ Gameplay Preview

```text
========================================
   WELCOME TO THE CODEALPHA HANGMAN GAME!   
========================================
I have chosen a word with 6 letters.
You are allowed up to 6 incorrect guesses. Good luck!


       +---+
       |   |
           |
           |
           |
           |
    =========
    
Word: _ _ _ _ _ _
Incorrect guesses left: 6
----------------------------------------
Enter a letter to guess: p

>> Great job! 'p' is in the word!

       +---+
       |   |
           |
           |
           |
           |
    =========
    
Word: p _ _ _ _ _
Incorrect guesses left: 6
Guessed letters: p
----------------------------------------
Enter a letter to guess: 
```

---

## 📂 Project Structure

```text
codealpha-hanggame/
│
├── hangman.py          # Main game source code
├── test_hangman.py     # Unit tests verifying game constraints
├── run_game.bat        # Windows quick-launch script
└── README.md           # Documentation & instructions
```

