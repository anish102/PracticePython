def year100(name, age):
    curYear = 2024
    age100 = curYear + 100 - age
    print(f'{name}, you will turn 100 at {age100}')


name = input("Enter your name:")
age = int(input("Enter your age:"))
year100(name, age)
