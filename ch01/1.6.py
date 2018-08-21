""" 1.6: Compress

    Scan through the string and keep count of repetition

    O(n) time
"""

def compress(s):

    # Early exit
    N = len(s)
    if (N < 2):
        return s

    run = 1
    prev = s[0]
    compressed = False
    out = ''
    for i in xrange(1, N):
        c = s[i]
        if (c == prev):
            run += 1
        else:
            # Append char and count to out
            out += "%s%i" % (prev, run)

            if (run > 1):
                compressed = True

            run = 1     # new run begins

        prev = c

    # Fall-through: handle the last run
    out += "%s%i" % (prev, run)
    if (run > 1):
        compressed = True

    if (compressed):
        return out
    else:
        return s

def compress_improved(s):
    """ Does not emit '1' for single chars """

    # Early exit
    N = len(s)
    if (N < 2):
        return s

    run = 1
    prev = s[0]
    out = ''
    for i in xrange(1, N):
        c = s[i]
        if (c == prev):
            run += 1
        else:
            # Append char and count to out
            if (run == 1):
                out += prev
            else:
                out += "%s%i" % (prev, run)

            run = 1     # new run begins

        prev = c

    # Fall-through: handle the last run
    if (run == 1):
        out += prev
    else:
        out += "%s%i" % (prev, run)

    return out

# Test cases
x = ['aabcccccaaa', 'hello', 'helllo', 'hellllllo', 'aaa', 'ababababab']
y = ['a2b1c5a3', 'h1e1l2o1', 'h1e1l3o1', 'h1e1l6o1', 'a3', 'ababababab']
y_improved = ['a2bc5a3', 'hel2o', 'hel3o', 'hel6o', 'a3', 'ababababab']

def run_tests():
    try:
        for i, test in enumerate(x):
            assert(compress(test) == y[i])
            assert(compress_improved(test) == y_improved[i])
        print("All tests passed")
    except AssertionError:
        print("Error on test %i (input: %s)" % (i, test))

rt = run_tests
