word = ("Bread")
wordList = list(word.lower())
updatedSpaces = []
wordLen = len(word)
lives = 5
letter = " "

for i in range (0, int(wordLen)):
    updatedSpaces.append("_")  
def getLetter():
    global letter
    letter = raw_input ("What letter would you like to guess    ")
def check():
    global updatedSpaces
    global lives
    global letter
    for x in range(0, int(wordLen)):
        if letter == wordList[x]:
            updatedSpaces[x] = wordList[x]
            print(updatedSpaces)
            print("You have:   ", lives, "   lives remaining")
            checklist = "".join(updatedSpaces)
            master = "".join(wordList)
            if checklist == master:
                print("You figured out the word    ")
                #break
            else:
                getLetter()
        else:
            lives -= 1
            if lives != 0:
                print("You have:  " + str(lives) + "  lives remaining!")
                print(updatedSpaces)
                getLetter()
            else:
                print("Out of lives: Game Over   ")
                
def game():
    getLetter()
    check()
    
game()                      