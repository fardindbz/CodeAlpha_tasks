import random

def hangman():
    words = ["python", "programming", "hangman", "challenge", "developer", "algorithm", "function"]
    
    word = random.choice(words)
    guessed_word = ["_"] * len(word)
    attempts = 6  
    guessed_letters = set()

    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")
    print("You have 6 incorrect guesses available.")
    print(" ".join(guessed_word))

    while attempts > 0:
        guess = input("\nEnter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            for idx, letter in enumerate(word):
                if letter == guess:
                    guessed_word[idx] = guess
        else:
            attempts -= 1
            print(f"Wrong guess! '{guess}' is not in the word. Attempts left: {attempts}")

        print(" ".join(guessed_word))

        if "_" not in guessed_word:
            print("\n Congratulations! You guessed the word:", word)
            break
    else:
        print("\n Game over! The word was:", word)

hangman()