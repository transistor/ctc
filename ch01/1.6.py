""" Scan through the string and keep count of repetition

    O(n) time
"""

def compress(s):
    """ See above  """

    N = len(s)

    if (N < 3):
        return s    # No compression possible

    # Maintain entries as 2-tuples: (char, count)
    counts = []

    prev = s[0]
    count = 1
    for c in s[1:]:
        if (prev == c):
            count += 1
        else:
            # Track the last run, then start a new one
            counts.append( (prev, count) )
            prev = c
            count = 1

    # Careful: if there is a run of repeated characters at the end,
    # they will not have been added to counts
    counts.append( (prev, count) )

    # Create compressed string:
    compressed = ''
    for c, n in counts:
        compressed += '%s%s' % (c, str(n))

    M = len(compressed)
    if (N <= M):
        return s
    else:
        return compressed

# Test cases
x = ['aabcccccaaa', 'hello', 'helllo', 'hellllllo', 'aaa', 'ababababab', '', '  ', '   ', ]
y = ['a2b1c5a3', 'hello', 'helllo', 'h1e1l6o1', 'a3', 'ababababab', '', '  ', ' 3', ]

def run_tests():
    try:
        for i, test in enumerate(x):
            assert(compress(test) == y[i])

        print("All tests passed")

    except:
        print("Error on test %i (input: %s)" % (i, test))
        
