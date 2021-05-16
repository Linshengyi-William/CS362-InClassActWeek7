import pytest
import palindrome

inp1 = "not palinedrome"
inp2 = 2
inp3 = "qwewq"
    
def test_inputType(inp):
        assert type(inp)==type("string")
    
def test_returnType(inp):
    result = palindrome.isPalindrome(inp)
    assert type(result)==type(True)

def test_correctResult(inp):
    result = palindrome.isPalindrome(inp)
    for i in range(0,len(inp)):
        if inp[i] != inp[len(inp)-i-1]:
            correct_result = False
            break
        correct_result = True
    assert result == correct_result

test_inputType(inp1)
test_inputType(inp2)
test_inputType(inp3)
test_returnType(inp1)
test_returnType(inp2)
test_returnType(inp3)
test_correctResult(inp1)
test_correctResult(inp2)
test_correctResult(inp3)


