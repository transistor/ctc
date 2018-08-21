""" 1.3: URLify """

def urlify(s):
    """ Two-pointer solution

        Start both pointers at the end of the string. One represents the
        write head, the other is the read head. The read head advances until
        it finds the first character. Upon finding the first char, it is 
        written at the write head. At this point, the write head will always
        have something to write (based on what is found at the read head),
        and, now, also advances toward the beginning of the string.

        If the read head encounters a space, then the write head will insert
        the '%20' replacement characters (3 chars), and take 3 steps
        toward the head.

        Note: This assumes the input string never ends with a blank space
        (i.e.: all blank space at the end of the string is padding for the
        insertion of replacement chars). This also means the code will not
        handle a single, blank char as the 'real' input string:

            in = '   '
                  ^-------- real space character input
                   ^^------ padding for replacement
    """

    N = len(s)
    read = write = N-1
    splitted = list(s)

    found_first_char = False
    while (read >= 0):
        # Advance read head to first character
        if not found_first_char:
            if (splitted[read] == ' '):
                read -= 1
                continue
            else:
                found_first_char = True

        # Handle char or blank space accordingly
        if (splitted[read] == ' '):
            splitted[write-2:write+1] = '%20'
            write -= 3
        else:
            splitted[write] = splitted[read]
            write -= 1

        read -= 1

    return ''.join(splitted)

# Test cases
x = ['hi', 'test string  ', 'one two three    ']
y = ['hi', 'test%20string', 'one%20two%20three']

# Space at start of input
start_x = ' start  '
start_y = '%20start'

x.append(start_x)
y.append(start_y)

def run_tests():
    try:
        for i, s in enumerate(x):
           assert(urlify(s) == y[i])

        print("All tests passed")
    except AssertionError:
        print("Error on test %i (input: %s)" % (i, x[i]))
        print("Expected: %s, Actual: %s" % (y[i], urlify_scan(x[i])))

rt = run_tests
