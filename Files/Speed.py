# By neverfriendme
choices = ["kph","mph"]
choice = input("If you are measuring in kilometers input kph, if you are measuring miles input mph:\n").strip().lower()
if choice not in choices:
    print("Invalid measurement")
    quit()
elif choice == choices[0]:
    speed = float(input("Enter a speed(Enter a float):"))
    print(f"In seconds: {speed * 3600} KM/s")
    print(f"In minutes: {60/speed} KM/m")
    print(f"In hours: {speed} KM/h")
    print(f"Conversion to MI: {speed / 1.609344}")
elif choice == choices[1]:
    speed = float(input("Enter a speed(Enter a float):"))
    print(f"In seconds: {speed * 3600} MI/s")
    print(f"In minutes: {60/speed} MI/m")
    print(f"In hours: {speed} MPH")
    print(f"Conversion to KM: {speed * 1.609344}")
