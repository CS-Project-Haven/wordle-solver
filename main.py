import random as rand

"""

== Wordle Solver ==

"""

ATTEMPTS = 6


def check_guess(user_guess, correct_word):
    global ATTEMPTS
    if user_guess == correct_word:
        print(f"Correct! The word was {''.join(correct_word)}\n"
              f"You guessed with {ATTEMPTS} attempts remaining!")
        start()
    elif user_guess:
        for i, letter in enumerate(user_guess):
            if correct_word[i] == user_guess[i]:
                print(f"{letter} is in the correct position.")
            elif letter in correct_word:
                print(f"{letter} in incorrect position.")
            else:
                print(f"{letter} is not in this word.")
        ATTEMPTS -= 1

    else:
        print(f"None of these characters are in the word.")
        ATTEMPTS -= 1


def guess():
    correct_word = generate_word()
    while ATTEMPTS > 0:
        user_guess = input("Guess the word: ")
        with open('valid_words.txt') as f:
            if len(user_guess.upper()) != 5:
                print("Input must be 5 characters long!")
            elif user_guess.upper() not in f.read():
                print(f"{user_guess.upper()} is not a valid input.")
            else:
                user_guess_split = [*user_guess.upper()]
                check_guess(user_guess_split, correct_word)
    print(f"You ran out of attempts!\n The word was {''.join(correct_word)}!")
    start()


def generate_word():
    with open("valid_words.txt") as f:
        lines = f.readlines()
        rand_word = rand.choice(lines)
        split_word = [*rand_word]
        split_word.pop(-1)
        print(split_word)
        return split_word


def start():
    while True:
        try:
            print("\n"
                  "1. Start Wordle\n"
                  "            ")
            choice = int(input("Pick an option: "))
            if choice == 1:
                guess()
        except:
            print("Input must be an integer!")
        else:
            break


if __name__ == "__main__":
    start()
