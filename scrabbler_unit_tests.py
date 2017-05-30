import unittest
from scrabbler import puller, scrabbler, match_pre, match_suf, prefix, suffix

class ScrabblerTestMethods(unittest.TestCase):

    def test_puller(self):
        testDictionary = puller('test_dictionary.txt')

        self.assertEqual(len(testDictionary), 9, 'length of the test dictionary should be 9')

        testList = ['apple', 'are', 'art', 'aspen', 'banana', 'bird', 'bin', 'burn', 'burnt']
        for x in range(0,8):
            self.assertEqual(testDictionary[x], testList[x])


    def test_scrabbler(self):

        self.assertEqual(scrabbler('bin', 'test_dictionary.txt'), ['bin'])

        self.assertEqual(scrabbler('nib', 'test_dictionary.txt'), ['bin'])

        self.assertEqual(scrabbler('paplertsn', 'test_dictionary.txt'), ['apple', 'are', 'art', 'aspen'])

        self.assertEqual(scrabbler('tare', 'test_dictionary.txt'), ['are', 'art'])

        with self.assertRaises(LookupError):
            scrabbler('abc', 'test_dictionary.txt')

    def test_prefix(self):

        self.assertEqual(prefix('ap', 'test_dictionary.txt'), ['apple'])

        self.assertEqual(prefix('a', 'test_dictionary.txt'), ['apple', 'are', 'art', 'aspen'])

        self.assertEqual(prefix('bi', 'test_dictionary.txt'), ['bird', 'bin'])

    def test_suffix(self):

        self.assertEqual(suffix('ple', 'test_dictionary.txt'), ['apple'])

        self.assertEqual(suffix('n', 'test_dictionary.txt'), ['aspen', 'bin', 'burn'])

if __name__ == '__main__':
    unittest.main()
