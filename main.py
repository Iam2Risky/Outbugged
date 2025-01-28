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
        return(f"Hello my name is {self.name}.\nWhat kind of bot do you have problem with\n1. Gardenbettle\n2. Cleanbug\n 3. Windowfly")
    
    def Response(self, userInput):
        print("Work in progress")
    

class Main:
    def __init__(self):
        # Bot-Instanz erstellen
        self.Bot = Bot("Debuggy")

    def run(self):
        print(self.Bot.Startup())
        while True:
            userInput = input("")
            print(text.Auswertung(userInput))

if __name__ == "__main__":
    app = Main()
    app.run()