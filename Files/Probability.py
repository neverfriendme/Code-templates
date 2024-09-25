from random import randrange
import time
# by neverfriendme
def probability():
    try:
        Range = int(input("Range = 0 , enter a number:\n"))
        if 1 == 1:
            while True:
                generate = randrange(0,Range)
                time.sleep(1)
                print(generate)
    except ValueError:
        print("Invalid Value")
        return ValueError
probability()
