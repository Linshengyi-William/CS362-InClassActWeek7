
import unittest
import palindrome

print("Please enter a string.")
inp = input("String is: ")

class TestCase(unittest.TestCase):
    def test_inputType(self):
        self.assertEqual(type(inp),type("string"))
    
    def test_returnType(self):
        result = palindrome.isPalindrome(inp)
        self.assertEqual(type(result),type(True))

    def test_correctResult(self):
        result = palindrome.isPalindrome(inp)
        for i in range(0,len(inp)):
            if inp[i] != inp[len(inp)-i-1]:
                correct_result = False
                break
            correct_result = True
        self.assertEqual(result,correct_result)
    
if __name__ == '__main__':unittest.main()

