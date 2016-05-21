"""----------------------------------------------------------------
This file contains a program that prompts the user to
enter patterns and it prints all the words in the official
crossword dictionary that match that pattern."""

## WRITTEN FOR PYTHON 2

# NOTE:  ALL TESTS ARE AT THE BOTTOM OF THE FILE


def crossHint(filename):
    """The main function takes in the filename where the crossword words
are stored.  It first reads in the list of words.  It sets up a loop
that repeats until the user decides to quit. Within the loop, it asks
the user for a pattern string, then gets the matching words for that
string, and then prints them.  Note that a pattern string must match
the length of the actual words exactly, and can contain alphabetic
characters and the symbol *, which indicates a blank in the puzzle,
where any letter might fit."""
    words = readWords(filename)
    goOn = "Y"

    while goOn.lower() in ["y", "yes"]:
        pattern = raw_input("Enter a pattern string, * for anything: ")
        matches = getMatchingWords(pattern, words)
        print
        print "---------------------"
        if matches == []:
            print "NO MATCHES"
        else:
            print "Words:"
            for m in matches:
                print "  ", m
        print "---------------------"
        print
        goOn = raw_input("Go again? (enter y or n): ")

# ------------  Testing ------------
# This function interacts with the user and everything else.
# Tests were run to check what happens if different files are read in,
# if the user enters a bad string (the program doesn't match anything),
# etc.


    
def readWords(filename):
    """Takes in a filename, opens the file, and reads in the list
of words in the file.  It returns a list object containing the
words, with whitespace removed."""
    inFile = open(filename, 'r')
    wordList = []
    for line in inFile:
        word = line.strip()
        wordList.append(word)
    inFile.close()
    return wordList



def getMatchingWords(pattern, wordList):
    """Takes in a pattern string and a list of words and it creates
a list of those words that match the pattern string.  This list
is returned"""
    lst = []
    for word in wordList:
        if matchesPattern(pattern, word):
            lst.append(word)
    return lst    




def matchesPattern(patt, word):
    """Takes in two strings, a pattern string and a word string, and it
determines if they match.  If their lengths are different, then they don't
match.  If their lengths are the same, then they must match exactly, unless
the pattern string contains a *, in which case it matches any letter in the
word string.  This function returns True or False"""
    if len(patt) != len(word):
        return False
    for i in range(len(patt)):
        if patt[i] != "*" and patt[i] != word[i]:
            return False
    return True





# ------------  Testing  readWords ------------
shortList = readWords("shortcross.txt")
longList = readWords("crosswords.txt")

# shortList:   should contain about 80 words from the beginning of the
#              crosswords list (aa) to the word abbeys
# longList:    should contain the entire crossword file list of words

# ------------  Testing getMatchingWords ------------
lst1 = getMatchingWords("*a*", shortList)
lst2 = getMatchingWords("a**e", longList)
lst3 = getMatchingWords("zyz**", longList)
lst4 = getMatchingWords("***************", longList)
lst5 = getMatchingWords("**u",longList)
# print lst1
# print lst2
# print lst3
# print lst4
# print lst5

# lst1:  ['aah', 'aal', 'aas']
# lst2:  ['abbe', 'able', 'abye', 'ache', ..., 'axle'] 24 words
# lst3:  []
# lst4:  ['acceptabilities', 'accessibilities', ...] 557 words
# lst5:  ['amu', 'eau', 'ecu', 'emu', 'feu', ...] 16 words



# ------------  Testing matchesPattern ------------
print matchesPattern("*at*", "mate")        # should be True
print matchesPattern("*at*", "rates")       # should be False
print matchesPattern("z***", "zoos")        # should be True
print matchesPattern("******", "yellow")    # should be True
print matchesPattern("exact", "exact")      # should be True
print matchesPattern("ag***", 'arbor')      # should be False
print matchesPattern("read", "real")        # should be False


# The call below automatically runs the whole program
crossHint("crosswords.txt")

