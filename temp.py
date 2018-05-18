def main():
    getKey = 
    list1, players = getScores()
    numbers = []
    highlow = list1.sorted()

def getScores():
    nameandScores = []
    total = 0
    nameandScore = "start"
    nameandScore = str(input("Enter the name and score of the next player: "))
    if nameandScore == "":     #Checks to see if the first entry is more than nothing
        input("You did not enter anything. Press enter to exit.")
        sys.exit()
    players = 0
    while nameandScore != "":
        try:            #This checks to see if values will work for future sorting
            int(nameandScore.split()[-1])
            total += int(nameandScore.split()[-1])
        except:
            print("Your name and score was not entered in the correct way.")
            input("Press enter to exit.")
            sys.exit()
        if int(nameandScore.split()[-1]) > 300 or int(nameandScore.split()[-1]) < 0:
            print("That score is not a possible bowling score.")
            input("Press enter to exit.")
            sys.exit()
        nameandScores.append(nameandScore)
        players += 1
        if players >= 2:    #I assume that at least two players will be entered
            print("If there are no more players press enter.")
        nameandScore = str(input("Enter the name and score of the next player: "))
    return nameandScores, players
main()
