from pa3 import affine_encrypt, affine_decrypt, rsa_encrypt, rsa_decrypt

def test():
    print("Testing Problem 1...")
    expected = 'QXUXMZX'
    received = affine_encrypt('DO NOT GO', 3, 7)

    print(f"Testing affine_encrypt(\"DO NOT GO\", 3, 7)...\n\tExpected: {expected} \n\tReceived: {received}")

    if expected == received:
        print("\tTest PASSED!")
    else:
        print("\tTest FAILED.")
    print("Testing Problem 2...")
    # Write your test cases for Problem 2 here

    print("Testing Problem 3...")
    # Write your test cases for Problem 3 here

    print("Testing Problem 4...")
    # Write your test cases for Problem 4 here
    return




