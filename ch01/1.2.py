# Note: Do not mistakes rotations and permutations. Rotations *are* permutations,
#       but there are more permutations than rotations for inputs of length >= 3
#
#   'hello', 'elhol'    -- permutations
#   'hello', 'lohel'    -- simple rotation (which is also a permutation)

def check_permutations_sets(a, b):
    """ M1) Convert each string to sets, then compare sets """

    # Testing the length is essential for this approach
    if (len(a) != len(b)):
        return 0        # Uneven length => not permutations

    if (set(a) == set(b)):
        return 1
    else:
        return 0

def check_permutations_sort(a,b):
    """ M2) Sort each string, then compare from beginning to end

            O(N) on the linear comparison, plus O(sort) for the sorting,
            plus O(N) on the string explode
    """

    if (len(a) != len(b)):
        return 0 

    asplit = [c for c in a]
    bsplit = [c for c in b]
    asplit.sort()
    bsplit.sort()

    N = len(a)
    for i in xrange(N):
        if (asplit[i] != bsplit[i]):
            return 0

    return 1    # All characters matched


# Test cases
x = [('', ''), ('  ', '  '), ('A', 'A'), ('hi', 'ih'), ('Hello', 'loHel'), ('hello', 'jello'), ('spin', 'twin')]
y = [True, True, True, True, True, False, False]

def run_tests():
    try:
        for i, test_pair in enumerate(x):
            a,b = test_pair
            assert(check_permutations_sets(a,b) == y[i])
            assert(check_permutations_sort(a,b) == y[i])

        print("All tests passed")
    except:
        print("Error on test %i (input: %s, %s)" % (i, a, b))

