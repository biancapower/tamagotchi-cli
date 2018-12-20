import random

name = "Nameless"
age = 0

max_stat = 10
fullness = random.randint(1,10) 
health = random.randint(1,10) 
happiness = random.randint(1,10) 

running = True

def print_stats():
    print(f'____________________\nName: {name}\nAge: {age}\nHunger: {round(max_stat - fullness)}\nHealth: {round(health)}\nHappiness: {round(happiness)}\n____________________')

def am_i_dead():
    if (fullness < 0) or (health < 0) or (happiness < 0):
        print(f'RIP {name}')

print_stats()

while running:

    command = input('Press (f) to feed, (e) to exercise, or (p) to play ')

    if command == 'f':
        fullness += 1
        happiness += random.randint(0,3)/10
    elif command == 'e':
        health += 1
        happiness += random.randint(0,20)/100 
        fullness -= random.randint(0,50)/100 
    elif command == 'p':
        happiness += 1
        fullness -= random.randint(0,25)/100
    else: # if invalid key pressed, decrease happiness
        happiness -= random.randint(0,5)
        
    print_stats()

    am_i_dead()
