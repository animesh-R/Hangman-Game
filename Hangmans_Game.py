# Hangman game
#
# -----------------------------------
# Helper code
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
WORDLIST_FILENAME = "words.txt"
def loadWords():
    """
        Returns a list of valid words. Words are strings of lowercase letters.
        Depending on the size of the word list, this function may
        take a while to finish.
    """
    print("Loading word list from file...")
    #inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
        wordlist (list): list of words (strings)
        Returns a word from wordlist at random
    """
    return random.choice(wordlist)
# end of helper code
# -----------------------------------
# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
    wordlist = loadWords()
    '''
        Created on Jul 26, 2017
        @author: Animesh
    '''
def getGuessedWord(secretWord, lettersGuessed):
    word = ""
    for i in range(0,len(secretWord)):
        if secretWord[i] in lettersGuessed:
            word = str(word)+str(secretWord[i])
        else:
            word = str(word)+str(" _ ")
    return (word)
#.................................................................
def isWordGuessed(secretWord, lettersGuessed):
    i=0
    Set=True
    while(Set):
        if secretWord[i] not in lettersGuessed:
            return (False)
            #break
        else:
            i+=1
    if i==len(secretWord):
        return (True)
#......................................................
import string
def getAvailableLetters(lettersGuessed):
    alphabet=string.ascii_lowercase
    for i in range(0,len(lettersGuessed)):
        if lettersGuessed[i] in alphabet:
            temp=lettersGuessed[i]
            update = alphabet.find(temp)
            alphabet=alphabet[:update]+ "" +alphabet[(update+1):]
    return alphabet
#.............................................
#secretWord='apple'
def hangman(secretWord):
    '''
        secretWord: string, the secret word to guess.
        Starts up an interactive game of Hangman.
        * At the start of the game, let the user know how many
        letters the secretWord contains.
        * Ask the user to supply one guess (i.e. letter) per round.
        * The user should receive feedback immediately after each guess
        about whether their guess appears in the computers word.
        * After each round, you should also display to the user the
        partially guessed word so far, as well as letters that the
        user has not yet guessed.
        Follows the other limitations detailed in the problem write-up.
    '''
    i=8
    alt=[]
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is "+str(len(secretWord))+ " letters long.")
    print("-----------")
    print("you have " + str(i) + " guesses left ")
    print("Available letters : " +str(getAvailableLetters(' ')))
    while(i>0):
        var = raw_input("Please guess a letter : ")
        #alt.append(var)
        #print(alt)
        #if var not in getAvailableLetters(alt):
        # print("Oops! You've already guessed that letter:")
        if var in secretWord:
            if var not in getAvailableLetters(alt):
                print("Oops! You've already guessed that letter:"+str(getGuessedWord(secretWord,alt)))
                print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
                print("you have " + str(i) + " guesses left")
                print("Available letters : " +str(getAvailableLetters(alt)))
            else:
                alt.append(var)
                print("Good guess:" +str(getGuessedWord(secretWord,alt)))
                print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
                if isWordGuessed(secretWord, alt):
                    print("Congratulations, you won!")
                    return None
                else:
                    print("you have " + str(i) + " guesses left")
                    print("Available letters : " +str(getAvailableLetters(alt)))
        else:
            if var not in getAvailableLetters(alt):
                print("Oops! You've already guessed that letter:"+str(getGuessedWord(secretWord,alt)))
                print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
                print("you have " + str(i) + " guesses left")
                print("Available letters : " +str(getAvailableLetters(alt)))
            else:
                alt.append(var)
                print("Oops! That letter is not in my word: " +str(getGuessedWord(secretWord,alt)))
                i-=1
                if i==0:
                    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
                    print("Sorry, you ran out of guesses. the word was " +str(secretWord))
                else:
                    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
                    print("you have " + str(i) + " guesses left")
                    print("Available letters : " +str(getAvailableLetters(alt)))
                    #print(hangman('y'))
                    #print("Oops! You've already guessed that letter:")
                    # #Oops! You've already guessed that letter:
                    # When you've completed your hangman function, uncomment these two lines
                    # and run this file to test! (hint: you might want to pick your own
                    # secretWord while you're testing)
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)