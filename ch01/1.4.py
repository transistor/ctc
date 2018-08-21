""" 1.4: Palindrome Permutation

    The question is phrased in an awkward way. Restating it makes it simpler:
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
    """ Count frequency of each char. If only one char appears an odd number
        of times, s can form a palindrome

        Note: need to skip spaces for the question
    """

    freq = {}
    for c in s:
        if c == ' ':
            continue
        elif c in freq:
            freq[c] += 1
        else:
            freq[c] = 1

    # Check for single odd freq
    odd_found = False
    for v in freq.values():
        if (v & 0x1):
            if odd_found:
                return False
            else:
                odd_found = True

    return True

pp = palindrome_permutation


# Test cases
x = ['tact coa', 'ABCD ABCD', 'ABCD Q ABCD', 'ABAB', 'BBBB', 'A B C D E B C E F A', 'abc', '123 456']
y = [True, True, True, True, True, False, False, False]

def run_tests():
    try:
        for i, s in enumerate(x):
           assert(pp(s) == y[i])

        print("All tests passed")
    except AssertionError:
        print("Error on test %i (input: %s)" % (i,s))

rt = run_tests
