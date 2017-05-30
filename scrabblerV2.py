
def puller(target):
    #function pulls words from file and compiles them into an array fLines
    with open(target) as f:
        fileLines = f.read().splitlines()
    return fileLines

def create_dictionary(letters):
    # creates a dictionary for the letters used in input

    scrabbledDict = {}
    for letter in letters:
        if letter not in scrabbledDict:
            scrabbledDict[letter] = 0
        scrabbledDict[letter] += 1
    scrabbledDict['size'] = len(letters)

    return scrabbledDict

def match_word(scrabbledLetters, word):
    # checks if the letters in scrabbledDict can make the given words

    if len(scrabbledLetters) < len(word):
        return False

    lettersDictionary = create_dictionary(scrabbledLetters)
    wordDictionary = create_dictionary(word)

    for letter in word:
        if letter not in lettersDictionary or wordDictionary[letter] > lettersDictionary[letter]:
            return False

    return True

def scrabbler(letters, listWords):
    
    count = 0

    for word in listWords:
        if match_word(letters, word):
            print word
            count += 1

    print count

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        letters = sys.argv[1].strip()

    listWords = puller('words.txt')

    scrabbler(letters, listWords)
