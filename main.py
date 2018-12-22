import random
import time

time_of_birth = time.time()

def age():
    return time.time() - time_of_birth

alive = True

# max allowed value for main stats
max_stat = 10

# initial stats
fullness = random.randint(1,10) 
health = random.randint(1,10) 
happiness = random.randint(1,10) 

# prints character stats
def print_stats():
    print(f'____________________\nName: {name}\nAge: {age()}\nHunger: {round(max_stat - fullness)}\nHealth: {round(health)}\nHappiness: {round(happiness)}\n____________________')

# determines whether character is dead and acts accordingly
def am_i_dead():
    if (fullness < 0) or (health < 0) or (happiness < 0): # if dead
        print(f'\nRIP {name}\n')
        return False
    else: # if alive
        return True

# asks user to name character
name = input('Hi! I\'m new. Please name me... ')

print_stats()

# loop until character is dead
while alive:

    command = input('Press (f) to feed, (e) to exercise, (p) to play, or (x) to exit ')

    if command == 'x':
        print('\nBye!\n')
        break
    elif command == 'f':
        if fullness < max_stat: fullness += 1
        if happiness < max_stat: happiness += random.randint(0,3)/10
    elif command == 'e':
        if health < max_stat: health += 1
        if happiness < max_stat: happiness += random.randint(0,20)/100 
        fullness -= random.randint(0,50)/100 
    elif command == 'p':
        if happiness < max_stat: happiness += 1
        fullness -= random.randint(0,25)/100
    else: # if invalid key pressed, decrease happiness
        happiness -= random.randint(0,5)
        
    print_stats()

    # returns false if dead, exiting the loop
    alive = am_i_dead()
