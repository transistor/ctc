def urlify_simple(s):
    """ M1) Using built-in Python string methods """

    return s.replace(' ', '%20')

def urlify_scan(s):
    """ M2) Manually scanning from beginning to end, and building a new string """

    processed = ''
    for c in s:
        if (c == ' '):
            processed += '%20'
        else:
            processed += c

    return processed

# Test cases
x = [' ', '  ', 'hi', 'test string', ' start', 'end ', ' one two three ']
y = ['%20', '%20%20', 'hi', 'test%20string', '%20start', 'end%20', '%20one%20two%20three%20']

def run_tests():
    try:
        for i, s in enumerate(x):
           assert(urlify_simple(s) == urlify_scan(s) == y[i])

        print("All tests passed")

    except:
        print("Error on test %i (input: %s)" % (i, s))
