import time
import random
Numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print("The multiplication test! 60 questions")
Duration = 0
correct = 0
wrong = 0
running = True
while running:
    time.sleep(1)
    Duration += 1
    print(Duration)

    First_num = random.choice(Numbers)
    second_num = random.choice(Numbers)

    answer = int(input("Answer please:"))
    if answer == First_num * second_num:
        correct += 1
    elif answer != First_num * second_num:
        wrong += 1

    print(f"{First_num} * {second_num}")
    if Duration == 60:
        running = False

        print(f"You got {correct} right and {wrong} wrong. Precentage: {correct / wrong}")
