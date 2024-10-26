import math

""" ----------------- PROBLEM 1 ----------------- """


def translate(S, z0):
    """
    translates the complex numbers of set S by z0
    :param S: set type; a set of complex numbers
    :param z0: complex type; a complex number
    :return: set type; a set consisting of points in S translated by z0
    """
    translated_set = {z + z0 for z in S}
    return translated_set


""" ----------------- PROBLEM 2 ----------------- """


def scale(S, k):
    """
    scales the complex numbers of set S by k.
    :param S: set type; a set of complex numbers
    :param k: float type; positive real number
    :return: set type; a set consisting of points in S scaled by k
    :raise: raises ValueError if k <= 0
    """
    if k <= 0:
        raise ValueError("k can not be <= 0")

    scaled_set = {k * z for z in S}

    return scaled_set

""" ----------------- PROBLEM 3 ----------------- """


def rotate(S, tau):
    """
    rotates the complex numbers of set S by tau radians.
    :param S: set type; - set of complex numbers
    :param tau: float type; radian measure of the rotation value.
                If negative, the rotation is clockwise.
                If positive the rotation is counterclockwise.
                If zero, no rotation.
    :returns: set type; a set consisting of points in S rotated by tau radians
    """
    #rotate_by = numpy.exp(1j * float(tau))
    rotate_by = math.exp(tau)**1j
    rotated_set = {complex(round((z * rotate_by).real, 2),
    round((z * rotate_by).imag, 2)) for z in S}

    return rotated_set


""" ----------------- PROBLEM 4 ----------------- """


class Vec:
    def __init__(self, contents=[]):
        """
        Constructor defaults to empty vector
        :param contents: list type; list of elements to initialize a vector
        object, defaults to empty list
        """
        self.elements = contents
        return

    def __abs__(self):
        """
        Overloads the built-in function abs(v)
        :returns: float type; the Euclidean norm of vector v
        """
        total = 0

        for x in self.elements:
            total += x**2

        euclidean_norm = math.sqrt(total)

        return euclidean_norm

    def __add__(self, other):
        """
        overloads the + operator to support Vec + Vec
        :raises: ValueError if vectors are not same length
        :returns: Vec type; a Vec object that is the sum vector of this Vec and
        'other' Vec
        """
        if len(self.elements) != len(other.elements):
            raise ValueError("Vectors are not the same length.")
        else:
            vector_sum = Vec([u + v for u, v in zip(self.elements, other.elements)])

        return vector_sum

    def __sub__(self, other):
        """
        overloads the - operator to support Vec - Vec
        :raises: ValueError if vectors are not same length
        :returns: Vec type; a Vec object that is the difference vector of this
        Vec and 'other' Vec
        """
        if len(self.elements) != len(other.elements):
            raise ValueError("Vectors are not the same length.")
        else:
            vector_diff = Vec([u -v for u, v in zip(self.elements, other.elements)])

        return vector_diff

    def __mul__(self, other):
        """
        Overloads the * operator to support
          - Vec * Vec (dot product) raises ValueError if vectors are not
            same length in the case of dot product; returns scalar
          - Vec * float (component-wise product); returns Vec object
          - Vec * int (component-wise product); returns Vec object
        """
        if type(other) == Vec:  # define dot product
            if len(self.elements) != len(other.elements):
                raise ValueError("Vectors are not the same length.")
            else:
                return sum(u * v for u, v in zip(self.elements, other.elements))

        elif type(other) == float or type(other) == int:  # scalar-vector multiplication
            scalar = Vec([other * u for u in self.elements])

            return scalar

    def __rmul__(self, other):
        """
        Overloads the * operation to support
              - float * Vec; returns Vec object
              - int * Vec; returns Vec object
        """
        if isinstance(other, (int, float)):
            return Vec([other * u for u in self.elements])

    def __str__(self):
        """returns string representation of this Vec object"""
        return str(self.elements)  # does NOT need further implementation
