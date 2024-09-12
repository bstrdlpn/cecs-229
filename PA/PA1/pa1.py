""" ---------------- PROBLEM 1 ----------------"""


def equiv_to(a, m, low, high):
    """
    Returns a list of all integer values x where x is congruent to
    a mod m, within a desired range restriction.

    Parameters:
        'a' : var in definition of congruence a (mod m)
        'm' : var in definition of congruence a (mod m)
        low : inclusive lower bound of inequality restricting range of x_vals
        high: inclusive upper bound of inequlaity restricting range of x_vals

    Returns:
        x_vals : a list containing all values satisifying range(low, high) such
                that x congruent a (mod m) 
    """
    # Generic form of low and high k inequalities
    k_low = (low-a) // m
    k_high = (high-a) // m  
    
    k_vals = list(range(k_low, k_high + 1))
    x_vals = []
    for k in k_vals:
        x = m * k + a
        x_vals.append(x)
    return x_vals


""" ---------------- PROBLEM 2 ----------------"""


def b_rep(n, b):
    digits = []  # stores the digits of the b-representation of n
    q = n
    while q != 0:
        digit = "FIXME: update 'digit' to be the remainder of q divided by b"
        if b == 16 and digit > 9:
            hex_dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
            # FIXME: Update digit = ...
        digits.append(digit)
        q = "FIXME: update q to the correct value."
    return  # FIXME: Return the string of digits


""" ---------------- PROBLEM 3 ----------------"""


def binary_add(a, b):
    # removing all whitespace from the strings
    a = a.replace(' ', '')
    b = b.replace(' ', '')

    # padding the strings with 0's so they are the same length
    if len(a) < len(b):
        diff = len(b) - len(a)
        a = "0" * diff + a
    elif len(a) > len(b):
        diff = len(a) - len(b)
        b = "0" * diff + b

    # addition algorithm
    result = ""
    carry = 0
    for i in reversed(range(len(a))):
        a_i = int(a[i])
        b_i = int(b[i])

        # FIXME: Update result += ....
        # FIXME: Update carry =
    if carry == 1:
        result += "FIXME: Update 'result' to the correct value."
    return  # FIXME return the appropriate string


""" ---------------- PROBLEM 4 ----------------"""


def binary_mul(a, b):
    # removing all whitespace from the strings
    a = a.replace(' ', '')
    b = b.replace(' ', '')

    # multiplication algorithm
    partial_products = []
    i = 0  # index of the current bit of string 'a' beginning at 0, right-to-left
    for bit in reversed(a):
        if bit == '1':
            partial_products.append("FIXME: Append the appropriate partial product")
        i += 1

    result = '0'
    while len(partial_products) > 0:
        result = binary_add("FIXME: Input the correct arguments")
        del partial_products[0]
    return  # FIXME: Return the appropriate result
