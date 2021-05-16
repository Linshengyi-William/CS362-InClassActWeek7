import pytest
import wordCount

inp1 = "this is a string"
inp2 = 123
inp3 = "thisisastring"


def test_inputType(inp):
    assert type(inp)==type("string")
    
def test_returnType(inp):
    result = wordCount.countWord(inp)
    assert type(result)==type(123)

def test_correctResult(inp):
    result = wordCount.countWord(inp)
    correct_result = len(inp.split())
    assert result==correct_result

test_inputType(inp1)
test_inputType(inp2)
test_inputType(inp3)
test_returnType(inp1)
test_returnType(inp2)
test_returnType(inp3)
test_correctResult(inp1)
test_correctResult(inp2)
test_correctResult(inp3)