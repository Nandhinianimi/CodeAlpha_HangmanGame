import random

# List of 5 predefined words
words = ["apple", "tiger", "house", "plant", "beach"]

# Choose a random word
word = random.choice(words)

# Create blanks for the word
display = ["_"] * len(word)

# Allow 6 incorrect guesses
wrong_guesses = 0
max_wrong_guesses = 6

print("Welcome to Hangman!")

# Main game loop
while wrong_guesses < max_wrong_guesses and "_" in display:
    print("\nWord:", " ".join(display))
    print("Guesses left:", max_wrong_guesses - wrong_guesses)

    guess = input("Enter a letter: ").lower()

    # Check if the guessed letter is in the word
    if guess in word:
        print("Correct!")

        # Reveal matching letters
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        print("Wrong!")
        wrong_guesses += 1

# Game result
if "_" not in display:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)