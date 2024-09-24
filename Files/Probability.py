from random import randrange
import time
# by neverfriendme
def probability():
    try:
        Range = int(input("Range: 1 now enter your number:\n"))
        if 1 == 1:
            while True:
                generate = randrange(1,Range)
                time.sleep(1)
                print(generate)
    except ValueError:
        print("Invalid Value")
        return ValueError
probability()