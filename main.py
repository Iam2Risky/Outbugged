"""
Main Script für den Chatbot
"""

import text

bots = {"Bot 1": "Gardenbeetle", "Bot 2": "Cleanbug", "Bot 3": "Windowfly"}

class Bot:
    def __init__(self, name):
        #Bot Variablen erstellen
        self.name = name
            
    def Startup(self):
        userInput = input(f"Hello my name is {self.name}.\nWhat kind of bot do you have problem with?\n1. Gardenbettle\n2. Cleanbug\n3. Windowfly\n4. Overall question\n")
        global name
        if userInput == "1":
            name = "Gardenbeetle"
        elif userInput == "2":
            name = "Cleanbug"
        elif userInput == "3":
            name = "Windowfly"
        elif userInput == "4":
            name = "other"
        else:
            return("Please describe your problem")
        

class Main:
    def __init__(self):
        # Bot-Instanz erstellen
        self.Bot = Bot("Debuggy")

    def run(self):
        self.Bot.Startup()
        run = text.mainline(name)
        return run

if __name__ == "__main__":
    app = Main()
    while True:
        fortnite = app.run()
        if fortnite == "break":
            break

        