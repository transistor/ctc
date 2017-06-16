# Note: We are assuming case-sensitivity

def is_unique(s):
    """ Using additional data structure

        A set cannot have duplicates. By creating a set of the characters
        in the string, duplicates will lead to a set length different than
        the string length
    """

    s_set = set(s)
    if (len(s) == len(s_set)):
        return 1    # All characters are unique
    else:
        return 0

def is_unique_in_place(s):
    """ No additional data structure

        Iterate over each character twice, essentially. This is ~O(n**2)
    """

    N = len(s)
    for i, pivot in enumerate(s):
        for compare in s[i+1:]:
            if pivot == compare:
                return 0    # Duplicate found
            else:
                pass

    return 1    # All unique


# Test cases
x = ['', ' ', '1', 'one', 'two', 'three', 'hello', 'HeLlO']
y = [True, True, True, True, True, False, False, True]

def run_tests():
    try:
        for i, test_string in enumerate(x):
            assert(is_unique(test_string) == y[i])
            assert(is_unique_in_place(test_string) == y[i])

        print("All tests passed")
    except:
        print("Error on test %i (input: %r)" % (i, test_string))

