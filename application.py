print("Welcome to 'Escape the Depths', a text-based survival game made with Python")
print("In this game you will be tasked to escape a dark prison and fight for your freedom")

try:
    start_game = input("Do you dare to play? Press Y to start: ")
    while start_game != "Y" and start_game != "y":
        print("Please enter Y if you want to continue!")
        start_game = input("Do you dare to continue? (Y/N): ")
except KeyboardInterrupt:
    print("Goodbye...For now")
    




    
    

