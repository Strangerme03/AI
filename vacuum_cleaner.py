#---Imports---
from random import randint, choice
from time import sleep

#----------------------------GLOBAL VARIABLES-----------------------------------
env_dirty_state = {0: False, 1: False}  # initial setup for dictionary
vaccum_location = 0

#-------------------***-----FUNCTIONS-----****----------------------------------

def set_vaccum_loc():
    global vaccum_location
    vaccum_location = randint(0, 1)

def rand_state_generation():
    global env_dirty_state
    state = [True, False]
    env_dirty_state[0] = choice(state)
    env_dirty_state[1] = choice(state)

def clean_rooms(room):
    if room == 0:
        print("Room A is DIRTY. Cleaning it up....")
        sleep(3)
        env_dirty_state[room] = False
        print("Room A cleaned.\nMoving...")
        sleep(3)
    elif room == 1:
        print("Room B is DIRTY. Cleaning it up....")
        sleep(3)
        env_dirty_state[room] = False
        print("Room B cleaned.\nMoving...")
        sleep(3)

#----------------------AGENTS---------------------------------------------------------------

def simple_reflex_agent():
    global env_dirty_state, vaccum_location
    name_of_room = {0: 'A', 1: 'B'}
    iter_count = 0
    set_vaccum_loc()
    rand_state_generation()
    cleaned_room = 0
    sleep(2)
    while True:
        if iter_count > 10 and cleaned_room == 2:
            print("Both rooms cleaned.")
            break
        iter_count += 1
        if cleaned_room == 2:
            cleaned_room = 0
            print("Both Room's Clean.")
            print("Robot Going to SLEEP.")
            sleep(5)
            print("---Waking Up----\n")
            set_vaccum_loc()
            rand_state_generation()
        if cleaned_room == 0:
            print(f"----Room Stats:---------")
            print(f"Vaccum in Room {name_of_room[vaccum_location]}.\n")
            print(f"Dirty State: \nA: {env_dirty_state[0]}, B: {env_dirty_state[1]}\n\n")
            sleep(2)
        if vaccum_location == 0:
            if env_dirty_state[vaccum_location]:
                clean_rooms(vaccum_location)
            else:
                if cleaned_room != 2:
                    print("Room A is clean. Moving to Room B...")
                    vaccum_location = 1
                    cleaned_room += 1
        elif vaccum_location == 1:
            if env_dirty_state[vaccum_location]:
                clean_rooms(vaccum_location)
            else:
                if cleaned_room != 2:
                    print("Room B is clean. Moving to Room A...")
                    vaccum_location = 0
                    cleaned_room += 1

#--------Creating a function like main----------
def main():
    print("\t-------Vaccum Cleaner AI Program--------\n\n")
    simple_reflex_agent()

# Run only if this program is executed directly
if __name__ == "__main__":
    main()
