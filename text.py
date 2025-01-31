Cable = "Looks like your cable got damaged, have you tried another cable or tested the cable on another product? (Yes / No)"
Port = "If the Cable is not the Problem, then it may be the Port, but for that I would like to send you to one of our Technicians. Would you Like that? (Yes/No)"


def mainline(textInput, inputName):
    print("")
    

def Auswertung(textInput, inputName):
    global name
    text = textInput
    name = inputName
    Theme = TopicMatching(text)
    if Theme == "charging":
        answer = Answering("Cable")
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
        cableInput = input("Looks like your cable got damaged, have you tried another cable or tested the cable on another product? (Yes / No)")
        cableInput = cableInput.lower()
        while True:
            if "yes" in cableInput:
                cableInput = input("If the Cable is not the Problem, then it may be the Port, but for that I would like to send you to one of our Technicians. Would you Like that? (Yes/No)")
                cableInput = cableInput.lower()
                if "yes" in cableInput:
                    return "A technician will be with you soon"
            elif "no" in cableInput:
                cableInput = input("Would you like to Test? (Yes / No)")
                cableInput = cableInput.lower()
                if cableInput == "No":
                    return "A technician will be with you soon"
                elif cableInput == "Yes":
                    cableInput = input("Does the Cable have a problem? (Yes / No)")
                    cableInput = cableInput.lower()
                    if cableInput == "no":
                        cableInput = input("If the Cable is not the Problem, then it may be the Port, but for that I would like to send you to one of our Technicians. Would you Like that? (Yes/No)")
                        cableInput = cableInput.lower()
                        if "yes" in cableInput:
                            return "A technician will be with you soon"
                    elif cableInput == "yes":
                        print("mach weiter hier")
    elif inputCheck == "part":
        while True:
            partInput = input("Which part needs to be replaced? please enter the partnumber")
            partInput = partInput.lower()
            if partInput.isdigit():
                print(f"do you want to order the part with the part number: {partInput}?")
                partInput = input("Yes / No")
                partInput = partInput.lower()
                if partInput == "yes":
                    print("You will reveice your Order Notice shortly, instructions on how to replace the part can be found in the scope of delivery")
                    break
                elif partInput == "no":  
                    print("Then get creative and print your own stuff.")   
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
    for Begriff, synonyms in synonyms.items():
        if any(synonym in text for synonym in synonyms):
            return Begriff
    return "Other"


def ProblemMatching(themeInput):
    Theme = themeInput
    if Theme == "load":
        while True:
            userInput = input("Is it a Hardware or Software problem? (Hardware / Software)")
            userInput = userInput.lower()
            if userInput == "hardware":
                return("hardware")
            elif userInput == "software":
                return("software")
            else:
                print("Please answer with Hardware or Software")
                

        

    

