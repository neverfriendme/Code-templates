from random import randrange
player = input("You will get a random addition question between 0 and 2000.Input start to answer!:\n").strip().lower()
if player != "start":
    quit()
if player == "start":
    while True:
        num1generator = randrange(0,2000)
        num2generator = randrange(0,2000)
        question = int(input(f"What is {num1generator} + {num2generator}?\n"))
        if question == num1generator + num2generator:
            print("Correct!")
        else:
            print("Wrong!")
