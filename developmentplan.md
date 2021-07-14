# **Development Plan - Python Terminal Application**

For my application I have chosen to create a text-based adventure game named "Escape From the Depths". The application will provide users with multiple choices and the user will have to navigate to the end of the story, ending up as a win or a loss depending on the users choices. It will give users an entertaining and fun interaction with Python and further showcases the  limitless things you can do with pythons tools. The main problem it will solve is curing boredome for any user that plays it, the simplicity and non-complicated aspects allows it to be played by any audience. Although, because games are normally played by a younger generation, this is the demographic it will target to mostly. It gives the intended audience a relaxed and entertaining break from the stresses of real life and gives them a fun experience. 

## **List of features:**

### 1. _**A while loop for input validation:**_  
At the very start of the application I decided to create a while loop that keeps asking the player if they want to start the game until they type Y or y. I made this feature because I believe it is a suitable input feature for the start of any game.

**User interaction and Experience:**
The user will find out how to use this feature because it gives clear instructions on what to do, type Y. The user just has to type Y or y into the terminal and the game will start. I made it accept the lower case "y" aswell because I didn't want it to be too picky. I added a try and except block to handle errors. Because it is a while loop it keeps looping until the user types Y so the only real error I had to take into consideration was a KeyboardInterrupt so that's what I added into the except block so it fails gracefully.


