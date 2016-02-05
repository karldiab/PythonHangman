import random
import string
import sys

WORDSLIST = "words.txt"

def loadWords():
    print("Loading words from file", WORDSLIST)
    try:    
        file = open(WORDSLIST, 'r', 1)
    except (IOError):
        print("Failed to read file", WORDSLIST, "quitting.")
        sys.exit(0);
    print("Words loaded successfully")
    return file;
loadWords()

