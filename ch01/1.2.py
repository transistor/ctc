""" 1.2: Check Permutation """

# Note: Do not mistakes rotations and permutations. Rotations *are* 
#       permutations, but there are more permutations than rotations for inputs 
#       of length >= 3
#
#   'hello', 'elhol'    -- permutations
#   'hello', 'lohel'    -- simple rotation (which is also a permutation)

def check_permutations_sets(a, b):
    """ M1) Count frequency of each character in 'a', then subtract each
            character in 'b'. If there is a decrement from zero, we can exit
            early. If the frequency count isn't all zero at the end, the
            strings are not permutations
    """
    freq = {}
    for c in a:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1

    for c in b:
        if (c not in freq) or (freq[c] == 0):
            # Cannot subtract from zero (b has more of this char than a)
            return False
        else:
            freq[c] -= 1

    # Ensure all vals in dict are zero
    for v in freq.values():
        if (v != 0):
            return False

    return True

def check_permutations_sort(a,b):
    """ M2) Sort each string, then compare from beginning to end

            O(N) on the linear comparison, plus O(sort) for the sorting,
            plus O(N) on the string explode
    """

    return bool(sorted(a) == sorted(b))

# Test cases
x = [('', ''), ('  ', '  '), ('A', 'A'), ('hi', 'ih'), ('Hello', 'loHel'), ('hello', 'jello'), ('spin', 'twin'), ('aaabc', 'abbbc')]
y = [True, True, True, True, True, False, False, False]

def run_tests():
    try:
        for i, test_pair in enumerate(x):
            a,b = test_pair
            assert(check_permutations_sets(a,b) == y[i])
            assert(check_permutations_sort(a,b) == y[i])

        print("All tests passed")
    except AssertionError:
        print("Error on test %i (input: %s, %s)" % (i, a, b))

rt = run_tests
