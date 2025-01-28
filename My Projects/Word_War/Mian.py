import random
import os

game_title = "Word Raider"

# Set up the list of words to choose from
word_bank = []

# Use a raw string for the file path
txt_file = r"C:\Users\mayyu\Documents\All-Refference-Code\1.Python\My Projects\Word_War\words.txt"

# Check if the file exists
if not os.path.exists(txt_file):
    print(f"Error: The file {txt_file} does not exist.")
else:
    # Open and read the file
    with open(txt_file, 'r') as word_file:
        for line in word_file:
            word_bank.append(line.rstrip().lower())

    # Check if the word bank is not empty
    if not word_bank:
        print("Error: The word bank is empty.")
    else:
        # Pick a random word from the list
        word_to_guess = random.choice(word_bank)

        # Set up the game variables
        misplaced_guesses = []
        incorrect_guesses = []
        max_turns = 5
        turns_taken = 0

        # Display the initial game state
        print("Welcome to", game_title)
        print("The word has", len(word_to_guess), "letters.")
        print("You have", max_turns - turns_taken, "turns left.")

        while turns_taken < max_turns:
            # Get the player's guess
            guess = input("Guess a word: ").lower()

            # Check if the guess length equals the word length and is all alpha letters
            if len(guess) != len(word_to_guess) or not guess.isalpha():
                print(f"Please enter a {len(word_to_guess)}-letter word.")
                continue

            # Check each letter in the guess against the word's letters
            index = 0
            for c in guess:
                if c == word_to_guess[index]:
                    print(c, end=" ")
                    if c in misplaced_guesses:
                        misplaced_guesses.remove(c)
                elif c in word_to_guess:
                    if c not in misplaced_guesses:
                        misplaced_guesses.append(c)
                    print("_", end=" ")
                else:
                    if c not in incorrect_guesses:
                        incorrect_guesses.append(c)
                    print("_", end=" ")
                index += 1

            print("\n")
            print("Misplaced letters: ", misplaced_guesses)
            print("Incorrect letters: ", incorrect_guesses)
            turns_taken += 1

            # Check if the player has won
            if guess == word_to_guess:
                print("Congratulations, you win!")
                break

            # Check if the player has lost
            if turns_taken == max_turns:
                print("Sorry, you lost. The word was", word_to_guess)
                break

            # Display the number of turns left and ask for another guess
            print("You have", max_turns - turns_taken, "turns left.")
