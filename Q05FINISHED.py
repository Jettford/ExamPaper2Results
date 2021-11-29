#      Q05

def displayMenu():
     # Completed subprogram that displays the menu
    
    print("                  Menu                    ")
    print("------------------------------------------")
    print("[1] Add player name")
    print("[2] Play guess the capital city")
    print("[3] End game")
    print("------------------------------------------")

def getMenuChoice():
    # Completed subprogram that gets and validates the menu choice
    choices = [1,2,3]
    mChoice = 0
    
    # Menu choice is validated
    while mChoice not in choices:
        mChoice = int(input("Input your menu choice: "))

    # Valid menu option returned to the main menu
    return mChoice
     
def addPlayerName():
    # Add your code to:
    #   ensure a player name is input
    #   return the player name to the main menu

    tempPlayerName = input("What is your players name?: ")
    if len(tempPlayerName) == 0:
        print("You must input a name, try again.")
        return addPlayerName() # this is fine...
    else:
        return tempPlayerName



def guessCapital():
    # Partially completed subprogram to:
    #   display questions
    #   check guesses
    #   return final score
    
    # Arrays holding question numbers, countries and their capital cities
    questions = [1,2,3,4,5,6,7,8,9]
    countries = ["England","France","Spain","Italy","Germany","Scotland","Wales","United Arab Emirates","China"]
    capitals = ["London","Paris","Madrid","Rome","Berlin","Edinburgh","Cardiff","Abu Dhabi","Beijing"]

    questionCount = 1
    questionScore = 0

    # Add your code here

    questionsDone = []
    questionActive = 0
    
    for x in range(5):
        while True:
            question = input(f"Please input what question you would like to attempt: ({questions[0]} - {questions[len(questions) - 1]}): ")
            try:
                if not int(question) in questions:
                    print(f"Please select a valid question from {questions[0]} to {questions[len(questions) - 1]}")
                else:
                    if int(question) in questionsDone:
                        listOfComplete = "(not "
                        for y in questionsDone:
                            listOfComplete += str(y)
                            if not y is questionsDone[len(questionsDone) - 1]:
                                listOfComplete += ", "
                        listOfComplete += ")"
                        print(f"Please select a question not already completed {listOfComplete}")
                        continue
                    questionActive = int(question) - 1
                    break
            except ValueError:
                print(f"Please select a valid question from {questions[0]} to {questions[len(questions) - 1]}")
        
        # current question is stored in questionActive
        
        questionsDone.append(questionActive) # don't let them do this again
        questionCount += 1
        
        currentCountry = countries[questionActive]
        currentCapital = capitals[questionActive]
        
        answer = input(f"What is the capital of {currentCountry}?: ")
        if answer.lower() == currentCapital.lower():
            print(f"Correct, the answer was {currentCapital}, that is one more point on the board.")
            questionScore += 1
        else:
            print(f"Incorrect, the answer was {currentCapital}, sadly no points for this question")
            
    print(f"Congratulations, you scored {questionScore}/5 on these questions.") 

    return questionScore

menuChoice = 0
score = 0
playerName = ""

while menuChoice != 3:
    displayMenu()
    menuChoice = getMenuChoice()
    
    # Add your code to:
    #   call the relevant subprogram if the menu choice is 1 or 2
    #   display the player name and the score if the menu choice is 3

    if menuChoice == 1:
        playerName = addPlayerName()
    elif menuChoice == 2:
        score += guessCapital()
    elif menuChoice == 3:
        break
    else:
        print("Your choice must be listed above, try again")

    
# Game is ending
if playerName == "": # No player was ever made so just exit I think
    exit(0)
else:
    print(f"Well done {playerName}, your score was {score}")