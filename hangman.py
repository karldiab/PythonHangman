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
    while word == "quit" or len(word) < 4:
        word = random.choice(wordsList)
    return random.choice(wordsList)
#takes in the word to guess and a list of the letters the user has guessed and
#returns the string displaying "_"'s for unguessed letters and the actual letter
#for correctly guessed letters. For example, if the word is "hello" and lettersGuessed
#is ['x','y','l','o'] the function would return "_ _ l l o"
def displayWord(word):
    global lettersGuessed
    displayedWord = ""
    for c in word:
        if c in  lettersGuessed:
            displayedWord += c + " "
        else:
            displayedWord += "_ "
    return displayedWord
#Displays the letters the user has guessed by converting the list into an organized string
def displayLetters():
    if len( lettersGuessed) == 0:
        return "None."
    displayedLetters = ""
    for l in lettersGuessed:
        displayedLetters += l + " "
    return displayedLetters
##Validates the user's input and returns the input if properly validated. Keeps propting
##the user for valid input until correct then returns the validated input
def getInput(wordToGuess):
    global lettersGuessed
    while 1:
        guess = input("Please guess a letter or the word: ")
        guess = guess.lower()
        if not guess.isalpha():
            print("You've got at least one non-letter in your guess. Try again silly!")
            continue
        if len(guess) == 1 and guess not in  lettersGuessed:
             lettersGuessed.append(guess)
        elif len(guess) == 1 and guess in  lettersGuessed:
            print("You've already guessed that letter! Try again")
            continue
        break
    return guess
##Takes in the user's guess and compares it to the word to guess. Returns 0 if the guess
##is incorrect, 1 if the user had guessed a letter and it is in the word and 2 if the user
##has guessed the word correctly
def interpretGuess(wordToGuess, guess):
    global guessesLeft
    print()
    if (len(guess) == 1 and guess in wordToGuess):
        #ugly nested if statement because I couldn't get a ternary opperator to work in python :(
        if (wordToGuess.count(guess) == 1):
            tempString = "is 1 " + guess
        else:
            tempString = "are " + str(wordToGuess.count(guess)) + " " + guess + "'s"
        print("Good job! There", tempString, "in the word.")
    elif (len(guess) == 1 and guess not in wordToGuess):
        print("Sorry there are no", guess, "'s in the word.")
        guessesLeft -= 1
    elif (len(guess) != 1 and guess != wordToGuess):
        print("Sorry,", guess, "is not the word.")
        guessesLeft -= 1
def checkForGameOver(wordToGuess, guess):
    global guessesLeft
    global lettersGuessed
    if not guessesLeft:
        print("You lose :( The word was", wordToGuess)
        return 1
    if guess == wordToGuess:
        print("You win!!! The word was", guess)
        return 1
    for c in wordToGuess:
        if c not in lettersGuessed:
            return 0
    print("You win!!! The word was", guess)
    return 1
def runGame():
    global wordsList
    global guessesLeft
    wordToGuess = chooseWord(wordsList)
    guessesLeft = NUMOFGUESSES
    global lettersGuessed
    lettersGuessed = []
    print()
    print("Welcome to hangman! I'm thinking of a", len(wordToGuess), "letter word." 
          " To win the game, you must guess the word correctly. You can either guess"
          " the word letter by letter or guess the complete word. Type \"quit\" at any"
          " time to quit.")
    print()
    while 1:
        print("Word to guess:", displayWord(wordToGuess))
        print("Letters guessed:", displayLetters())
        print()
        if  guessesLeft != 1:
            print("You have",  guessesLeft, "guesses remaining.")
        else:
            print("You have 1 guess remaining.")
        currentGuess = getInput(wordToGuess)
        if currentGuess == "quit":
            break
        interpretGuess(wordToGuess, currentGuess)
        if checkForGameOver(wordToGuess, currentGuess):
            playAgain = input("Play again? (yes/no)")
            if playAgain.lower() == "yes":
                runGame()
            else:
                break
    print("Goodbye!")
wordsList = loadWords()
runGame()
    

