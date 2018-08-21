""" Zero Matrix

    M1) Scan the matrix and save the x,y coordinates of each zero in separate
        sets. Use the two sets to zero-out rows and columns, accordingly.

    M2) An in-place approach is to find and mark zeroes with an identifying
        value (e.g.: '@'), and then using a second pass to zero-out rows and 
        columns based on the @.

        Careful: when zeroing-out a row/column, any @ element cannot be
        converted to zero. The @ characters are only switched to zero when they
        are being used to zero-out a row/column.
"""

def zero_set(m):
    """ M1 """

    row_zeroes, col_zeroes = set(), set()

    rows = len(m)
    cols = len(m[0])

    # Find zeroes
    for i in xrange(rows):
        for j in xrange(cols):
            if m[i][j] == 0:
                row_zeroes.add(i)
                col_zeroes.add(j)

    # Zero-out rows/cols
    for row in row_zeroes:
        for j in xrange(cols):
            m[row][j] = 0

    for col in col_zeroes:
        for i in xrange(rows):
            m[i][col] = 0

    return m

def zero_flip(m):
    """ M2 """

    rows = len(m)
    cols = len(m[0])

    # Find zeroes
    for i in xrange(rows):
        for j in xrange(cols):
            if m[i][j] == 0:
                m[i][j] = '@'      # Identifying character

    # Zero-out rows/cols
    for i in xrange(rows):
        for j in xrange(cols):
            if m[i][j] == '@':
                # Zero-out the '@' itself
                m[i][j] = 0

                # Zero-out the row and column (ignoring other '@' chars)
                for c in xrange(cols):              # Zero-out row
                    if m[i][c] != '@':
                        m[i][c] = 0

                for r in xrange(rows):              # Zero-out column
                    if m[r][j] != '@':
                        m[r][j] = 0 

    return m

zs = zero_set
zf = zero_flip

# Test cases
x = [ [[1,2,3], [4,5,6], [7,8,9]],
      [[0,2,3], [4,5,6], [7,8,9]],
      [[1,0,3], [4,5,6], [7,8,9]],
      [[1,2,3], [4,5,0], [7,8,9]],
      [[1,2,3], [4,5,6], [7,8,0]],
      [[1]],
      [[0]],
      [[1,1,1,0,1,1]],
      [[1], [1], [1], [0], [1], [1]],
      [[1,2,3], [4, 0, 6]],
      [[1,2], [3,0], [5,6]],
    ]
y = [ [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
      [[0, 0, 0], [0, 5, 6], [0, 8, 9]],
      [[0, 0, 0], [4, 0, 6], [7, 0, 9]],
      [[1, 2, 0], [0, 0, 0], [7, 8, 0]],
      [[1, 2, 0], [4, 5, 0], [0, 0, 0]],
      [[1]],
      [[0]], 
      [[0, 0, 0, 0, 0, 0]],
      [[0], [0], [0], [0], [0], [0]], 
      [[1, 0, 3], [0, 0, 0]],
      [[1, 0], [0, 0], [5, 0]]
    ]

# Note: run_tests() will modify the inputs in-place, so the tests can only be
#       run once
def run_tests():
    for i, m in enumerate(x):
        # Need a deep-copy of the inputs for the sake of test
        mcopy = [e[:] for e in m]
        zero_set(mcopy)
        try:
            assert(mcopy == y[i])
        except AssertionError:
            print("zero_set(): Error on test %i (input: %r)" % (i, m))

        mcopy = [e[:] for e in m]
        zero_flip(mcopy)
        try:
            assert(mcopy == y[i])
        except AssertionError:
            print("zero_flip(): Error on test %i (input: %r)" % (i, m))

    print("All tests passed")

rt = run_tests


