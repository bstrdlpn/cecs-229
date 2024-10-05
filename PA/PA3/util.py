def digits2letters(digits):
    """
    converts the string of double-digit numbers to letters using the map
    00 -> A, 01 -> B, ..., 25 -> Z
    :param  digits: str type; string of double-digit numbers in the range 00 - 25
    :return: str type; a string of letters A-Z corresponding to the double-digit numbers
    """
    letters = ""
    start = 0  # initializing starting index of first digit
    while start <= len(digits) - 2:
        digit = digits[start: start + 2]  # accessing the double-digit
        if int(digit) < 26:
            letters += chr(int(digit) + 65)  # concatenating to the string of letters
        start += 2  # updating the starting index for next digit

    return letters


def letters2digits(letters):
    """
    converts the given string of letters to a string of double digits
    using the mapping A -> 00, B - > 01, ..., Z -> 25
    :param letters: str type; the string of letters
    :return: str type; a string of double-digit characters
    """
    digits = ""
    for c in letters:
        if c.isalpha():
            letter = c.upper()  # converting to uppercase
            d = ord(letter) - 65
            if d < 10:
                digits += "0" + str(d)  # concatenating to the string of digits
            else:
                digits += str(d)
    return digits


def blocksize(n):
    """
    returns the size of a block in an RSA encrypted string
    :param n: int type; the modulo in the RSA key (n, e)
    :return: int type; the size of an RSA block of characters
    """
    twofive = "25"
    while int(twofive) < n:
        twofive += "25"
    return len(twofive) - 2
