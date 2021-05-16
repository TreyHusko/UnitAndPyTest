import unittest
import wordCount
import pytest

class testCaseWordCount(unittest.TestCase):
    def test_WordCount1(self):
        result = wordCount.count('The dog ran down the road')
        self.assertEqual(result, 5)
    
    def test_WordCount2(self):
        self.assertRaises(ValueError, wordCount.count, '')

    def test_WordCount3(self):
        self.assertRaises(ValueError, wordCount.count, 'The dog jumped.')

if __name__ == "__main__":
    unittest.main()

# def test_count():
#     assert wordCount.count('The dog ran down the road') == 5

# def test_count2():
#     with pytest.raises(ValueError):
#         wordCount.count('')


# def test_count3():
#     with pytest.raises(ValueError):
#         wordCount.count('The dog jumped.')