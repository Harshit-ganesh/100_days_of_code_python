from art import *
from game_data import data
import random
from clear import clear

flag = True
s = 0
h = 0


def high_low(z, data, t):
    if t % 2 == 0:
        A = {"A"}
    else:
        A = {"B"}
    a = data[z]["name"]
    b = data[z]["description"]
    c = data[z]["country"]
    d = data[z]["follower_count"]
    print(f"Compare {A}: {a}, {b}, from {c}")
    return d, t + 1


def correct(choice, result1, result2):
    if result1 > result2 and choice == "A":
        return 1
    if result2 > result1 and choice == "B":
        return 1
    else:
        return 2


while flag:
    clear()
    print(logo)
    t = 0
    if s == 0:
        z = random.randint(0, len(data) - 2)
        w = z + 1
    elif s == 1:
        z = w
        w = random.randint(0, len(data))
        h += 1
        print(f"You're right! Current score: {h}.")
    else:
        print(f"Sorry, that's wrong. Final score: {h}")
        break

    result1 = high_low(z, data, t)
    print(result1)

    print(vs)

    result2 = high_low(w, data, result1[1])
    print(result2)

    choice = input("Who has more followers? Type 'A' or 'B':")
    s = correct(choice, result1[0], result2[0])
