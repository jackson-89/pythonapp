

def intro():
    try:
        user_input = ""
        while user_input != "Y" or "y":
            user_input = input("Press Y to continue")
        if user_input == "Y" or "y":
            print("Congrats you made a blank resume")
            file = open("resume.txt", "x")  
    except:
        print("Please enter a valid response (Y/N")

intro()

        