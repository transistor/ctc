""" 
    This problem is a puzzle, not a coding problem.

    If you want to find out if s1 is a rotation of s2, simple concatenate two
    copies of s2 back-to-back, then call is_substring(), e.g.:

        s1: waterbottle
        s2: erbottlewat
        s2+s2: erbottlewaterbottlewat
                       ^^^^^^^^^^^

        s1: hello
        s2: lohel
        s2+s2: lohellohol
                 ^^^^^
"""

def is_substring(s1, s2):
    """ The question says that you are given this method. It is simple to write in Python """
    if s1 in s2:
        return 1
    else:
        return 0

def is_rotation(s1, s2):

    return is_substring(s1, s2*2)

# Test cases
x = [('waterbottle', 'erbottlewat'), ('hello', 'lohel'), ('ABCdefGHI', 'GHIABCdef'), ('ab', 'ba'), ('a', 'a'), ('hello', 'jello'), ('Hi', 'hi') ]
y = [True, True, True, True, True, False, False]

def run_tests():
    try:
        for i, test_pair in enumerate(x):
            s1, s2 = test_pair
            assert(is_rotation(s1, s2) == y[i])

        print("All tests passed")
    except:
        print("Error on test %i (input: %s, %s)" % (i, s1, s2))
