"""
Main Script für den Chatbot

"""

import text

bots = {"Bot 1": "Gardenbeetle", "Bot 2": "Cleanbug", "Bot 3": "Windowfly"}

class main:
    bot = bot("Debuggy")

    print(bot.Startup())
    

class bot:
    def __init__(self, name):
        #Bot Variablen erstellen
        self.name = name
            
    def Startup(self):
        return(f"Hello my name is {self.name}.\nWhat kind of bot do you have problem with\n")
    
    def Response(self, userInput):
        print("Work in progress")
        


