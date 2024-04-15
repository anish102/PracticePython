import random

a = random.randint(1, 9)
count = 0
flag = True
while (1 < 2):
    usr = input("Guess the number, and to exit type 'exit':")
    if (usr == "exit"):
        print(f'Exiting after {count} wrong guesses.')
        break
    if (int(usr) == a):
        print(f'Exactly right after {count} wrong guesses.')
        break
    elif (int(usr) > a):
        print("Too high")
        count += 1
    elif (int(usr) < a):
        print("Too low")
        count += 1
