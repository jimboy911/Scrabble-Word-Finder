#Scrabble Word Finder Challenge
#from - http://wiki.openhatch.org/Scrabble_challenge
#current state should be run from the command line with one argument

#Step 1: open and read the sowpods.txt file
#create a function to open the file and store all the data in a list

def openFile():
    """This is a function to open the sowpods file and store all the lines as individual list entries.
    this function also strips the carriage return from each entry in the list
    to prepare it for the word check functions."""
    
    with open("sowpods.txt", "r") as files: #opens the sowpods list, as "files"; should automatically close it, too
        sowpodsList = files.readlines() #takes files and reads every line, storing in a list
        sowpodsList3 = []   #prepares a list to place or "append" the words into

    for i in sowpodsList: #iterates through each word in the list
        sowpodsList2 = i.strip() #strips the carriage return
        sowpodsList3.append(sowpodsList2)   #after it strips the carraige return, it stores each result into a new list
        
    return sowpodsList3 #returns the completed list, imported from the text file with carriage returns removed

############################

#step 2: Get the rack
#Scrabble racks have 7 letters

def getRack():
    """this version prompts the user for input for the letters, for quick code testing purposes"""
    rack = input("Please enter your scrabble rack (7 letters): ")   #prompts user for input and stores input in "rack"
    if len(rack) != 7:  #quick check to see if the user actually entered in 7 letters
        print("Please enter exactly 7 letters.")    #informs the user that they didn't enter in 7 letters for the rack
        exit()  #then exits the program. user will have to restart the process again
    rack = rack.upper() #converts all characters to uppercase
    print("You've entered: ", rack) #feedback to user
    return list(rack)   #returns the rack as a list for further processing

def getRack2():
    """this is actually the way the scrabble challenge instructs to do - to be run from the command line"""
    import sys #read arguments from the command line
    rack = sys.argv[1] #returns list of arguments run from the command line, the [1] stands for the it taking 1 argument
    rack = rack.upper() #converts the characters in rack to all uppercase
    #by default the first argument is the path to the program
    #then adding a space and putting an argument after that will create 2nd argument
    #but only if you run from the command line
    if len(rack) != 7:  #again, checks for 7 letters in the argument
        print("Please enter exactly 7 letters.") #feedback to user
        sys.exit() #exits the program
    else:   #else statement here for formality and completeness
        pass
    return rack #maybe it wasn't necessary to convert the rack to a list. this was working fine in testing

######################

#step 3: find valid words
#go through every word in sowpodsList3
#check to see if the letters in rack match letters in the word
#if the letters match, add the word to validWords list

def count_letters(word):
    """This is a function to count the number of letters in each word and return it as a dictionary"""
    letterCount = {} #defining a dictionary to add letters into and store their counts
    for eachLetter in word: #goes through each letter in the word
        if eachLetter in letterCount: #checks for existence of letter in dictionary
            letterCount[eachLetter] += 1 #if it's already in the dictionary, it increases by 1
        else:
            letterCount[eachLetter] = 1 #if it's not in the dictionary yet, it adds an entry
    return letterCount #returns the dictionary of letters and their counts

def wordCheck(eachWord, rack):
    """This function is used in conjunction with count_letters() to place the rack
    and the word that's currently being evaluated. Then compare their dictionary's letter counts"""
    word_count = count_letters(eachWord) #sampled from openFile
    rack_count = count_letters(rack) #sampled from getRack
    trues = 0   #defining an integer used for counting later in the function

    for eachEntry in word_count:    #goes through each dictionary key in the word being examined
        if eachEntry in rack_count: #checks if the key (which is the letter being examined) is in both dictionaries
            if word_count[eachEntry] <= rack_count[eachEntry]: 
                #checks if the examined word's key's/letter's count is <= to the same key in the rack
                trues += 1 #if it is, it counts up by one for trues variable
        if trues == len(word_count): #and if the number of trues matches the number of letters in the word being examined
            return eachWord #then it returns the word being examined.
        #there is an implied else here statement, which returns a None value when the if statement directly above isn't true

#######################
        
def main():
    """This is where all the functions get put together"""
    wordList = openFile()   #opens the text file of words and stores it in wordList
    rack = getRack2()       #either prompts for user input for the rack in getRack() or takes command prompt arguments in getRack2()
    validWords = []         #sets up a list for valid words to be used in scoring later

    for eachWord in wordList:   #goes through each word imported into the word list
        validWords.append(wordCheck(eachWord, rack))    #adds each word that passes the wordCheck function into the list

    validWords = filter(None, validWords)   #filters out the None values in the list that were returned from the wordCheck function
    validWords = list(validWords) #converts validWords back to a list because using filter turned it into a generator

    scoring(validWords) #scores all the validWords

#############

def scoring(validWords): #takes all the validWords generated in main() to calculate their scores
    """print the score first followed by the word, one entry per line
    the example in the challenge has it ordered from highest scoring word to lowest scoring"""

    results = [] #prepares a list to put results into
    
    #directly below is a dictionary listing the letters and their corresponding scrabble score
    scores = {"A": 1, "C": 3, "B": 3, "E": 1, "D": 2, "G": 2,
         "F": 4, "I": 1, "H": 4, "K": 5, "J": 8, "M": 3,
         "L": 1, "O": 1, "N": 1, "Q": 10, "P": 3, "S": 1,
         "R": 1, "U": 1, "T": 1, "W": 4, "V": 4, "Y": 4,
         "X": 8, "Z": 10}

    #for each letter in the test word
    #match each letter with each key in the dictionary in scores
    #once the dictionary returns the value of the key, which will be an integer
    #add it to the score of the word
    #then print the score of the word followed by the word
    for eachWord in validWords: #goes through all the words in the validWords list
        wordScore = 0   #resets the wordScore to 0 for each word the function goes through
        for eachLetter in eachWord: #goes through each letter in each word examined
            wordScore += scores[eachLetter] #searches for each letter in the scores dictionary and returns/adds the value stored
        if wordScore < 10: #added code to make the list print out in the correct order
            wordScore = str(wordScore) #converts the score, which is an integer, to a string
            wordScore = "0" + wordScore #then puts both the score and the word together
        else: #if the score is higher than 10
            wordScore = str(wordScore) #converts the score, which is an integer, to a string
        results.append(wordScore + " " + eachWord) #adds each word looked at, and their score, to the results list
    results = sorted(results, reverse=True) #sorts through the list, highest score first
    for eachResult in results: #goes through each result in the results list
        print(eachResult) #prints out each result on its own line

##############

main() #calls main function, so the program starts up right away; especially for the command line version
