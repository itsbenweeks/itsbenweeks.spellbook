# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
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

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    trueGuesses = 0
    for char in lettersGuessed:
#Lets remove duplicate guesses.
##Doesn't need to be here since the input is now sanitized.        
##        while lettersGuessed.count(char) > 1:
##            lettersGuessed.remove(char)
        if char in secretWord:
            trueGuesses += secretWord.count(char)
## Wasn't doing a proper count because it was imporperly indented to run inside the for loop, causing no winning condition.
    if trueGuesses == len(secretWord):
        return True
    else:
        return False

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: dictionay, what letters have been guessed correctly, what letters haven't been guessed, and what is still to be guessed

    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    global letters
    lettersGuessed = lettersGuessed.lower()
    for char in lettersGuessed:
        if char not in string.ascii_lowercase:
            print 'Come on, guy. What is this? Your first rodeo, clown?'
        elif char in letters['trueGuesses']+letters['untrueGuesses']:
            print 'You\'ve guessed that already, buddy.'
        elif char in secretWord:
            letters['trueGuesses'] += char
            print 'Cool, bro! That is totally in there!'
            letters['guessable'] = letters['guessable'].replace(char, '')
        else:
            letters['untrueGuesses'] += char
            print 'Naw, dude. Guess again.'
#We may want this part of the function someplace else

    for char in letters['guessable']:          
        if char in secretWord:
            secretWord = secretWord.replace(char, '_')
    for char in secretWord:
        secretWord += '%s ' %char
            
    return secretWord

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    global letters
    return letters['guessable']

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

    global letters
    letters['guessable'] = string.ascii_lowercase
    letters['trueGuesses'] = ''
    letters['untrueGuesses'] = ''
 
    print 'Welcome to hang, man.'
    print 'Lets get started, I\'ve picked a word, and you have to guess it. \n You can guess incorrectly 7 times'
    print 'There are %s letters in this word I have chosen!' %len(secretWord)
    countSecretWord = len(secretWord)
    print "_ "*countSecretWord
    
    while len(letters['untrueGuesses'])<7:

        if  isWordGuessed(secretWord, letters['trueGuesses']):
            print 'You did it!'
            break
        else:
            if len(letters['untrueGuesses'])==6:
                print '\n\nYou have one guess left'
                
            else:
                print '\n\nYou have %d guesses left' % (7-len(letters['untrueGuesses']))
            print 'Available letters are %s' % letters['guessable']
            guess = raw_input('Guess a letter, buddy: ')
            print getGuessedWord(secretWord, guess)
    again = raw_input ('Would you like to play again? ')
    if again[0]=='y':
        secretWord = chooseWord(wordlist).lower()
        return hangman(secretWord)
    else:
        return
    
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
#wordlist = loadWords()
#secretWord = chooseWord(wordlist).lower()
letters={}
guess = ''
#hangman(secretWord)
hangman('candlemass')
