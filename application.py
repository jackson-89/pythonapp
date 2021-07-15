import time
import sys

a = 3
b = 0.2
c = 0.08

def intro():
    print("A large knock throws you from your slumber")
    time.sleep(a)
    print('\a')
    print("You jolt awake and scan around the dark room you lay in")
    time.sleep(a)
    print("The dark prison room bears nothing but a mouldy bed, a sad little bench and a --- you notice something off")
    time.sleep(a)
    print("The doors for the room has been left open! The large knock was the sound of it loosley slamming")
    time.sleep(a)
    print("This is the moment you have been waiting for, you will not get another oppurtunity like this to escape! ")
    time.sleep(a)
    print("You sneak through the gate and make your way up to the hallway where you are met with three different paths")
    time.sleep(a)
    print("")
    first_choice()

def first_choice():
    list_of_paths = ["a","b","c"]
    user_choice = ""
    while user_choice not in list_of_paths:
        print(''' Here are the different paths you can take:
        a) Towards the wardens room
        b) Towards the prison cafeteria
        c) Towards the guard bunkers''')
        
        user_choice = input("Enter your option: ")
        
        if user_choice == list_of_paths[0]:
            warden_path()
        elif user_choice == list_of_paths[1]:
            cafeteria_path()
        elif user_choice == list_of_paths[2]:
            guard_path()

def warden_path():
    print("warden")

def cafeteria_path():
    print("cafeteria")

def guard_path():
    print("guard")


print("Welcome to 'Escape the Depths', a text-based survival game made with Python")
print("In this game you will be tasked to escape a dark prison and fight for your freedom")

try:
    start_game = input("Do you dare to play? Press Y to start: ")
    while start_game != "Y" and start_game != "y":
        print("Please enter Y if you want to continue!")
        start_game = input("Do you dare to continue? (Y/N): ")
except KeyboardInterrupt:
    print("Goodbye...For now")
    
intro()



    
    

