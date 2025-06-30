import time
print("Interest calculator")
try:
    Money = float(input('Amount of borrowed money:\n'))
    # How much did they borrow
    Interest_rate = float(input("Interest rate (e.g. 9.45 for 9.45%):\n")) / 100
    # To get the percentage
    Days_long = int(input("How many days:\n"))
    # How long did they keep it
    Interest = Money * Interest_rate * Days_long / 365
    # The simple formula. We multiply money by the interest rate so we get the extra money we owe. Then we multiply by how many days long divided by 365 days so we get the time period.
    print("Loading calculation...")
    time.sleep(3)
    # Just something cool
    if Interest < 1.00:
        print(f"{Interest:.2f} cents")
    elif Interest > 1.00:
        print(f"{Interest:.2f} dollars")
    # Rounds the numbers. Makes it look polished.
except ValueError:
    print("You entered a string instead of a number!")
