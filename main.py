"""
Main Script für den Chatbot
"""
name = ""

import text

bots = {"Bot 1": "Gardenbeetle", "Bot 2": "Cleanbug", "Bot 3": "Windowfly"}

class Bot:
    def __init__(self, name):
        #Bot Variablen erstellen
        self.name = name
            
    def Startup(self):
        userInput = input(f"Hello my name is {self.name}.\nWhat kind of bot do you have problem with?\n1. Gardenbettle\n2. Cleanbug\n3. Windowfly\n4. Overall question")
        if userInput == "1":
            name = "Gardenbeetle"
        elif userInput == "2":
            name = "Cleanbug"
        elif userInput == "3":
            name = "Windowfly"
        else:
            return("Please describe your problem")
        return(f"You have a problem with {name}, please describe your problem")
        

class Main:
    def __init__(self):
        # Bot-Instanz erstellen
        self.Bot = Bot("Debuggy")

    def run(self):
        print(self.Bot.Startup())
        while True:
            userInput = input("")
            print(text.Auswertung(userInput, name))

if __name__ == "__main__":
    app = Main()
    app.run()