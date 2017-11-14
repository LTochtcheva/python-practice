# The main idea is to count all the occuring characters(UTF-8) in string. If you have string like this aba then the result should be { 'a': 2, 'b': 1 }

# What if the string is empty ? Then the result should be empty object literal { }
def count(string):
    if (len(string) == 0):
        return {}
    letters = {}
    for char in string:
        if (char in letters):
            letters[char] = letters[char] + 1
        else:
            letters[char] = 1
    print('letters: ',letters)
    return letters


def test_answer():
    assert count('aba') == { 'a': 2, 'b': 1 }
    assert count('') == {}

