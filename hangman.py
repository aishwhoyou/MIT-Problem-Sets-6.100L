# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open("words.txt", 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True

    # FILL IN YOUR CODE HERE AND DELETE "pass"


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guess = ""
    for letter in secret_word:
        if letter in letters_guessed:
            guess += letter
        else:
            guess += "*"
    return guess


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters = ""
    for i in string.ascii_lowercase:
        if i not in letters_guessed:
            letters += i
    return letters

def choose_letters(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    get_available_letters: returns string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order

    returns: random letter from secret_word that has not been guessed
    
    """
    choose_from = ""
    letters = get_available_letters(letters_guessed)
    for i in secret_word:
        if i in letters:
            choose_from += i
    new = random.randint(0, len(choose_from)-1)
    revealed_letter = choose_from[new]
    return revealed_letter
        

def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses = 10
    letters_guessed = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    print("Welcome to Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")

    while not has_player_won(secret_word, letters_guessed) and guesses > 0:
        print("--------------")
        print(f"You have {guesses} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        guess = input("Please guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            if guess in letters_guessed:
                print(f"Oops! You have already guessed that letter: {get_word_progress(secret_word,letters_guessed)}")
            elif guess in vowels and guess not in secret_word:
                letters_guessed.append(guess)
                print(f"Oops! That letter is not in my word: {get_word_progress(secret_word,letters_guessed)}")
                guesses -= 2
            elif guess.lower() in secret_word:
                letters_guessed.append(guess)
                print(f"Good guess: {get_word_progress(secret_word,letters_guessed)}")
            else:
                print(f"Oops! That letter is not in my word: {get_word_progress(secret_word,letters_guessed)}")
                guesses -= 1
        elif with_help and guess == '!':
            if guesses > 3:
                choose_letters(secret_word, letters_guessed)
                letters_guessed.append(choose_letters(secret_word,letters_guessed))
                print(f'Letter revealed: {choose_letters(secret_word,letters_guessed)}')
                print(get_word_progress(secret_word,letters_guessed))
                guesses -= 3
            else:
                print(f'Oops! Not enough guesses left: {get_word_progress(secret_word,letters_guessed)}')
        else:
            print(f"Oops! That is not a valid letter. Please input a letter from the alphabet: {get_word_progress(secret_word,letters_guessed)}")
    score = guesses + (3 * len(secret_word)) + (4 * len(set(secret_word)))   
    if guesses == 0:
        print("--------------")
        print(f"Sorry, you ran out of guesses. The word was {secret_word}")
    else:
        print("--------------")
        print("Congratulations, you won!")
        print(f"Your total score for this game is: {score}")



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test
if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
    with_help = True
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.


