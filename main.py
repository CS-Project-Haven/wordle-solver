import random as rand

"""

== Wordle Solver ==

"""

ATTEMPTS = 6


def word_display(letter_array, holding_array):
    generated_word = ''
    for i in holding_array:
        if i != '':
            generated_word += f"| {i} |"
        else:
            generated_word += "| '' |"
    return print(generated_word)


def check_guess(user_guess, correct_word):
    letter_positions = ['', '', '', '', '']
    holding_array = []
    global ATTEMPTS
    if user_guess == correct_word:
        print(f"Correct! The word was {''.join(correct_word)}\n"
              f"You guessed with {ATTEMPTS} attempts remaining!")
        start()
    elif user_guess:
        for i, letter in enumerate(user_guess):
            if correct_word[i] == user_guess[i]:
                holding_array.append(letter)
            elif letter in correct_word:
                holding_array.append(letter + '*')
            elif letter in correct_word and letter in holding_array:
                holding_array.append('')
            else:
                holding_array.append('')
        ATTEMPTS -= 1

    else:
        print(f"None of these characters are in the word.")
        ATTEMPTS -= 1
    word_display(letter_positions, holding_array)


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
                  "0. Quit\n"
                  "1. Start Wordle\n"
                  "            ")
            choice = int(input("Pick an option: "))
            if choice == 0:
                break
            if choice == 1:
                guess()
        except:
            print("Input must be an integer!")
        else:
            print("There was an error!")


if __name__ == "__main__":
    start()
