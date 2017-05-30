
def puller(target):
    #function pulls words from file and compiles them into an array fLines
    with open(target) as f:
        fileLines = f.read().splitlines()
    return fileLines

def scrabbler(letters, target):
    # tester function to allow txt file to be specified with test txt file

    dictionary = puller(target)
    lettersListReference = []
    answerList = [] # returns list of words, FOR UNIT TEST IMPLEMENTATION ONLY

    for word in dictionary:
        # can throw out all cases in which the word in the dictionary is bigger than the letters because we can't reuse letters

        if len(word) > len(letters):
            continue

        lettersList = []
        for char in letters:
            lettersList.append(char)

        # would be faster to cycle throught the letters in the words in the dictionary because we're taking out the large word cases
        runner = True

        for char in word:
            try:
                lettersList.remove(char)
            except ValueError:
                runner = False
                break


        if runner:
            print word
            answerList.append(word) # used for test cases

    if len(answerList) == 0:
        raise LookupError('no words could be made from given letters')

    print len(answerList)
    return answerList # used for test cases

def prefix(letters, target):
    dictionary = puller(target)
    answer = [] # used for test cases

    # if we encounter a term that is a prefix and the next term is not a prefix, then all the following terms will not be prefixes and we can break the loop
    done = False
    nextDone = False

    for word in dictionary:
        if match_pre(letters, word):
            print word
            done = True
            answer.append(word)
        elif done:
            nextDone = True
        if done and nextDone:
            break

    return answer # used for test cases

def suffix(letters, target):
    dictionary = puller(target)
    answer = [] # used for test cases

    for word in dictionary:
        if match_suf(letters, word):
            print word
            answer.append(word)
    return answer #used for test cases

def match_pre(prefix, word):
    for i in range(0, len(prefix)):
        if prefix[i] != word[i]:
            return False
    return True

def match_suf(suffix, word):
    lengthSuffix = len(suffix)
    lengthWord = len(word)
    for i in range(0, len(suffix)):
        if suffix[i] != word[lengthWord - lengthSuffix + i]:
            return False
    return True


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        letters = sys.argv[1].strip()

    scrabbler(letters, 'words.txt')
