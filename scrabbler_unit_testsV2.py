import unittest
from scrabblerV2 import puller, create_dictionary

class ScrabblerTestMethods(unittest.TestCase):

    def test_puller(self):
        testDictionary = puller('test_dictionary.txt')

        self.assertEqual(len(testDictionary), 9, 'length of the test dictionary should be 9')

        testList = ['apple', 'are', 'art', 'aspen', 'banana', 'bird', 'bin', 'burn', 'burnt']
        for x in range(0,8):
            self.assertEqual(testDictionary[x], testList[x])


    def test_create_dictionary(self):
        testerDictionary = {'a': 1, 'b': 2, 'c': 1}
        functionDictionary = create_dictionary('abbc')
        functionDictionary2 = create_dictionary('abcb')

        self.assertEqual(testerDictionary, functionDictionary)
        self.assertEqual(testerDictionary, functionDictionary2)

if __name__ == '__main__':
    unittest.main()
