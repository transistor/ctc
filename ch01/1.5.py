""" 1.5: One Away

    This is a type of "edit distance" question

    Three types of edits:
        i) Character insertion
        ii) Character removal
        iii) Character swap

    Assuming the inputs do not differ in length by more than 1 character, scan
    through them and check for a mismatch. If a mismatch is found, consider the
    three options we have for 'editing' the strings (insert/remove/swap).
"""

def one_away_compact(a, b):
    """ More compact code than second implementation below """

    # Early exit
    N, M = len(a), len(b)
    if (abs(N-M) > 1):
        return False
    elif (not a and b or a and not b):
        return False

    # Check if there is a mismatch in the two strings up to min(N,M)
    i = 0
    while (i < min(N,M)):
        if (a[i] == b[i]):
            i += 1
        else:
            # Mismatch found. Check three options
            first = a[i+1:] == b[i:]    # insert in to a / delete from b
            second = a[i:] == b[i+1:]   # insert in to b / delete from a
            third = a[i+1:] == b[i+1:]  # char swap
            return (first or second or third)

    # Fall-through: two possible cases, both returning True:
    #   i) if (N==M), and no mismatch was found, then strings are identical
    #
    #   ii) if abs(N-M) == 1, and the first min(N,M) characters matched, then
    #       the extra character in the longer string represents 1 insertion

    return True


def one_away(a, b):

    # Early exit
    N, M = len(a), len(b)
    if abs(N-M) > 1:
        return False

    # If strings are the same length, then the only possibility for handling
    # a mismatch is a character replacement
    if (N == M):
        i = 0
        while (i < N):
            if a[i] != b[i]:                # Mismatch found
                return a[i+1:] == b[i+1:]   # Remaining strings must be equal

            i += 1

        return True                         # Strings are equal
    else:
        # Strings differ in length by 1. Either a character must be deleted
        # from one string, or inserted in to the other
        #
        # Idea: find the point of mismatch, then check if the remaining strings
        #       match using either one insertion or deletion
        if (N < M):
            shorter, longer = a, b
            len_s, len_l = N, M
        else:
            shorter, longer = b, a
            len_s, len_l = M, N

        for i in xrange(len_s):
            if shorter[i] != longer[i]:
                if (shorter[i:] == longer[i+1:]):       # Delete from longer
                    return True
                elif (shorter[i+1] == longer[i:]):      # Insert in shorter
                    return True
                else:                                   # Neither work
                    return False

        # Fall-through: the strings match up to the final char. Thus, a deletion
        # of the final char in the longer string, or an insertion on to the
        # shorter string, create a match
        return True

# Test cases
x = [('', ''), ('hi', 'hi'), ('pale', 'ple'), ('pales', 'pale'), ('pale', 'bale'), ('pale', 'bake'), ('hello', 'HeLlo'), ('ball', 'fell'), ('ii', 'jj')]
y = [True, True, True, True, True, False, False, False, False]

def run_tests():
    try:
        for i, test_pair in enumerate(x):
            a, b = test_pair
            assert(one_away(a,b) == y[i])
        print("All tests passed")
    except AssertionError:
        print("Error on test %i (input: %s, %s)" % (i, a, b))

rt = run_tests
