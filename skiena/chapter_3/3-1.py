"""
Give an algorithm that returns true if a string properly contains balanced paranthesis.
"""

def is_balanced(input_string):
    number_of_open_paranthesis = []

    for parenthesis in input_string:
        if parenthesis == "(":
            number_of_open_paranthesis.append("(")
        else:
            if number_of_open_paranthesis == []:
                return False
            number_of_open_paranthesis.pop()
    
    return len(number_of_open_paranthesis) == 0


if __name__ == "__main__":
    assert is_balanced(")(") == False
    assert is_balanced("()") == True
    assert is_balanced("((()))") == True
    assert is_balanced("()()()()())") == False
    assert is_balanced("()))))") == False
    assert is_balanced("())(") == False

