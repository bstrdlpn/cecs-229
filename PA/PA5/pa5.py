from Vec import Vec

"""-------------------- PROBLEM 1 --------------------"""
class Matrix:

    def __init__(self, rows):
        """
        initializes a Matrix with given rows
        :param rows: the list of rows that this Matrix object has
        """
        self.rows = rows
        self.cols = []
        self._construct_cols()
        return

    """
  INSERT MISSING SETTERS AND GETTERS HERE
  """
    # Setters
    def set_row(self, i, new_row):
        """
        Change the i-th row to be the list new_row and reconstruct the internal
        column list.

        :raises: ValueError; if new_row != matrix row length
        """
        index = i - 1
        row_elements = len(self.rows[0])
        if len(new_row) != row_elements:
            raise ValueError("Incompatible row length.")
        else:
            self.rows[index] = new_row
            self._construct_cols()

    def set_col(self, j, new_col):
        """
        Change the j-th column to be the list new_col, and reconstruct the 
        internal rows list.

        :raises: ValueError; if new_col != matrix col length
        """
        index = j - 1
        col_elements = len(self.rows)
        if len(new_col) != col_elements:
            raise ValueError("Incompatible column length.")
        else:
            self.cols[index] = new_col
            self._construct_rows()

    def set_entry(self, i, j, val):
        """
        Change the existing a_{ij} entry in the matrix to val.

        :param i: int; index of row, indexed at 1
        :param j: int; index of col, indexed at 1

        :raises: IndexError; if i does not satisfy 1<=i<=m or j does not satisfy
        1<=j<=n where m = num rows and n = num cols
        """
        num_rows = len(self.get_rows())
        num_cols = len(self.get_columns())
        index_row = i - 1
        index_col = j - 1

        if not (1 <= i <= num_rows) or not (1 <=j <= num_cols):
            raise IndexError
        else:
            self.rows[index_row][index_col] = val
            self._construct_cols()

    # Getters
    def get_row(self, i):
        """
        Return the i-th row as a list.

        :param i: int; index of row, start indexed at 1
        :raises: IndexError if i does not satisfy 1<=i<=m
        :return: list; row[i-1]
        """
        #if 1 <= i < len(self.rows):
            #raise IndexError(f"i does not satisfy range 1<={i}<={len(self.rows)}")
        return self.rows[i-1]

    def get_col(self, j):
        """
        Return the j-th column as a list.

        :param j: int; index of col, start indexed at 1
        :raises: IndexError if j does not satisfy 1<=j<=n
        :return: list; col[j-1]
        """
        #if 1 <= j <= len(self.cols):
            #raise IndexError(f"j does not satisfy range 1<={j}<={len(self.cols)}")
        return self.cols[j-1]

    def get_rows(self):
        """Return the list of lists that are the rows of the matrix obj."""
        return self.rows
    
    def get_columns(self):
        """Return the list of lists that are the columns of the matrix obj."""
        return self.cols

    def get_diag(self, k):
        """
        Return the k-th diagonal of a matrix where k=0 returns the main 
        diagonal, k>0 returns the diagonal beginning at a_{1(k+1)} and k<0 
        returns the diagonal beginning at a_{(-k+1)1}. eg. get_diag(1) for an 
        nxn matrix returns [a_{12},a_{23},a_{34},...,a_{(n-1)n}]

        :param k: int; increments or decrements start index for diagonal
        """
        diag_list = []
        num_rows = len(self.get_rows())
        num_cols = len(self.get_columns())

        if k >= 0:
            for row_index in range(num_rows):
                col_index = row_index + k
                if col_index < num_cols:
                    diag_list.append(self.rows[row_index][col_index])
        else:
            # values of k < 0
            for col_index in range(num_cols):
                row_index = col_index - k
                if row_index < num_rows:
                    diag_list.append(self.rows[row_index][col_index])

        return diag_list


    def get_entry(self, i, j):
        return self.rows[i-1][j-1]

    def _construct_cols(self):
        """
        HELPER METHOD: Resets the columns according to the existing rows
        """
        
        """
        self.cols = []
        cols_list = []
        
        # number of rows in the new columns list
        num_rows = len(self.rows[0])
        
        for col_index in range(num_rows):
            new_col = []
            for row in self.rows:
                new_col.append(row[col_index])
            cols_list.append(new_col)

        self.cols = cols_list
       """
        self.cols = []
        transpose = [list(row) for row in zip(*self.rows)]
       
        self.cols = transpose

    def _construct_rows(self):
        """
        HELPER METHOD: Resets the rows according to the existing columns
        """
        self.rows = []
        transpose = [list(row) for row in zip(*self.cols)]

        self.rows = transpose

    def __add__(self, other):
        """
        overloads the + operator to support Matrix + Matrix
        :param other: the other Matrix object
        :raises: ValueError if the Matrix objects have mismatching dimensions
        :raises: TypeError if other is not of Matrix type
        :return: Matrix type; the Matrix object resulting from the Matrix + Matrix operation
        """
        # type check
        if not isinstance(other, type(self)):
            raise TypeError("Object not a matrix.")
        
        # matrix dimensions
        self_m = len(self.get_rows())
        self_n = len(self.get_columns())
        other_m = len(other.get_rows())
        other_n = len(other.get_columns())

        # dimension check
        if (self_m, self_n) != (other_m, other_n):
            raise ValueError("Incompatible dimensions.")
        
        result = [[self.rows[i][j] + other.rows[i][j] for j in range(self_n)] for i in range(self_m)]
        
        return type(self)(result)

    def __sub__(self, other):
        """
        overloads the - operator to support Matrix - Matrix
        :param other:
        :raises: ValueError if the Matrix objects have mismatching dimensions
        :raises: TypeError if other is not of Matrix type
        :return: Matrix type; the Matrix object resulting from Matrix - Matrix operation
        """
        # type check
        if not isinstance(other, type(self)):
            raise TypeError("Object not a matrix.")

        # matrix dimensions
        self_m = len(self.get_rows())
        self_n = len(self.get_columns())
        other_m = len(other.get_rows())
        other_n = len(other.get_columns())

        if (self_m, self_n) != (other_m, other_n):
            raise ValueError("Incompatible dimensions.")

        result = [[self.rows[i][j] - other.rows[i][j] for j in range(self_n)] for i in range(self_m)]

        return type(self)(result)

    def __mul__(self, other):
        """
        overloads the * operator to support
            - Matrix * Matrix
            - Matrix * Vec
            - Matrix * float
            - Matrix * int
        :param other: the other Matrix object
        :raises: ValueError if the Matrix objects have mismatching dimensions
        :raises: TypeError if other is not of Matrix type
        :return: Matrix type; the Matrix object resulting from the Matrix + Matrix operation
        """
        if isinstance(other, (int, float)):
            # MATRIX-SCALAR multiplication
            self_m = len(self.rows)
            self_n = len(self.rows[0])

            result = [[round(self.rows[i][j] * other, 1) for j in range(self_n)] for i in range(self_m)]

            return type(self)(result)

        elif isinstance(other, Matrix):
            # MATRIX-MATRIX multiplication
            # dimensions of matrices
            self_m = len(self.get_rows())
            self_k = len(self.get_columns())
            other_k = len(other.get_rows())
            other_n = len(other.get_columns())

            # check matrix dimensions
            if self_k != other_k:
                raise ValueError("Matrix dimensions are incompatible.")
            
            # initialize empty matrix with dimensions (self_m x other_n)
            result = [[0 for _ in range(other_n)] for _ in range(self_m)]
            
            for i in range(self_m):
                for j in range(other_n):
                    for k in range(self_k):
                        result[i][j] += self.rows[i][k] * other.rows[k][j]
            
            return type(self)(result)

        elif isinstance(other, Vec):
            # dimensions of matrices
            self_m = len(self.get_rows())
            self_n = len(self.get_columns())
            other_n = len(other)

            if self_n != other_n:
                raise ValueError("Matrix dimensions are incompatible.")

            # initialize empty matrix with dimensions (self_m x 1)
            result = [0 for _ in range(self_m)]

            for i in range(self_m):
                for j in range(other_n):
                    result[i] = sum(self.rows[i][j] * other[j] for j in range(other_n))

            return Vec(result)
            
        else:
            raise TypeError(f"Matrix * {type(other)} is not supported.")
        return

    def __rmul__(self, other):
        """
        overloads the * operator to support
            - float * Matrix
            - int * Matrix
        :param other: the other Matrix object
        :raises: ValueError if the Matrix objects have mismatching dimensions
        :raises: TypeError if other is not of Matrix type
        :return: Matrix type; the Matrix object resulting from the Matrix + Matrix operation
        """
        if isinstance(other, (int, float)):
            # MATRIX-SCALAR
            return self.__mul__(other)
        else:
            raise TypeError(f"{type(other)} * Matrix is not supported.")
        return

    '''-------- ALL METHODS BELOW THIS LINE ARE FULLY IMPLEMENTED -------'''

    def dim(self):
        """
        gets the dimensions of the mxn matrix
        where m = number of rows, n = number of columns
        :return: tuple type; (m, n)
        """
        m = len(self.rows)
        n = len(self.cols)
        return (m, n)

    def __str__(self):
        """prints the rows and columns in matrix form """
        mat_str = ""
        for row in self.rows:
            mat_str += str(row) + "\n"
        return mat_str

    def __eq__(self, other):
        """
        overloads the == operator to return True if
        two Matrix objects have the same row space and column space
        """
        if type(other) != Matrix:
            return False
        this_rows = [round(x, 3) for x in self.rows]
        other_rows = [round(x, 3) for x in other.rows]
        this_cols = [round(x, 3) for x in self.cols]
        other_cols = [round(x, 3) for x in other.cols]

        return this_rows == other_rows and this_cols == other_cols

    def __req__(self, other):
        """
        overloads the == operator to return True if
        two Matrix objects have the same row space and column space
        """
        if type(other) != Matrix:
            return False
        this_rows = [round(x, 3) for x in self.rows]
        other_rows = [round(x, 3) for x in other.rows]
        this_cols = [round(x, 3) for x in self.cols]
        other_cols = [round(x, 3) for x in other.cols]

        return this_rows == other_rows and this_cols == other_cols


"""-------------------- PROBLEM 2 --------------------"""


def rotate_2Dvec(v: Vec, tau: float):
    """
    computes the 2D-vector that results from rotating the given vector
    by the given number of radians
    :param v: Vec type; the vector to rotate
    :param tau: float type; the radians to rotate by
    :return: Vec type; the rotated vector
    """
    pass  # FIXME: REPLACE WITH IMPLEMENTATION
