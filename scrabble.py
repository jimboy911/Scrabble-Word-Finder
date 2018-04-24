#scrabble challenge

#step 1: open and read the sowpods word file
#SOWPODS = the word list used in English-language tournament Scrabble
#in most countries except the USA, thailand, and canada.

#download the SOWPODSS word file first
#copied to C:\Users\andmonte\Documents\Python\Scrabble folder\sowpods.txt
#upon opening it's a long list of scrabble words in all capital letters

#create a function to open the file and store all the data in a list

def openFile():
    files = open("sowpods.txt", "r") #opens the target file / using testlist for now
    sowpodsList = files.readlines() #takes files and reads every line, storing in a list
    sowpodsList3 = []

    for i in sowpodsList:
        sowpodsList2 = i.strip() #strips the carriage return
        sowpodsList3.append(sowpodsList2)
        
    return sowpodsList3

    #can also use a with method, which will automatically close the file

############################

#step 2: get the rack
#ask for some user input to insert some letters
#how many letters in a scrabble rack? = 7 letters

def getRack():
    rack = input("Please enter your scrabble rack (7 letters): ")
    if len(rack) != 7:
        print("Please enter exactly 7 letters.")
        exit()
    rack = rack.upper() #converts all characters to uppercase
    print("You've entered: ", rack)
    return list(rack)

#alternative way
import sys #read arguments from the command line
def getRack2():
    rack = sys.argv[1] #returns list of arguments run from the command line, takes 1 arg
    rack = rack.upper() #converts the characters in rack to all uppercase
    #by default the first argument is the path to the program
    #then adding a space and putting an argument after that will create 2nd argument
    #but only if you run from the command line
    if len(rack) != 7:
        print("Please enter exactly 7 letters.")
        sys.exit()
    else:
        pass
    return rack

######################

#step 3: find valid words
#go through every word in sowpodsList2
#check to see if the letters in rack match letters in the word
#if the letters match, add the word to validWords list

def count_letters(word):
    letterCount = {} #dictionary to add letters into and store their counts
    for eachLetter in word: #goes through each letter in the word
        if eachLetter in letterCount: #checks for existence of letter in dictionary
            letterCount[eachLetter] += 1 #if it's already in the dictionary, it increases by 1
        else:
            letterCount[eachLetter] = 1 #if it's not in the dictionary yet, it adds an entry
    return letterCount #returns the dictionary of letters and their counts

def wordCheck(eachWord, rack):
    word_count = count_letters(eachWord) #sampled from openFile
    rack_count = count_letters(rack) #sampled from getRack
    trues = 0
    #print(word_count) #prints out a dictionary
    #print(rack_count) #prints out a dictionary

    for eachEntry in word_count:
        if eachEntry in rack_count:
            if word_count[eachEntry] <= rack_count[eachEntry]:
                trues += 1
        if trues == len(word_count):
            return eachWord

            
def main():
    wordList = openFile()
    rack = getRack2()
    validWords = []

    for eachWord in wordList:
        validWords.append(wordCheck(eachWord, rack))

    validWords = filter(None, validWords)
    validWords = list(validWords)
    #print(validWords)

    scoring(validWords)

#############

def scoring(validWords):
    """print the score first followed by the word, one entry per line"""

    #testWord = "HELLO"
    results = []
    
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
    for eachWord in validWords:
        wordScore = 0
        for eachLetter in eachWord:
            wordScore += scores[eachLetter]
        if wordScore < 10:
            wordScore = str(wordScore)
            wordScore = "0" + wordScore
        else:
            wordScore = str(wordScore)
        results.append(wordScore + " " + eachWord)
    results = sorted(results, reverse=True)
    for eachResult in results:
        print(eachResult)

##############

main()
