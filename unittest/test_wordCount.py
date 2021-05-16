import unittest
import wordCount

print("Please enter a string.")
inp = input("String is: ")

class TestCase(unittest.TestCase):
    def test_inputType(self):
        self.assertEqual(type(inp),type("string"))
    
    def test_returnType(self):
        result = wordCount.countWord(inp)
        self.assertEqual(type(result),type(123))

    def test_correctResult(self):
        result = wordCount.countWord(inp)
        correct_result = len(inp.split())
        self.assertEqual(result,correct_result)

result = wordCount.countWord(inp)
print("There are ",result," words in the string.") 
if __name__ == '__main__':unittest.main()