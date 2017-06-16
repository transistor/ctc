""" Zero Matrix

    Approach: Create a duplicate of the input matrix, then scan the
    input for zeroes. For each zero encountered, zero-out the
    corresponding row and column in the output matrix.

    It is possible to do this in-place while maintaining a history of
    rows and columns that have been zeroed-out, but it is much cleaner
    to use a duplicate matrix

    If you want to do it in-place, perform an initial pass to find all
    zeroes. Then, iterate over the zeroes you've found, and zero-out
    the corresponding rows and columns.
"""

def zero_matrix(m):
    """ Matrix representation will be in the form of a list of lists  """

    # Create duplicate matrix (assume that matrix is valid in structure)
    N = len(m)
    M = len(m[0])

    # Deep copy
    zeroed = []
    for i, row in enumerate(m):
        row_copy = []
        for j, col in enumerate(row):
            row_copy.append(m[i][j])
        zeroed.append(row_copy)

    # Scan through matrix to find zeroes and then zero-out
    for i, row in enumerate(m):
        for j, col in enumerate(row):
            if (m[i][j] == 0):
                # Zero-out row i and column j in duplicate matrix
                # length of rows: M (= number of columns)
                # height of columns: N (= number of rows)
                
                for idx in xrange(M):
                    zeroed[i][idx] = 0       # Zero-out row

                for idx in xrange(N):
                    zeroed[idx][j] = 0       # Zero-out column

    #print("Zeroed:")
    #for row in zeroed:
    #    print row

    return zeroed

zm = zero_matrix

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

def run_tests():
    try:
        for i, m in enumerate(x):
           assert(zero_matrix(m) == y[i])

        print("All tests passed")
    except:
        print("Error on test %i (input: %r)" % (i, m))
