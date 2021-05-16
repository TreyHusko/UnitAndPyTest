import unittest
import palindrome
import pytest

class testPalindrome(unittest.TestCase):
    def test_Palindrome1(self):
        result = palindrome.pal('dog')
        self.assertEqual(result, True)

    def test_Palindrome2(self):
        result = palindrome.pal('RacECAR')
        self.assertEqual(result, True)

    def test_Palindrome3(self):
        self.assertRaises(ValueError, palindrome.pal, 'dad')

if __name__ == "__main__":
    unittest.main()

# def test_pal():
#     assert palindrome.pal('dog') == True
# def test_pal2():
#     assert palindrome.pal('RacECAR') == True
# def test_pal3():
#     with pytest.raises(ValueError):
#         palindrome.pal('dad')