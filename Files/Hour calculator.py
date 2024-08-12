# by neverfriendme
choice = input("Minutes to hours or Hours to minutes?\nMinutes\nHours\n")
if choice == "Minutes":
    hour = 60
    min = int(input("Minutes: "))
    print(min/hour)
elif choice == "Hours":
    min = 60
    hours = int(input("Hours: "))
    print(hours * min)