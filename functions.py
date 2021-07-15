

def start():
    try:
        print("YOU HAVE LOST!")
        start_game = input("If you wish to play again, press Y to restart: ")
        while start_game != "Y" and start_game != "y":
            print("Please enter Y if you wish to restart!")
            start_game = input("Do you dare try again? Enter Y: ")
        if start_game == "Y" or "y":
            print("LOL")
    except KeyboardInterrupt:
        print("Goodbye...For now")





start()