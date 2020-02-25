# Written by Bronson Schultz
# For use by Ian Small, for educational purposes.
# Generate a random cord progression and bridge to practice for upcoming
# musical jury assessment
from string import ascii_uppercase
import random as rand


def read_file(file_name):
    """
    read in a file and save it's contents as a nested list
    :param file_name: name of the file
    :return: a list of lines of the file
    """
    items = list()
    with open(file_name) as file:
        for line in file:
            items.append(line.strip())

    return items


def get_keys():
    """
    Generate all of required musical keys for progressions, including redundant scales
    :return: list of needed keys
    """
    keys = list()
    for i in range(7):
        keys.append(ascii_uppercase[i])
        if i != 1 and i != 4:
            keys.append(ascii_uppercase[i] + "#")
        if i != 0 and i != 2 and i != 5:
            keys.append(ascii_uppercase[i] + "b")
    return keys


def print_rand_progression(progs_list, keys_list):
    """
    generate one random progression in one random key
    :pre the file of progressions has already been read
    :param progs_list: list of possible progressions
    :param keys_list: list of possible keys
    :post: print a progression in a key
    :return: none
    """
    prog = rand.choice(progs_list)
    key = rand.choice(keys_list)
    print(prog, "in", key)


def get_rand_bridge(bridge_list):
    """
    print a random possible bridge
    :param bridge_list: list of bridges
    :return: the random bridge chosen
    """
    return rand.choice(bridge_list)


def print_n_practice_problems(n, progs_list, keys_list, bridge_list):
    """
    prints n progression test practice problems
    :param n: integer from user input
    :param progs_list: list of all possible progressions
    :param keys_list: list of all musical key
    :param bridge_list: list of all possible bridges
    :return: none
    """
    if n == 1:
        print(n, "practice problem: \n")
    else:
        print(n, "practice problems: \n")
    for i in range(n):
        print_rand_progression(progs_list, keys_list)
        print("Bridge: " + get_rand_bridge(bridge_list))
        print()


def print_all_practice_problems(progs_list, keys_list, bridge_list):
    """
    print every possible combination of progressions and keys and all the bridges (~ 2500 lines)
    :param progs_list: list of all possible progressions
    :param keys_list: list of all musical keys
    :param bridge_list: list of all possible bridges
    :return: none
    """
    print("Every practice problem:")
    for prog in progs_list:
        for key in keys_list:
            print()
            print(prog, "in", key)

    for bridge in bridge_list:
        print(bridge)


# Run Script

alls = ["all", "a", "yes"]  # possible commands to give all progressions
quits = ["quit", "q", "done", "exit", "leave"]  # possible commands to quit the program
progs = read_file("progressions.txt")
bridges = read_file("bridges.txt")
keys = get_keys()

print("Jury Simulator, Give a number or \"all\" for every combination")
n = input("How many progressions do you want? ")

# Run Loop
while n not in quits:  # While the user doesn't exit the program
    if n in alls:  # print all
        print_all_practice_problems(progs, keys, bridges)
    elif n.isdigit():  # print n
        print_n_practice_problems(int(n), progs, keys, bridges)
    else:
        print("that's not valid input")
    print("\n Type exit to exit")
    n = input("How many progressions do you want? ")

print("Done!")
