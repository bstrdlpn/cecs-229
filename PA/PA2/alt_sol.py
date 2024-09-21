def primes(a, b):
    """
    returns a set of all primes in the range
    :param a: int type; lower bound
    :param b: int type; upper bound
    :return: Python set of all primes p satisfying a <= p <= b
    """
    if a > b or a < 1:
        raise ValueError("Invalid range.")
    if a == 1:
        a = 2
    ps = []
    for n in range(a, b+1):
        is_prime = True
        for k in range(2, n):
            if n % k == 0:
                is_prime = False
        if is_prime:
            ps.append(n)
    return set(ps)

def bezout_coeffs(a, b):
    """
    returns the Bezout coefficients of the two
    given integers
    :param a: int type
    :param b: int type
    :return: Python dictionary; keys are the given integers, values are their corresponding Bezout coefficients
    """
    def helper(a, b):
        if a == 0:
            return (0, 1)
        else:
            x, y = helper(b % a, a)
            return (y - (b // a) * x, x)
    return dict(zip([a, b], helper(a, b)))
