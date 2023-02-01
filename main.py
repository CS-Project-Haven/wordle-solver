import random as rand

"""

== Wordle Solver ==

"""

ATTEMPTS = 6


def check_guess(user_guess, correct_word):
    common_chars = set(user_guess) & set(correct_word)
    if user_guess == correct_word:
        print(f"Correct! The word was {''.join(correct_word)}\n"
              f"You guessed with {ATTEMPTS} attempts remaining!")
        start()
    elif common_chars:
        for i in common_chars:
            if i in correct_word:
                print(f"{i} is not in the correct position.")

    else:
        print(f"None of these characters are in the word.")


def guess():
    correct_word = generate_word()
    while ATTEMPTS > 0:
        user_guess = input("Guess the word: ")
        with open('valid_words.txt') as f:
            if user_guess.upper() not in f.read():
                print(f"{user_guess} is not a valid input.")
            else:
                user_guess_split = [*user_guess]
                check_guess(user_guess_split, correct_word)


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
        except TypeError:
            print("Input must be an integer!")
        else:
            continue


if __name__ == "__main__":
    start()
