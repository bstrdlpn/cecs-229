import copy
import math
from structures import Matrix, Vec
""" ----------------- PROBLEM 1 ----------------- """


def norm(v : Vec, p: int):
    """
    returns the p-norm of Vec v
    :param v: Vec type; the Vec object for which the norm will be applied
    :param p: int type; the integer determining the norm to be calculated
    :returns: float type; the norm as a float
    """
    result = 0

    for element in v:
        result += math.pow(abs(element), p)

    result = math.pow(result, 1/p)

    return result
""" ----------------- PROBLEM 2 ----------------- """


def _ref(A : Matrix):
    """
    returns the Row Echelon Form of the Matrix A
    :param A: Matrix type; the matrix A for which to perform Row-Echelon Form
    :returns: Matrix type; distinct Matrix object that is the
              Row-Echelon Form of A
    """
    B = Matrix(copy.deepcopy(A.rows))
    m, n = B.dim()
    k = 1  # initializing the row-index of where to begin searching for the pivot
    for j in range(1, n + 1):
        
        p = _pivot_idx(k, j, B) # gets the index of the pivot at column j
        
        if p is None:
            continue
          
        if p != k: # we must swap row k with row p
            row_k = B.get_row(k)
            row_p = B.get_row(p)

            B.set_row(p, row_k)
            B.set_row(k, row_p)
  
        pivot = B.get_entry(k, j)
        if abs(pivot) > 1e-10:
            new_row = [element / pivot for element in B.get_row(k)]
            B.set_row(k, new_row)
  
        # reducing the rows below row k by a scalar multiple of row k
        for i in range(k + 1, m + 1): 
            scalar = B.get_entry(i, j)
          
            reduced_row = [a - (scalar * b) for a, b in zip(B.get_row(i), B.get_row(k))]
          
            B.set_row(i, reduced_row)
        k += 1
    return B


""" ----------------- PROBLEM 3 ----------------- """


def rank(A : Matrix):
    """
    returns the rank of the given Matrix object
    as an integer
    """
    B = Matrix(copy.deepcopy(A.rows))
    B_ref = _ref(B)
    B_ref = B_ref.get_rows()

    rank = 0
    
    for sublist in B_ref:
        result = 0
        for element in sublist:
            result += element
        if result != 0:
            rank += 1
    
    return rank


""" ----------------- PROBLEM 4 ----------------- """


def gauss_solve(A : Matrix, b : Vec):
    """
    returns the solution to the system Ax = b if the system has a solution. If 
    the system does not have a solution, None is returned. If the system has 
    infinitely-many solutions, the number of free variables as an 'int' is 
    returned.

    :param A:   Matrix type; the matrix of coefficients of the system of equations
    :param b:   Vec object; the vector of constants in the system of equations

    :returns:   
              - None; if the system does not have a solution
              - int type; if the system has infinitely many solutions, the 
                number of free variables is returned
              - Vec type; the vector solution of the system if it has a solution
    """
    # the augmented matrix
    new_cols = copy.deepcopy(A.cols)
    new_cols.append(b.elements)
    Ag = Matrix(new_cols).transpose()

    # ranks of A and Ag
    Arank = rank(A)
    Agrank = rank(Ag)
    m, n = A.dim()

    if Arank != Agrank: # no solution
        return None
    elif Arank < n: # infinitely many solutions
        # number of free variables = num of cols in A - Arank
        return n - Arank
    else: # unique solution, return type 'Vec'
        Ag_ref = _ref(Ag)

        solution = [0] * n

        # back sub
        for i in range(n, 0, -1):
            row_index = i - 1
            rhs = Ag_ref.get_entry(i, n + 1)

            for j in range(i + 1, n + 1):
                col_index = j - 1
                rhs -= Ag_ref.get_entry(i, j) * solution[col_index]

            solution[row_index] = rhs / Ag_ref.get_entry(i, i)

        return Vec(solution)
    



""" ----------------- PROBLEM 5 ----------------- """


def gram_schmidt(S : set):
    """
    returns the orthonormal basis of given set S
    :param S: set type; a set of linearly independent 'Vec' objects
    :returns: an orthonormal set of 'Vec' objects
    """
    # TODO: Implement this function
    pass


""" ----------------- HELPER METHOD ----------------- """

def _pivot_idx(i: int, j: int, A: Matrix):
    """
    finds the row index >= i of the first non-zero entry
    in column j of the given Matrix.  If no non-zero entry
    exists in column j at or after row i, then None is returned.
    :param i: int type; the row index of where to begin search
    :param j: int type; the column index of where to begin search
    :param A: Matrix type; the matrix of interest
    :return: int type or None type; if int, the row index of the
             first non-zero entry in column j.
    """
    column = A.get_col(j)
    for k in range(i - 1, len(column)):
        if abs(column[k]) > 1E-6:
            return k + 1
        else:
            A.set_entry(k, j, 0)
    return None