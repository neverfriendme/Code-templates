# by neverfriendme
choice = input("Minutes to hours or Hours to minutes?\nMinutes\nHours\nSeconds\n")
if choice == "Minutes":
    hour = 60
    min = float(input("Minutes(Enter a float): "))
    print(min/hour)
elif choice == "Hours":
    min = 60
    hours = float(input("Hours(Enter a float): "))
    print(hours * min)
elif choice == "Seconds":
    min = 0.60
    sec = float(input("Seconds(Enter a float):"))
    print(min/sec)
    