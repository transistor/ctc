""" 1.1: Is Unique """

# Note: Assume strings are case-sensitive

def is_unique(s):
    """ Using additional data structure: O(n) time and space.

        A set cannot have duplicates. By creating a set of the characters
        in the string, duplicates will lead to a set length different than
        the string length
    """

    seen = set()
    for c in s:
        if c in seen:
            return False
        
        seen.add(c)

    return True


def is_unique_in_place(s):
    """ No additional data structure: O(1) space

        Iterate over each character twice, essentially. This is O(n^2) time.
    """
    N = len(s)
    for i in xrange(N):
        c = s[i]
        for j in xrange(i+1, N):
            if (s[j] == c):
                return False

    return True


# Test cases
x = ['', ' ', '1', 'one', 'two', 'three', 'hello', 'HeLlO']
y = [True, True, True, True, True, False, False, True]

def run_tests():
    try:
        for i, test_string in enumerate(x):
            assert(is_unique(test_string) == y[i])
            assert(is_unique_in_place(test_string) == y[i])
        print("All tests passed")
    except AssertionError:
        print("Error on test %i (input: %r)" % (i, test_string))

rt = run_tests
