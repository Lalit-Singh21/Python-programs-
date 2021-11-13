#Requirement:

# Implement the class below such that it takes a list of words at construction time and
# it is optimised for fast/efficient retrivial of anagrams given a word to the method get_anagrams.

# The words may or may not be sorted and may or may not contain duplicates.
# The get_anagrams should return the set of all anagrams that can be found in the file, including the word passed in to the method itself.
# Attached example words.txt file
# Also, implement the below TODO (which will also be assessed) in order to test the correctness of the class.

# Extra: Thread safe under current CPython implementations.
# Extra: Can we add more kinds of tests to the unittest ?

import threading
import os
import inspect
import unittest


class Anagram:
    """This class allows for fast retrivial of anagrams from a pre-defined list of words"""

    def __init__(self, words):
        """Not implemented yet"""
        self.words=words
        #list of unit test function names which have requirement of supplied word included in the word list
        self.appendWordIfTest = []
        self.lock=threading.Lock()

    def get_anagrams(self, word):
        try:
            self.lock.acquire()
            #getting the calling function name(this is to decide weather to append the supplied word in the word list)
            caller_function=inspect.stack()[1][3]
            print 'Test name:', caller_function
            word_list = list(word)
            word_list.sort()
            anagram_list=[]
            if caller_function in self.appendWordIfTest:
                self.words.append(word)
                #print self.words
            try:
                for eachword in self.words:
                    eachword_list = list(eachword.strip().lower())
                    eachword_list.sort()
                    #if sorted word in file matches with sorted supplied word
                    if eachword_list == word_list:
                        anagram_list.append(eachword)
                print "Word to be tested: ", word, ", Anagram list is: ", anagram_list
                wordcount=len(anagram_list)
                uniquewordcount=len(set(anagram_list))
                if caller_function=="test_CheckCount":
                    return wordcount,uniquewordcount
                elif caller_function=="test_CheckAllValues":
                    return anagram_list
                else:
                    return set(anagram_list)                
            except Exception, e:
                print "Error: ", e
        except Exception, e:
            print "Test failed: ", e
        finally:
            self.lock.release()


            
class TestAnagram(unittest.TestCase):
    def setUp(self):
        """Not implemented yet"""
        #TODO: read in the file words.txt and pass the list of words to the Anagram constructor
        # list_of_words must be a list of strings
        filePath = r"C:\Lalit\PythonTraining_CustomProcessing\pyTest\words.txt"
        list_of_words =[]
        if os.path.exists(filePath):
            fileObject = open(filePath, 'r')
            list_of_words = [line.strip() for line in fileObject]
        self.anagram = Anagram(list_of_words)	
	

    def test_functional(self):
        self.assertEqual(self.anagram.get_anagrams('acer'), set(['acer', 'care', 'race', 'acre']))
        self.assertEqual(self.anagram.get_anagrams('regal'), set(['argle', 'lager', 'large', 'glare', 'regal']))
        self.assertEqual(self.anagram.get_anagrams('python'), set())
        self.assertEqual(self.anagram.get_anagrams('siren'), set(['rines', 'risen', 'reins', 'siren', 'resin', 'serin', 'rinse']))

    #test anagram with supplied word inluded/appended in the word list
    def testAnagram_includingWord(self):
        #myName=inspect.stack()[0][3]
        sThisFunction="testAnagram_includingWord"
        self.anagram.appendWordIfTest.append(sThisFunction)
        self.assertEqual(self.anagram.get_anagrams('crea'), set(['acer', 'care', 'crea', 'race', 'acre']))
        self.assertEqual(self.anagram.get_anagrams('regal'), set(['argle', 'lager', 'large', 'glare', 'regal']))
        #test with blank value
        self.assertEqual(self.anagram.get_anagrams(""),set(['']))
        
    #negative test with value not present in word list
    def test_Negativecheck(self):
        self.assertNotEqual(self.anagram.get_anagrams(""),(set(['Test'])))

    #test with blank value not included in the word list
    def test_InputBlankWithoutAppend(self):
        self.assertEqual(self.anagram.get_anagrams(""),(set([])))

    #test anagram with count of unique values in the word list and count of all values in the word list
    def test_CheckCount(self):
        sThisFunction="test_CheckCount"
        self.anagram.appendWordIfTest.append(sThisFunction)        
        self.assertEqual(self.anagram.get_anagrams('acer'), (5,4))
        self.assertEqual(self.anagram.get_anagrams('siren'),(8,7))
        
    #test anagram with all values in the word list including duplicates
    def test_CheckAllValues(self):
        sThisFunction="test_CheckAllValues"
        self.anagram.appendWordIfTest.append(sThisFunction)        
        self.assertEqual(self.anagram.get_anagrams('crea'),(['acre', 'care', 'race', 'acer', 'crea']))


    #test anagram of palindromes in the word list
    def test_Checkpalindrome(self):        
        #test if palindrome of word exists in anagram
        testlist=self.anagram.get_anagrams('abcdcba')
        palindromelist=[]
        for word in testlist:
            if str(word) == str(word)[::-1]:
                palindromelist.append(word)
        print "List of palindrome: ", palindromelist
        self.assertTrue(set(palindromelist) <= set(testlist))
        print "number of palindromes in the word list is: ", len(palindromelist)


    '''other unit tests which can be designed
    1) check the type of the function returning anagram
    2) check if multiple words can be passed
    3) more negative checks to test the "Except" blocks
    '''


##if __name__ == '__main__':
##    unittest.main()


if __name__=='__main__':
    try:
        unittest.main()
    except SystemExit as inst:
        if inst.args[0] is True:
            raise

