name = "Nameless"
age = 0

hunger = 5
health = 5
happiness = 5

running = True

print(f'____________________\nName: {name}\nAge: {age}\nHunger: {hunger}\nHealth: {health}\nHappiness: {happiness}\n____________________')

while running:

    command = input('Press (f) to feed, (e) to exercise, or (p) to play ')

    if command == 'f':
        hunger = hunger + 1
    elif command == 'e':
        health = health + 1
    elif command == 'p':
        happiness = happiness + 1
    else: # if invalid key pressed, decrease happiness
        happiness = happiness - 1
        

    print(f'____________________\nName: {name}\nAge: {age}\nHunger: {hunger}\nHealth: {health}\nHappiness: {happiness}\n____________________')
