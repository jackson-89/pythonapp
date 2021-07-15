import time
import sys


def player_loss():
    try:
        print("YOU HAVE LOST!")
        start_game = input("If you wish to play again, press Y to restart: ")
        while start_game != "Y" and start_game != "y":
            print("Please enter Y if you wish to restart!")
            start_game = input("Do you dare try again? Enter Y: ")
        if start_game == "Y" or "y":
            intro()
    except KeyboardInterrupt:
        print("Goodbye...For now")

def intro():
    print("A large knock throws you from your slumber")
    time.sleep(3)
    print("\a(BANG!)\nYou jolt awake and scan around the dark room you lay in")
    time.sleep(3)
    print("The dark prison room bears nothing but a mouldy bed, a sad little bench and a --- you notice something off")
    time.sleep(3)
    print("The doors for the room has been left open! The large knock was the sound of it loosley slamming")
    time.sleep(3)
    print("This is the moment you have been waiting for, you will not get another oppurtunity like this to escape! ")
    time.sleep(3)
    print("You sneak through the gate and make your way up to the hallway where you are met with three different paths")
    time.sleep(3)
    print("")
    first_choice()

def first_choice():
    list_of_paths = ["a","b","c"]
    user_choice = ""
    while user_choice not in list_of_paths:
        print(''' Here are the different paths you can take:
        a) Towards the wardens room
        b) Towards the prison cafeteria
        c) Towards the guard bunkers\n''')
        
        user_choice = input("Enter your option (a/b/c): ")
        print(f"You have chosen {user_choice}")
        
        if user_choice == list_of_paths[0]:
            warden_path()
        elif user_choice == list_of_paths[1]:
            cafeteria_path()
        elif user_choice == list_of_paths[2]:
            guard_path()

def warden_path():
    print("You make your way anxiously to the bowels of the prison, towards the behemoth himself...")
    time.sleep(3)
    print("You slither through the darkness, avoiding all light sources that attempt to alert your presence")
    time.sleep(3)
    print("You stop at a big wooden door that is notorious for being the wardens bunker and you enter...")
    time.sleep(3)
    print("You open the door to a half-asleep warden clutching a shotgun pointed straight towards you!")
    time.sleep(3)
    warden = '\'How did you get out of your cell! Darn prison rat! Ill show you!\n\''
    for char in warden:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print("(\aBANG!)\n The warden fires the shotgun straight at you, knocking you to the ground")
    time.sleep(2)
    warden2 = "'Should've stayed in your cell...'\n"
    for char in warden2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    player_loss()
    

def cafeteria_path():
    print("cafeteria")

def guard_path():
    print("guard")

def start():
    try:
        print("Welcome to 'Escape the Depths', a text-based survival game made with Python")
        print("In this game you will be tasked to escape a dark prison and fight for your freedom")
        start_game = input("Do you dare to play? Press Y to start: ")
        while start_game != "Y" and start_game != "y":
            print("Please enter Y if you want to continue!")
            start_game = input("Do you dare to continue? Enter Y: ")
        if start_game == "Y" or "y":
            intro()
    except KeyboardInterrupt:
        print("Goodbye...For now")

start()        




    
    

