import time
Cable = "Looks like your cable got damaged, have you tried another cable or tested the cable on another product? (Yes / No)"
Port = "If the Cable is not the Problem, then it may be the Port, but for that I would like to send you to one of our Technicians. Would you Like that? (Yes/No)"


def mainline(inputName):
    global name
    name = inputName
    zahler = 0
    if name == "other":
        OverallQuestions()
    else:
        print(f"You have a problem with {name}, please describe your problem")
        while True:
            if zahler == 0:
                textInput = input("")
                zahler += 1
                print(Auswertung(textInput))
            else:
                textInput = input("Is there another problem i can help you with? (Yes/No)\n").lower()
                if textInput == "no":
                    return "break"
                elif textInput == "yes":
                    return


def Auswertung(textInput):
    text = textInput
    Theme = TopicMatching(text)
    if Theme == "charging":
        answer = Answering("Cable")
        if answer == None:
            return "ok"
        else:
            return answer
    elif Theme == "load":
        softHard = ProblemMatching(Theme)
        if softHard == "hardware":
            answer = Answering("Cable")
            return answer
        elif softHard == "software":
            return "Unfortunately due to maintanance the software is currently not available. Please try again later."
    elif Theme == "update":
        return "You can find the new softwareversion on bugland.de/software. You can also turn on automatic updates in you Settings under Updates - Security"
    elif Theme == "break" or "replace":
        answer = Answering("part")
        return answer



def Answering(check):
    inputCheck = check
    if inputCheck == "Cable":
        cableInput = input("Looks like your cable got damaged, have you tried another cable or tested the cable on another product? (Yes / No)\n")
        cableInput = cableInput.lower()
        while True:
            if "yes" in cableInput:
                cableInput = input("If the Cable is not the Problem, then it may be the Port, but for that I would like to send you to one of our Technicians. Would you Like that? (Yes/No)\n")
                cableInput = cableInput.lower()
                if "yes" in cableInput:
                    return "A technician will be with you soon"
                elif cableInput == "no":
                    return
            elif "no" in cableInput:
                cableInput = input("Would you like to Test? (Yes / No)\n")
                cableInput = cableInput.lower()
                if cableInput == "No":
                    return "A technician will be with you soon"
                elif cableInput == "Yes":
                    cableInput = input("Does the Cable have a problem? (Yes / No)\n")
                    cableInput = cableInput.lower()
                    if cableInput == "no":
                        cableInput = input("If the Cable is not the Problem, then it may be the Port, but for that I would like to send you to one of our Technicians. Would you Like that? (Yes/No)\n")
                        cableInput = cableInput.lower()
                        if "yes" in cableInput:
                            return "A technician will be with you soon"
                    elif cableInput == "yes":
                        print("continue here")
    elif inputCheck == "part":
        while True:
            partInput = input("Which part needs to be replaced? please enter the partnumber\n")
            partInput = partInput.lower()
            if partInput.isdigit():
                print(f"do you want to order the part with the part number: {partInput}?")
                partInput = input("Yes / No\n")
                partInput = partInput.lower()
                if partInput == "yes":
                    print("You will reveice your Order Notice shortly, instructions on how to replace the part can be found in the scope of delivery")
                    break
                elif partInput == "no":  
                    print("Then get creative and print your own stuff.")
                    break
            else:
                print("please enter a valid part number")


                            


        

def TopicMatching(textInput):
    text = textInput
    synonyms = {
        "charging": ["charge", "charging", "recharging", "powering", "energizing", "juicing"],
        "load": ["load", "loading", "upload", "download", "carrying", "burden", "freight", "payload"],
        "break": ["break", "broken", "fracture", "rupture", "snap", "crack", "shatter", "split"],
        "update": ["update", "refresh", "upgrade", "revise", "renew", "modify", "patch", "enhance", "improve"],
        "replace": ["replace", "substitute", "exchange", "swap", "change", "switch", "supplant", "alternate", "displace"],
        "gardenbeetle": ["gardenbeetle", "beetle", "bug", "garden", "käfer", "gartenkäfer"],
        "cleanbug": ["cleanbug", "clean", "putzen", "reinigungsbot", "staubsauger", "staubsaugroboter"],
        "windowfly": ["windowfly", "window", "fenster", "fliege", "fensterputzroboter", "fenster"]
    }

    text = text.lower()
    while True:
        for Begriff, synonyms in synonyms.items():
            if any(synonym in text for synonym in synonyms):
                return Begriff
        text = input("Wir konnten ihre Anfrage nicht zuordnen bitte wählen sie eine dieser Kategorien: Charging\nload\nbreak\nupdate\nreplace\n")


def ProblemMatching(themeInput):
    Theme = themeInput
    if Theme == "load":
        while True:
            userInput = input("Is it a Hardware or Software problem? (Hardware / Software)\n")
            userInput = userInput.lower()
            if userInput == "hardware":
                return("hardware")
            elif userInput == "software":
                return("software")
            else:
                print("Please answer with Hardware or Software")

def OverallQuestions():
    while True:
        questionInput = input("Which topic do you want to have a conversation about:\n1. Pricing\n2. Delivery time\n3. Models\n4. warranty\n5. refunds\n").lower()
        if questionInput == "1":
            print("The Gardenbeetle is: 3 yacht monkey nft's\n"
                  "The Cleanbug is: 0,005₿\n"
                  "The Windowfly is: 1337.69₱\n")
            time.sleep(10)
            return
        elif questionInput == "2":
            print("The delivery time for all of our products and replacements is 3-5 working days delivered by DHL\n")
            time.sleep(10)
            return
        elif questionInput == "3":
            print("Our Models are the Gardenbeetle, which can easily be used in your garden to mow the lawn\n, the Cleanbug, which is a cleaning robot\nand the Windowfly, which is a window cleaning robot\n")
            time.sleep(10)
            return
        elif questionInput == "4":
            print("Don't think our products can be refunded! SIKE You keep your shit bro, we don't want it either haha RIP BOZO")
            time.sleep(10)
            return
        elif questionInput == "5":
            print("There are no refunds on all of our products, verklag uns doch!")
            time.sleep(10)
            return
        else:
            print("Please only enter the number of the topic you want to talk about")