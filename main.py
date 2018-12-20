import random

name = "Nameless"
age = 0

max_stat = 10
fullness = random.randint(1,10) 
health = random.randint(1,10) 
happiness = random.randint(1,10) 

running = True

def print_stats():
    print(f'____________________\nName: {name}\nAge: {age}\nHunger: {max_stat - fullness}\nHealth: {health}\nHappiness: {happiness}\n____________________')

print_stats()

while running:

    command = input('Press (f) to feed, (e) to exercise, or (p) to play ')

    if command == 'f':
        fullness += 1
        happiness += 0.25
    elif command == 'e':
        health += 1
        happiness += 0.1
        fullness -= 0.3
    elif command == 'p':
        happiness += 1
        fullness -= 0.25
    else: # if invalid key pressed, decrease happiness
        happiness -= 1
        
    print_stats()
