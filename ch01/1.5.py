""" 
    This is a type of "edit distance" question

    Three types of edits:
        i) Character insertion
        ii) Character removal
        iii) Character swap

    The first two cases can be collapsed in to a single case by selecting the
    shorter string (if there is one) as your 'start' string. This reduces the
    amount of code you need to write
"""

def one_away(a, b):
    """ See above  """

    N = len(a)
    M = len(b)
    length_distance = abs(N-M)

    # We could do a string comparison up-front to see if strings are matching,
    # but that is an O(n) operation by itself

    if ( length_distance > 1 ):
        return 0    # Lengths differ by more than 1
    elif ( length_distance == 1 ):
        # Check for insertion between shorter and longer string
        shorter = a if N < M else b
        longer = b if M > N else a

        # Count instances of each character found, then compare counts
        long_count = {}
        for c in longer:
            if (long_count.has_key(c)):
                long_count[c] += 1
            else:
                long_count[c] = 1

        # Compare counts against shorter string (subtract)
        for c in shorter:
            if (long_count.has_key(c)):
                long_count[c] -= 1
            else:
                # longer string is missing this character
                #print("missing %s" % c)
                return 0

        dist_one = False
        for k,v in long_count.iteritems():
            # All entries should be zero, with one entry value being 1
            if v == 0:
                pass
            elif v == 1:
                if dist_one == False:
                    dist_one = True
                else:
                    # Multiple new characters in longer string
                    return 0
            else:
                # Multiple unmatched characters
                return 0

        if (dist_one):
            return 1    # Longer string has exactly 1 insertion over shorter string

    elif ( length_distance == 0 ):
        # Check for character swap between strings
        # Same method as above will work, but the end result should be that there
        # is 1 of one character, and -1 of another character

        a_count = {}
        for c in a:
            if (a_count.has_key(c)):
                a_count[c] += 1
            else:
                a_count[c] = 1

        for c in b:
            if (a_count.has_key(c)):
                a_count[c] -= 1
            else:
                a_count[c] = -1

        plus_one = False
        minus_one = False
        for k,v in a_count.iteritems():
            # All entries should be zero, with one entry value being 1, and one being -1
            if v == 0:
                pass
            elif v == 1:
                if plus_one == False:
                    plus_one = True
                else:
                    # Multiple new characters in longer string
                    return 0
            elif v == -1:
                if minus_one == False:
                    minus_one = True
                else:
                    # Multiple missing
                    return 0
            else:
                # Multiple unmatched characters
                return 0

        # If we have fallen through to here, either the strings are one-away, or zero-away
        return 1

# Test cases
x = [('', ''), ('hi', 'hi'), ('pale', 'ple'), ('pales', 'pale'), ('pale', 'bale'), ('pale', 'bake'), ('hello', 'HeLlo'), ('ball', 'fell'), ('ii', 'jj')]
y = [True, True, True, True, True, False, False, False, False]

def run_tests():
    try:
        for i, test_pair in enumerate(x):
            a, b = test_pair
            assert(one_away(a,b) == y[i])

        print("All tests passed")

    except:
        print("Error on test %i (input: %s, %s)" % (i, a, b))
        
