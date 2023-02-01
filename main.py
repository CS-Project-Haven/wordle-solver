import random as rand

"""

== Wordle Solver ==

"""

ATTEMPTS = 6


def check_guess(user_guess, correct_word):
    if user_guess == correct_word:
        print(f"Correct! The word was {''.join(correct_word)}\n"
              f"You guessed with {ATTEMPTS} attempts remaining!")
    elif set(user_guess) & set(correct_word):
        print(f"")

    else:
        print("")


def guess():
    correct_word = generate_word()
    while ATTEMPTS > 0:
        user_guess = input("Guess the word: ")
        with open('valid_words.txt') as f:
            if user_guess not in f.read():
                print(f"{user_guess} is not a valid input.")
            else:
                user_guess_split = [*user_guess]
                check_guess(user_guess_split, correct_word)


def generate_word():
    with open("valid_words.txt") as f:
        lines = f.readlines()
        rand_word = rand.choice(lines)
        [*rand_word].pop(-1)
        return [*rand_word]


def start():
    guess()


if __name__ == "__main__":
    start()
