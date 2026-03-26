import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    A = np.array(A)
    (i,j) = A.shape
    ans = np.zeros((j,i))

    for a in range (j):
        for b in range (i):
            ans[a][b] = A[b][a]

    return ans