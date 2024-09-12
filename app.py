import random

def hangman():
    words = ['python', 'java', 'kotlin', 'javascript']
    word = random.choice(words)
    guessed_word = ['_'] * len(word)
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman!")
    
    while attempts > 0:
        print("\n" + " ".join(guessed_word))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
            if '_' not in guessed_word:
                print("\n" + " ".join(guessed_word))
                print("Congratulations! You've guessed the word correctly!")
                break
        else:
            attempts -= 1
            print(f"Incorrect! You have {attempts} attempts left.")

    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The word was '{word}'.")

hangman()
