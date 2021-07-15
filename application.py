import time
import sys


def player_loss():
    try:
        print("\aYOU HAVE LOST!")
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
    time.sleep(2)
    print("The dark prison room bares nothing but a mouldy bed, a sad little bench and a --- you notice something off")
    time.sleep(4)
    print("The doors for the room has been left open! The large knock was the sound of it loosley slamming")
    time.sleep(4)
    print("This is the moment you have been waiting for, you will not get another oppurtunity like this to escape! ")
    time.sleep(4)
    print("You sneak through the gate and make your way up to the hallway where you are met with three different paths...")
    time.sleep(5)
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
    print("You make your way towards the place you have spent countless hours devouring vile portions of questionable foods")
    time.sleep(4)
    print("You enter the cafeteria entrance and you are welcomed with a horrid smell of rotten milk and raw meat")
    time.sleep(4)
    print("You wander inside carefully and you suddenly see another prisoner sitting down, eating a bowl of food!")
    time.sleep(4)
    print("He notices you and stands up immediately")
    time.sleep(3)
    prisoner = "'Stop! You don't have permission to be out of your cell! Guards help!'\n"
    for char in prisoner:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(2)
    print("The prisoner's shouting has alerted the guards and a pack of them ambush the cafeteria, tackling you to the ground")
    time.sleep(4)
    player_loss()

def guard_path():
    print("You stupidly creep down the corridor towards the most dangerous part of the prison, the guard bunkers")
    time.sleep(4)
    print("As you approach you hear the snoring and rustling of unconcious guards catching some shut eye, you are terrified")
    time.sleep(4)
    print("All of a sudden a guard emerges from one of the rooms and faces you in a concerned fasion")
    time.sleep(4)
    guard = "'You finally made it! I was hoping you would see the door I left open for you. Come on lets get you out of here\n'"
    for char in guard:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(2)
    print("Someone is looking out for you it seems! The guard smuggles you out of the prison and you make a run for it.... ")
    time.sleep(2)
    print("")
    time.sleep(2)
    print("")
    time.sleep(2)
    end_quote = "...and you don't look back.\n"
    for char in end_quote:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(2)
    print("ye")
    
    #player_win()

def start():
    try:
        print("Welcome to 'Escape the Depths', a text-based survival game made with Python")
        print("In this game you will be tasked to escape a dark prison and fight for your freedom")
        start_game = input("Do you dare to play? Press Y to start: ")
        while start_game != "Y" and start_game != "y":
            print("Please enter Y if you want to continue!")
            start_game = input("Do you wish to play? Enter Y: ")
        if start_game == "Y" or "y":
            intro()
    except KeyboardInterrupt:
        print("Goodbye...For now")

start()        




    
    

