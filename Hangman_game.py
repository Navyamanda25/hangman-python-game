import random
import hangman_stages
import word_list

def play_game(lives, score):
    category = random.choice(list(word_list.WORDS.keys()))
    chosen_word = random.choice(word_list.WORDS[category]).lower()
    word_length = len(chosen_word)
    display = ["_"] * word_length
    guessed_letters = set()
    correct_guesses = 0

    print("\n Welcome to Hangman Game!")
    print(f" Hint: The word is related to '{category}'.")
    print(f" Lives: {lives}")
    print(" ".join(display))
    print(hangman_stages.stages[lives])

    game_over = False

    while not game_over:
        guessed_letter = input("\n Guess a letter: ").lower()

        if not guessed_letter.isalpha() or len(guessed_letter) != 1:
            print(" Please enter only one valid letter (a-z).")
            continue

        if guessed_letter in guessed_letters:
            print(f"You already guessed '{guessed_letter}'. Try another letter.")
            continue
        guessed_letters.add(guessed_letter)

        if guessed_letter in chosen_word:
            for position in range(word_length):
                if chosen_word[position] == guessed_letter:
                    display[position] = guessed_letter
            correct_guesses += 1
            print(" Correct!")

            # Bonus life system
            if correct_guesses % 3 == 0 and lives < 6:
                lives += 1
                print(" Bonus! You earned +1 extra life!")
        else:
            lives -= 1
            print(f" Wrong! You lost a life. Lives left: {lives}")

        print(" ".join(display))
        if lives >= 0:
            print(hangman_stages.stages[lives])

        if "_" not in display:
            print(f"\n You win! The word was '{chosen_word}'.")
            score["wins"] += 1
            game_over = True

        if lives == 0:
            print(f"\n You lost! The word was '{chosen_word}'.")
            score["losses"] += 1
            game_over = True

    return score


def choose_difficulty():
    print("\nSelect difficulty level:")
    print("1️*Easy (6 lives)")
    print("2️*Medium (4 lives)")
    print("3️*Hard (3 lives)")
    while True:
        choice = input("Enter your choice (1/2/3): ").strip()
        if choice == "1":
            return 6
        elif choice == "2":
            return 4
        elif choice == "3":
            return 3
        else:
            print("Invalid input. Please choose 1, 2, or 3.")


# MAIN PROGRAM 
score = {"wins": 0, "losses": 0}

while True:
    lives = choose_difficulty()
    score = play_game(lives, score)

    print("\n Current Score:")
    print(f" Wins: {score['wins']}")
    print(f" Losses: {score['losses']}")

    choice = input("\nDo you want to play again? (y/n): ").lower()
    if choice != "y":
        print("\n Final Score Summary:")
        print(f" Wins: {score['wins']}")
        print(f" Losses: {score['losses']}")
        print("Thanks for playing! Goodbye See you Again!!")
        break
