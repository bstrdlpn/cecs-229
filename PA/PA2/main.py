import random
import math
import pa2
import alt_sol
import your_tester


def main():
    print("Welcome to the PA #2 Tester")

    while True:
        user_in = input(
            "\n" + "-" * 50 +
            "\nWhich problem would you like to test?\n1.  Problem 1: primes(a, b)\n2.  Problem 2: bezout_coeffs(a, "
            "b)\n3.  Problem 3: gcd(a, b)\n4.  Problem 4: mod_inv(a, m)\n5.  Problem 5: solve_mod_equiv(a, b, m, low, "
            "high)\n6.  Run your own tester.\nQ.  Quit\n\nEnter your selection: "
        )
        if user_in == '1':
            print("\n" + "-" * 50 + "\n\nTesting Problem 1...\n\n")
            a = random.randint(1, 60)
            b = random.randint(a + 15, 100)
            expected = alt_sol.primes(a, b)
            received = pa2.primes(a, b)
            print(f"Testing primes({a}, {b})....\nExpected: {expected}\nReceived: {received}")

            if expected == received:
                print("\nTest PASSED!")
            else:
                print("\nTest FAILED.")

        elif user_in == '2':
            print("\n" + "-" * 50 + "\n\nTesting Problem 2...\n\n")
            a = random.randint(1, 60)
            b = random.randint(a + 15, 100)
            expected = alt_sol.bezout_coeffs(a, b)
            received = pa2.bezout_coeffs(a, b)

            print(f"Testing bezout_coeffs({a}, {b})....\nExpected: {expected}\nReceived: {received}")

            if expected == received:
                print("\nTest PASSED!")
            else:
                print("\nTest FAILED.")

        elif user_in == '3':
            print("\n" + "-" * 50 + "\n\nTesting Problem 3...\n\n")
            a = random.randint(-100, 100)
            while a == 0:
                a = random.randint(-100, 100)
            expected = math.gcd(a, a)
            received = pa2.gcd(a, a)

            print(f"Testing gcd({a}, {a})....\n\tExpected: {expected}\n\tReceived: {received}")

            if expected == received:
                print("\tTest PASSED!\n")
            else:
                print("\tTest FAILED.\n")

            possibilities = [-1, 1]
            for i in possibilities:
                for j in possibilities:
                    if i < 0:
                        a = random.randint(-100, -50)
                        while a == 0:
                            a = random.randint(-100, 100)
                    else:
                        a = random.randint(50, 100)
                        while a == 0:
                            a = random.randint(-100, 100)
                    if j < 0:
                        b = random.randint(-100, -50)
                        while b == 0:
                            b = random.randint(-100, 100)
                    else:
                        b = random.randint(-100, -50)
                        while b == 0:
                            b = random.randint(-100, 100)

                    expected = math.gcd(a, b)
                    received = pa2.gcd(a, b)

                    print(f"Testing gcd({a}, {b})....\n\tExpected: {expected}\n\tReceived: {received}")

                    if expected == received:
                        print("\tTest PASSED!\n")
                    else:
                        print("\tTest FAILED.\n")

        elif user_in == '4':
            print("\n" + "-" * 50 + "\n\nTesting Problem 4...\n\n")
            a = random.randint(2, 10)
            m = random.randint(2, 50)
            while pa2.gcd(a, m) != 1:
                a = random.randint(2, 10)
                m = random.randint(2, 50)
            received = pa2.mod_inv(a, m)
            print(f"Testing mod_inv({a}, {m})....\nReceived: {received}")

            if (received * a - 1) % m == 0:
                if 0 < received < m:
                    print(f"{received} * {a} is EQUIVALENT to 1 under modulo {m}.\n\nTest PASSED.")
                else:
                    print(f"{received} * {a} equivalent to 1 under modulo {m} is correct, but {received} is not the "
                          f"range [{low}, {high}].")
            else:
                print(f"{received} * {a} is NOT EQUIVALENT to 1 under modulo {m}.\n\nTest FAILED.")

        elif user_in == '5':
            print("\n" + "-" * 50 + "\n\nTesting Problem 5...\n\n")
            a = random.randint(2, 20)
            m = random.randint(2, 50)
            b = random.randint(-10, 10)
            while pa2.gcd(a, m) != 1:
                a = random.randint(-10, 10)
                m = random.randint(2, 50)

            low = random.randint(-2*m, 0)
            high = low + random.randint(m, 2*m)
            received = pa2.solve_mod_equiv(a, b, m, low, high)
            print(f"Testing solve_mod_equiv({a}, {b}, {m}, {low}, {high})....\n")
            if len(received) == 0:
                print("Received: { }")
            else:
                print("Received:", received)
            for x in received:
                if (a * x - b) % m == 0:
                    if low <= x <= high:
                        print(f"\tx = {x}: {a}*{x} is EQUIVALENT to {b} modulo {m} ==> CORRECT.")
                    else:
                        print(f"\tx = {x}: {a}*{x} is EQUIVALENT to {b} modulo {m} BUT x is NOT IN CORRECT "
                              f"RANGE [{low}, {high}].")
                else:
                    print(f"\tx = {x}: {a}*{x} is NOT EQUIVALENT to {b} modulo {m} ==> INCORRECT.")

        elif user_in == '6':
            print("\n" + "-" * 50 + "\n\nRunning your own tester...\n\n")
            your_tester.test()

        elif user_in.upper() == 'Q':
            break
        else:
            print("Invalid selection.  Please try again.")
    return


if __name__ == "__main__":
    main()
