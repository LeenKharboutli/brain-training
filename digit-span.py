from random import randint
from time import sleep

level = -1
while level not in list(range(2,10)):
    level = int(input("set level, 2 - 9"))


def create_random_sequence(level):
    sequence = []
    for i in range(level):
        sequence.append(randint(2,10))

    return sequence


tests = {

    "test1" : create_random_sequence(level),
    "test2" : create_random_sequence(level),
    "test3" : create_random_sequence(level),
    "test4" : create_random_sequence(level),
    "test5" : create_random_sequence(level)
}


for test, sequence in tests.items():
    print(test)
    for item in sequence:
        sleep(0.25)
        print(item)
