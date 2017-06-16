""" The question is phrased in an awkward way. Restating it makes it simpler:
    Can the letters of the input be arranged as a palindrome (even using
    words)?

    Since the palindrome doesn't need to use real words (from a dictionary),
    we can ignore spaces in the input.

    The problem is now reduced to something simpler:
        1. If there are an even number of characters in the input string, are
           there an even number of each type of character?
                e.g.: ABAB CDCD
                      ABCD DCBA
                          Char count: A:2, B:2, C:2, D:2

        2. If there is an odd number of input characters, is there an odd
           number of exactly one character, and an even number for all others?
                e.g.: ABAB Q CDCD
                      ABCD Q CDCD
                          Char count: A:2, B:2, C:2, D:2, Q:1

           (The odd numbered character forms the pivot in the middle of the
            palindrome)
"""

def palindrome_permutation(s):
    """ Bugs:
            - Does not ignore whitespace
            - Case-sensitive (obviously trivial to change)
    """

    # Get number of unique characters
    uniques = len(set(s))

    # Use a dict to keep count of characters
    count = {}

    # Scan through input and count chars
    for c in s:
        if (count.has_key(c)):
            count[c] += 1
        else:
            count[c] = 1

    # Check if case (1) or case (2) above is satisfied:
    N = len(s)

    if (N%2 == 0):       # even-length input
        for key, val in count.iteritems():
            if (val%2 != 0):
                # Odd-number characters found
                return 0    # No palindrome possible
    else:
        odd_found = False
        for key, val in count.iteritems():
            if (val%2 != 0):
                if (odd_found):
                    # Multiple odd-number characters found
                    return 0    # No palindrome possible
                else:
                    odd_found = True

    return 1    # palindrome is possible

pp = palindrome_permutation


# Test cases
x = ['tact coa', 'ABCD ABCD', 'ABCD Q ABCD', 'ABAB', 'BBBB', 'A B C D E B C E F A', 'abc', '123 456']
y = [True, True, True, True, True, False, False, False]

def run_tests():
    try:
        for i, s in enumerate(x):
           assert(pp(s) == y[i])

        print("All tests passed")

    except:
        print("Error on test %i (input: %s)" % (i,s))
        
