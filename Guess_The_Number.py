import random


def guess_no(x):
    random_no = random.randint(1, x)
    guess_no = 0
    while guess_no != random_no:
        guess_no = int(input(f"Guess a number between 1 & {x}: "))
        if guess_no < random_no:
            print("Too low, guess again.")
        elif guess_no > random_no:
            print("Too high, guess again.")
    print("Yaaaay!, you guessed right.")


guess_no(10)
