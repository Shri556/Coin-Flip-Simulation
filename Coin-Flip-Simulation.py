from random import choice
from time import sleep


def inpt():
    while True:
        x = input("Toss the next one(Y/N): ")
        if x.lower() in ('y','n'):
            break
        else:
            sleep(0.2)
            print("Enter a Valid input")
    return x

def flip():
    option = ['HEADS','TAILS']

    result = choice(option)
    return result


if __name__ == '__main__':
    b = flip()

    print("FLIPING")
    sleep(2)
    print(b)

    while True:
        a = inpt()
        if a.lower() == 'y':
            b = flip()
            print(b)
        if a.lower() == 'n':
            print("EXITING")
            sleep(3)
            break
