# Selling Bee Solver
# (c) 2022 Michael Tucker

from collections import defaultdict

class Trie:
    """
    Implementation of a trie for storing words.
    """
    def __init__(self):
        self.root = defaultdict()
        self.words = []

    # Inserts a word into the trie
    def insert(self, word):
        current = self.root
        for letter in word:
            current = current.setdefault(letter.upper(), {})
        current.setdefault("_end")

    # Loads word list into the trie if is long enough
    def loadWordList(self, fileName, minLength):
        with open(fileName) as f:
            contents = f.read()
        words = contents.splitlines()

        for word in words:
            if len(word) >= minLength:
                self.insert(word)

    # Returns words that can be made of the center_letter and outside_letters
    def getWords(self, center_letter, letters):
        self.words = []
        current = self.root
        word = ""
        self.trieCrawler(center_letter, letters, current, word)
        self.words.sort()
        return self.words

    # Recursive trie crawler to find all words using the letters
    def trieCrawler(self, center_letter, letters, current, word):
        if "_end" in current and center_letter in word:
            self.words.append(word)

        for next_letter in list(set(letters) & set(current.keys())):
            new_word = word[:]
            new_word += next_letter
            new_node = current[next_letter]
            self.trieCrawler(center_letter, letters, new_node, new_word)


def main():
    minWordLength = 4;
    wordCorpus = 'engmix.txt'
    beeTrie = Trie()
    beeTrie.loadWordList(wordCorpus, minWordLength)

    center_letter = ''
    while not (center_letter.isalpha() and len(center_letter)==1):
        center_letter = input('Center Letter: ')
        if len(center_letter) > 1:
            print('Input is too long, try again')
        elif len(center_letter) < 1:
            print('Input is too short, try again')
        elif not center_letter.isalpha():
            print('Input is invalid, try again')
    center_letter = center_letter.upper()

    outside_letters = ''
    while not (outside_letters.isalpha() and len(outside_letters)>0):
        outside_letters = input('Outside Letters: ')
        outside_letters = ''.join([i for i in outside_letters if i.isalpha()])
        if len(outside_letters) < 1:
            print('Input not valid, try again')
    outside_letters = outside_letters.upper()

    letters = outside_letters+center_letter
    print(beeTrie.getWords(center_letter, letters))

main()
