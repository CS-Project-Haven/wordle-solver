import itertools
import random as rand

"""

== Wordle Solver ==

"""


def start():

    # file_name = "valid_words.txt"
    #
    # rng = rand.Random(0)
    # line_count = sum(1 for _ in open(file_name))
    # random_index0 = rng.randint(0, line_count - 1)
    # random_line = next(itertools.islice(open(file_name), random_index0, None))
    #
    # print(random_line)

    with open("valid_words.txt") as f:
        lines = f.readlines()
        print(rand.choice(lines))


if __name__ == "__main__":
    start()
