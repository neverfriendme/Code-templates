# by:neverfriendme
running = True
def predictor():
    try:
        print("Age teller")
        year = int(input("I will predict your age. Give me your year of birth and I will predict two outcomes\n:"))
        year_now = int(input("Now tell me the current year so I can give the right outcome\n:"))
        print(f"You are either {year_now - year} or if you have a late birthday you may be {year_now - year - 1}. Am I correct?")
    except ValueError:
        print("Not a number please try again.")

while running:
    predictor()