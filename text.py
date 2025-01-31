Cable = "Looks like your cable got damaged, have you tried another cable or tested the cable on another product? (Yes / No)"
Port = "If the Cable is not the Problem, then it may be the Port, but for that I would like to send you to one of our Technicians. Would you Like that? (Yes/No)"

def Auswertung(textInput):
    text = textInput
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
            return "Leider hat das Programm aktuell Wartungsarbeiten, weshalb sie nicht darauf zugreifen können"
    elif Theme == "update":
        return "Die neue softwareversion finden sie auf Bugland.de/Software/. Sie können auch in dem Programm in die Einstellungen und dann unter Update & Sicherheit, den automatisches update knopf drücken. "
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
                    return "Ein Techniker wird sich bald um sie kümmern"
            elif "no" in cableInput:
                cableInput = input("Would you like to Test? (Yes / No)")
                cableInput = cableInput.lower()
                if cableInput == "No":
                    return "Ein Techniker wird sich bald um sie kümmern"
                elif cableInput == "Yes":
                    cableInput = input("Does the Cable have a problem? (Yes / No)")
                    cableInput = cableInput.lower()
                    if cableInput == "no":
                        cableInput = input("If the Cable is not the Problem, then it may be the Port, but for that I would like to send you to one of our Technicians. Would you Like that? (Yes/No)")
                        cableInput = cableInput.lower()
                        if "yes" in cableInput:
                            return "Ein Techniker wird sich bald um sie kümmern"
                    elif cableInput == "yes":
                        print("mach weiter hier")
    elif inputCheck == "part":
        partInput = input("Was für ein Teil muss ersetzt werden? Bitte nenne uns die teil nummer")


                            


        

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
                

        

    

