"""
Give an algorithm that returns true if a string properly contains balanced paranthesis.
"""

def is_balanced_which_index(input_string):
    count = 0
    for i in range(0, len(input_string)):
        if input_string[i] == "(":
            count += 1
        if input_string[i] == ")":
            count -= 1
        if count < 0: 
            print("index with an issue %i" %i)
            return False
    
    if count != 0:
        print("index with an issue is %i" %(len(input_string) - 1))
        return False
    return True
    
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

    assert is_balanced_which_index(")(") == False
    assert is_balanced_which_index("())(") == False
    assert is_balanced_which_index("()()()()())") == False
    assert is_balanced_which_index("()()()()()") == True




