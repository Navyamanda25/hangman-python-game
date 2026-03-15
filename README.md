# hangman-python-game
A command-line Hangman game built with Python featuring categories, difficulty levels, score tracking, and ASCII graphics.
#  Hangman Game (Python)

A command-line Hangman game built using Python.  
Players guess letters to reveal a hidden word while managing limited lives.

---

##  Features

- Multiple word categories
- Difficulty levels (Easy / Medium / Hard)
- ASCII Hangman graphics
- Score tracking system
- Bonus life reward system
- Input validation

---

##  Project Structure

hangman-game/
│
├── Hangman_game.py      # Main game logic
├── hangman_stages.py    # ASCII hangman visuals
├── word_list.py         # Word categories and word bank

---

##  How to Run

1. Install Python (3.x)
2. Clone the repository

git clone https://github.com/yourusername/hangman-python-game.git


3. Navigate to project folder

cd hangman-python-game


4. Run the game

python Hangman_game.py

---

##  Difficulty Levels

Easy → 6 lives  
Medium → 4 lives  
Hard → 3 lives  

---

##  How the Game Works

- A random word is selected from a category.
- The player guesses letters.
- Correct letters reveal positions.
- Incorrect guesses reduce lives.
- Every 3 correct guesses gives a bonus life.

---

##  Example Gameplay

Hint: The word is related to 'Animals'

_ _ _ _ _

Guess a letter: a

Correct!

---

##  Technologies Used

Python  
Random module  
CLI Interface  

---

##  Author

Navya Lakshmi

GitHub: https://github.com/Navyamanda25

