import random
import math
import pa3
import your_tester

print("Welcome to the PA #3 Tester")

while True:
    user_in = input(
            "\n" + "-" * 50 +
            "\nWhich problem would you like to test?\n"
            "1.  Problem 1: affine_encrypt(text, a, b)\n"
            "2.  Problem 2: affine_decrypt(cipher, a, b)\n"
            "3.  Problem 3: rsa_encrypt(text, n, e)\n"
            "4.  Problem 4: rsa_decrypt(cipher, p, q, e)\n"
            "5.  Run your own tester.\n"
            "Q.  Quit\n\nEnter your selection: "
    )

    if user_in == '1':
        print("\n" + "-" * 50 + "\n\nTesting Problem 1...\n\n")
        try:
            expected1 = 'INOTTOZZSNKOJ'
            received1 = pa3.affine_encrypt('STOP POLLUTION', 5, 22)
            print(
                    f"Testing affine_encrypt(\"STOP POLLUTION\", 5, 22)....\n\tExpected: {expected1} \n\tReceived: {received1}"
            )

            if expected1 == received1:
                print("\tTest PASSED!")
            else:
                print("\tTest FAILED.")

            expected2 = 'WGVXFCVO'
            received2 = pa3.affine_encrypt("BLACK HAT", 1, -31)
            print(
                    f"\nTesting affine_encrypt(\"BLACK HAT\", 1, -31)....\n\tExpected: {expected2} \n\tReceived: {received2}"
            )

            if expected2 == received2:
                print("\tTest PASSED!")
            else:
                print("\tTest FAILED.")

            print(
                    f"\nTesting affine_encrypt(\"SOME MESSAGE\", 2, 3)...\n\tExpected: ValueError"
            )
        except Exception as e:
            print(f"The following unexpected error occurred:\n{e}")

        try:
            received = pa3.affine_encrypt("SOME MESSAGE", 2, 3)
            print("\tReceived:", received)
            print("\tTest FAILED.")
        except ValueError:
            print("\tRaised ValueError.\n\tTest PASSED!")


    elif user_in == '2':
        print("\n" + "-" * 50 + "\n\nTesting Problem 2...\n\n")

        expected1 = 'STOPPOLLUTION'
        received1 = pa3.affine_decrypt('INOttOZZSnKOJ', 5, 22)
        print(
                f"Testing affine_decrypt('INOttOZZSnKOJ', 5, 22)....\n\tExpected: {expected1} \n\tReceived: {received1}"
        )

        if expected1 == received1:
            print("\tTest PASSED!")
        else:
            print("\tTest FAILED.")

        expected2 = 'BLACKHAT'
        received2 = pa3.affine_decrypt('WGVXFCVO', 1, -31)
        print(
                f"\nTesting affine_decrypt('WGVXFCVO', 1, -31)....\n\tExpected: {expected2} \n\tReceived: {received2}"
        )

        if expected2 == received2:
            print("\tTest PASSED!")
        else:
            print("\tTest FAILED.")

    elif user_in == '3':
        print("\n" + "-" * 50 + "\n\nTesting Problem 3...\n\n")
        texts = ['STOP', 'HELP', 'STOPS', 'REPEAT']
        expected = ['20812182', '09810461', '208121821346', '194319342299']

        for i in range(len(texts)):
            cipher = pa3.rsa_encrypt(texts[i], 2537, 13)
            print(
                    f"Testing encryptRSA({texts[i]}, 2537, 13)\n\tReceived: {cipher}\n\tExpected: {expected[i]}"
            )
            if cipher == expected[i]:
                print("\tTest PASSED!\n")
            else:
                print("\tTest FAILED.\n")

    elif user_in == '4':
        print("\n" + "-" * 50 + "\n\nTesting Problem 4...\n\n")
        expected = ['STOP', 'HELP', 'STOPSX', 'REPEAT']
        ciphers = ['20812182', '09810461', '208121821346', '194319342299']

        for i in range(len(ciphers)):
            text = pa3.rsa_decrypt(ciphers[i], 43, 59, 13)
            print(
                    f"Testing decryptRSA({ciphers[i]}, 43, 59, 13)\n\tReceived: {text}\n\tExpected: {expected[i]}"
            )
            if text == expected[i]:
                print("\tTest PASSED!\n")
            else:
                print("\tTest FAILED.\n")

    elif user_in == '5':
            print("\n" + "-" * 50 + "\n\nRunning your own tester...\n\n")
            your_tester.test()

    elif user_in.upper() == 'Q':
        break
    else:
        print("Invalid selection.  Please try again.")
