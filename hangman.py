import random
import string
import sys

WORDSLIST = "words.txt"
NUMOFGUESSES = 7

#function to load the words list from external file "words.txt" and
#return the words as a list.
def loadWords():
    print("Loading words from file", WORDSLIST)
    try:    
        file = open(WORDSLIST, 'r', 1)
    except (IOError):
        print("Failed to read file", WORDSLIST, "quitting.")
        sys.exit(0)  
    extractedWords = file.readline()
    words = extractedWords.split()
    print(len(words), "words loaded successfully")
    return words

#function that takes in a wordlist and choses a word
#randomly from the list
def chooseWord(wordsList):
    word = random.choice(wordsList)
    #loop to avoid the choice of the reserve word 'quit'
    while word == "quit":
        word = random.choice(wordsList)
    return random.choice(wordsList)
#takes in the word to guess and a list of the letters the user has guessed and
#returns the string displaying "_"'s for unguessed letters and the actual letter
#for correctly guessed letters. For example, if the word is "hello" and lettersGuessed
#is ['x','y','l','o'] the function would return "_ _ l l o"
def displayWord(word,lettersGuessed):
    displayedWord = ""
    for c in word:
        if c in lettersGuessed:
            displayedWord += c + " "
        else:
            displayedWord += "_ "
    return displayedWord
#Displays the letters the user has guessed by converting the list into an organized string
def displayLetters(lettersGuessed):
    if len(lettersGuessed) == 0:
        return "None."
    displayedLetters = ""
    for l in lettersGuessed:
        displayedLetters += l + " "
    return displayedLetters

def getInput(wordToGuess, lettersGuessed):
    while 1:
        guess = input("Please guess a letter or the word: ")
        guess = guess.lower()
        if len(guess) == 1 and guess not in lettersGuessed:
            lettersGuessed.append(guess)
        elif len(guess) == 1 and guess in lettersGuessed:
            print("You've already guessed that letter! Try again")
            continue
        break
    return guess
    
def runGame():
    lettersGuessed = []
    wordToGuess = chooseWord(loadWords())
    guessesLeft = NUMOFGUESSES
    print()
    print("Welcome to hangman! I'm thinking of a", len(wordToGuess), "letter word." 
          " To win the game, you must guess the word correctly. You can either guess"
          " the word letter by letter or guess the complete word. Type \"quit\" at any"
          " time to quit.")
    print()
    while 1:
        print("Word to guess:", displayWord(wordToGuess,lettersGuessed))
        print("Letters guessed:", displayLetters(lettersGuessed))
        print()
        currentGuess = getInput(wordToGuess, lettersGuessed)
        if currentGuess == "quit":
            print("Yup got it")
            break
        
    print("Goodbye!")
runGame()
    

