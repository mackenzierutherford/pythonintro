#AMANDA OWENS MACKENZIE RUTHERFORD
# textmodel.py
#
# TextModel project!
#
# Name(s):
#
from porter import create_stem
import math
class TextModel(object):
    """A class supporting complex models of text."""

    def __init__(self):
        """Create an empty TextModel."""
        #
        # Create dictionaries for each characteristic
        #
        self.text = ''
        self.words = {}           # For counting words
        self.wordlengths = {}     # For counting word lengths
        self.stems = {}           # For counting stems
        self.sentencelengths = {} # For counting sentence lengths
        
        # Create another of your own
        #
        self.punctuation = {}     # For counting ___________

    def __repr__(self):
        """Display the contents of a TextModel."""
        s = 'Words:\n' + str(self.words) + '\n\n'
        s += 'Word lengths:\n' + str(self.wordlengths) + '\n\n'
        s += 'Stems:\n' + str(self.stems) + '\n\n'
        s += 'Sentence lengths:\n' + str(self.sentencelengths) + '\n\n'
        s += 'MY PARAMETER:\n' + str(self.punctuation)
        return s

    # Include other functions here.
    # In particular, you'll need functions that add to the model.
    def readTextFromFile(self, filename):
        """takes a string and sets self.text to the text in that
        text in that file represented as a single string"""
        
        f = open( filename )
        text = f.read()
        self.text = text
        f.close()
        return self.text

    def makeSentenceLengths(self):
        """uses the text in self.text to create the dictionary
        of self.sentencelengths"""
        
        LoW = self.text.split()
        d = self.sentencelengths
        currentcount = 0
        for word in LoW:
            currentcount += 1
            if word[-1] in '!?.':
                if currentcount not in d:
                    d[currentcount] = 1
                    currentcount = 0
                else: 
                    d[currentcount] += 1
                    currentcount = 0

        return d
    
    def cleanString(self, s):
        """cleans the string of all punctuation and uppercase letters"""
        s = s.lower()
        import string 
        for p in string.punctuation:
            s = s.replace(p, '')
        return s
    
    def makeWordLengths(self):
        """uses the text in self.text to create the dictionary
         of word-length features"""
        d = self.wordlengths
        L = self.cleanString(self.text)
        L = L.split(" ")
        for word in L:
            if len(word) not in d:
                d[len(word)] = 1
            else:
                d[len(word)] += 1
        return d
    
    def printAllDictionaries(self):
        """prints the current dictionaries"""
        print(self)

    def makeWords(self):
        """makes the word dictionary"""
        d = self.words
        L = self.cleanString(self.text)
        L = L.split()
        for word in L:
            if word not in d:
                d[word] = 1
            else:
                d[word] += 1
        return d

    def makeStems(self):
        """makes stems dictionary"""
        d = self.stems
        L = self.cleanString(self.text)
        L = L.split()
        for word in L:
            if create_stem(word) not in d:
                d[create_stem(word)] = 1
            else:
                d[create_stem(word)] += 1
        return d

    def makePunctuation(self):
        """makes punctuation dictionary"""
        d = self.punctuation
        LoW = self.text
        for ch in LoW:
            if ch in '!?.,;:–)\'"':
                if ch not in d:
                    d[ch] = 1
                else:
                    d[ch] += 1
        return d

    def normalizeDictionary(self, d):
        """returns a normalized dictionary"""
        nd = {}
        for k in d:
            nd[k] = d[k]/(sum(d.values()))
        return nd

    def smallestValue(self, nd1, nd2):
        """"finds? smallest value"""
        L = []
        for k in nd1:
            L += [nd1[k]]
        for k in nd2:
            L += [nd2[k]]
        return min(L)
    
    def compareDictionaries(self, d, nd1, nd2):
        """compares the dictionaries"""
        nd1 = self.normalizeDictionary(nd1)
        nd2 = self.normalizeDictionary(nd2)
        total1 = 0.0
        total2 = 0.0
        epsilon = 0.5*self.smallestValue(nd1, nd2)
         
         #nd1
        for k in d:
            if k not in nd1:
                total1 += d[k]*math.log(epsilon)
            else:
                total1 += d[k]*math.log(nd1[k])
        
        #nd2
        for k in d:
            if k not in nd2:
                total2 += d[k]*math.log(epsilon)
            else:
                total2 += d[k]*math.log(nd2[k])
        return [total1, total2]
    
    def createAllDictionaries(self):
        """Create out all five of self's
           dictionaries in full.
        """
        self.makeSentenceLengths()
        self.makeWords()
        self.makeStems()
        self.makeWordLengths()

    def compareTextWithTwoModels(self, model1, model2):
        """runs comparison with two texts"""

        sentlen = self.compareDictionaries(self.makeSentenceLengths(), model1.makeSentenceLengths(), model2.makeSentenceLengths())
        words = self.compareDictionaries(self.makeWords(), model1.makeWords(), model2.makeWords())
        stems = self.compareDictionaries(self.makeStems(), model1.makeStems(), model2.makeStems())
        punct = self.compareDictionaries(self.makePunctuation(), model1.makePunctuation(), model2.makePunctuation())
        wordlen = self.compareDictionaries(self.makeWordLengths(), model1.makeWordLengths(), model2.makeWordLengths())

        print(("{0: >4} {1: >20} {2: >30}".format("name", A, B)))
        print(("{0: >4} {1: >20} {2: >30}".format("---", "-----", "-----")))
        print(("{0: >4} {1: >20} {2: >30}".format("words", words[0], words[1])))
        print(("{0: >4} {1: >20} {2: >30}".format("word length", wordlen[0], wordlen[1])))            
        print(("{0: >4} {1: >20} {2: >30}".format('sentence lengths',sentlen[0], sentlen[1])))
        print(("{0: >4} {1: >20} {2: >30}".format('stems',stems[0], stems[1])))
        print(("{0: >4} {1: >20} {2: >30}".format('punctuation',punct[0], punct[1]))) 
        print("\n\n\n")
        win1 = 0
        win2 = 0
        for L in [sentlen, words, stems, punct, wordlen]:
            if L[0] > L[1]:
                win1 += 1
            else: win2 += 1
        print("--------------")
        print(A, " wins on", win1, "features")
        print(B, " wins on", win2, "features\n\n")

        if win1 > win2:
            print("Text was more likely to be written by", A)
        elif win2 > win1:
            print("Text was more likely to be written by", B)
        else:
            print("I cant decide!! aaaaaarg")
            
        
# And test things out here...

TM = TextModel()
# Add calls that put information into the model

print(" +++++++++++ Kenz +++++++++++ ")
TM1 = TextModel()
TM1.readTextFromFile("mack.txt")
TM1.createAllDictionaries()  # provided in hw description


print(" +++++++++++ Amanda +++++++++++ ")
TM2 = TextModel()
TM2.readTextFromFile("amanda.txt")
TM2.createAllDictionaries()  # provided in hw description



print(" +++++++++++ Unknown text +++++++++++ ")
TM_Unk = TextModel()
TM_Unk.readTextFromFile("mystery2.txt")
TM_Unk.createAllDictionaries()  # provided in hw description

A = 'mackenzie'
B = 'amanda'

TM_Unk.compareTextWithTwoModels(TM1, TM2)








    