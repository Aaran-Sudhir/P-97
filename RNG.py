import random
number = random.randint(1,10)
tries = 0
while tries > -1:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < number:
        tries += 1
        print("You guess was too low")
    elif guess > number:
        tries += 1
        print("You guess was too high")
    if guess == number:
        tries += 1
        print("CONGRATS YOU GOT THE NUMBER IN ", tries," TRIES")
