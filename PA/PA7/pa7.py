from helpers import gram_schmidt
from structures import Vec, Matrix
import numpy as np
import cmath


# ----------------------- PROBLEM 1 ----------------------- #
def qr_solve(A: Matrix, b: Vec):
    """
    Solves the system of equations Ax = b by using the
    QR factorization of Matrix A
    :param A: Matrix of coefficients of the system
    :param b: Vec of constants
    :return:  Vec solution to the system
    """
    # Constructing U
    # U should be the set of orthonormal vectors returned
    # by applying Gram-Schmidt Process to the columns of A
    U = gram_schmidt(A.cols)
    n = len(U)

    # Constructing Q
    # Q should be the matrix whose columns are the elements
    # of the vector in set U
    Q = Matrix([[None for j in range(n)] for i in range(n)])
    for j in range(n):
        Q.set_col(j, U[j])

    # Constructing R
    R = Matrix([[0 for j in range(n)] for i in range(n)])
    for j in range(n):
        for i in range(n):
            if i <= j:
                pass

    # Constructing the solution vector x
    b_star = Q.transpose() * b
    x = [None for i in range(n)]
    # FIXME: find the components of the solution vector
    #        and replace them into elements of x
    return Vec(x)


# ----------------------- PROBLEM 2 ----------------------- #
def _submatrix(A: Matrix, i: int, j: int):
    """
    constructs the sub-matrix of an mxn Matrix A that
    results from omitting the i-th row and j-th column;
    i and j satisfy that 0 <= i <= m, and 0 <= j <= n
    :param A: Matrix object
    :param i: int index of row to omit
    :param j: int index of column to omit
    :return: Matrix object representing the sub-matrix
    """
    m, n = A.dim()
    pass  # FIXME: Implement this function


# ----------------------- PROBLEM 3 ----------------------- #
def determinant(A: Matrix):
    """
    computes the determinant of square Matrix A;
    Raises ValueError if A is not a square matrix.
    :param A: Matrix object
    :return: float value of determinant
    """
    m, n = A.dim()
    if m != n:
        raise ValueError(
            f"Determinant is not defined for Matrix with dimension {m}x{n}.  Matrix must be square."
        )
    if n == 1:
        return None  # FIXME: Return the correct value
    elif n == 2:
        return None  # FIXME: Return the correct value
    else:
        d = 0
        # FIXME: Update d so that it holds the determinant
        #        of the matrix.  HINT: You should apply a
        #        recursive call to determinant()
        return d


# ----------------------- PROBLEM 4 ----------------------- #
def eigen_wrapper(A: Matrix):
    """
    uses numpy.linalg.eig() to create a dictionary with
    eigenvalues of Matrix A as keys, and their corresponding
    list of eigenvectors as values.
    :param A: Matrix object
    :return: Python dictionary where keys are eigenvalues of type 'float' or 'complex' and values eigenvectors of type 'Vec'
    """
    pass  # FIXME: Implement this function


# ----------------------- PROBLEM 5 ----------------------- #
def svd(A: Matrix):
    """
    computes the singular value decomposition of Matrix A;
    returns Matrix objects U, Sigma, and V such that:
    1. V is the Matrix whose columns are eigenvectors of 
        A.transpose() * A
    2. Sigma is a diagonal Matrix of singular values of 
        A.transpose() * A appearing in descending order along 
        the main diagonal
    3. U is the Matrix whose j-th column uj satisfies 
        A * vj = sigma_j * uj where sigma_j is the j-th singular 
        value in decreasing order and vj is the j-th column vector of V
    4. A = U * Sigma * V.transpose()
    :param A: Matrix object
    :return: tuple with Matrix objects; (U, Sigma, V)
    """
    m, n = A.dim()
    aTa = A.transpose() * A
    eigen = eigen_wrapper(aTa)
    eigenvalues = np.sort_complex(list(eigen.keys())).tolist()[::-1]

    # Constructing V
    # V should be the mxm matrix whose columns
    # are the eigenvectors of matrix A.transpose() * A
    V = Matrix([[None for j in range(n)] for i in range(n)])
    for j in range(1, n + 1):
        pass  # FIXME: Replace this with the lines that will
        #        correctly build the entries of V

    # Constructing Sigma
    # Sigma should be the mxn matrix of singular values.
    singular_values = None  # FIXME: Replace this so that singular_values
    #        holds a list of singular values of A
    #        in decreasing order
    Sigma = Matrix([[0 for j in range(n)] for i in range(m)])
    for i in range(1, m + 1):
        pass  # FIXME: Replace this with the lines that will correctly
        #        build the entries of Sigma

    # Constructing U
    # U should be the matrix whose j-th column is given by
    # A * vj / sj where vj is the j-th eigenvector of A.transpose() * A
    # and sj is the corresponding j-th singular value
    U = Matrix([[None for j in range(m)] for i in range(m)])
    for j in range(1, m + 1):
        pass  # FIXME: Replace this with the lines that will
        #        correctly build the entries of U
    return (U, Sigma, V)
