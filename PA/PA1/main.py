import random
import sys
from pa1 import equiv_to
from pa1 import b_rep
from pa1 import binary_add
from pa1 import binary_mul
import your_tester


def main():
  print("Welcome to the PA #1 Tester")

  while True:
    user_in = input(
      "\n" + "-" * 50 +
      "\nWhich problem would you like to test?\n1.  Problem 1: equiv_to(a, m, low, high)\n2.  Problem 2: b_rep(n, b)\n3.  Problem 3: binary_add(a, b)\n4.  Problem 4: binary_mul(a, b)\n5.  Run your own tester.\nQ.  Quit\n\nEnter your selection: "
    )
    if user_in == '1':
      print("\n" + "-" * 50 + "\n\nTesting Problem 1...\n\n")
      a = random.randint(-20, 20)
      m = random.randint(4, 15)
      low = random.randint(-30, 30)
      high = random.randint(low + 10, low + 20)

      x_vals = equiv_to(a, m, low, high)
      print(
        f"Range [{low}, {high}], equivalent to {a} under modulo {m}...\nReturned: {x_vals}"
      )

      print("\nChecking the correctness of the returned values...")
      for x in x_vals:
        is_correct = (x - a) % m == 0
        print(
          f"\nReturned value: {x}\n\t\tIs {x} equivalent to {a} under modulo {m}?"
        )
        if is_correct:
          print(f"\t\t\tYes, {x} is divisible by {m}")
          if x <= high and x >= low:
            print(
              f"\n\t\tIs {x} in the range [{low}, {high}]?\n\t\t\t\tYes.  Test passed!"
            )
          else:
            print(
              f"\n\t\tIs {x} in the range [{low}, {high}]?\n\t\t\tNo.  Test failed."
            )
        else:
          print(f"which is not divisible by {m}  Test failed.")

    elif user_in == '2':
      print("\n" + "-" * 50 + "\n\nTesting Problem 2...\n\n")
      a = random.randint(10, 50)
      print(f"Decimal integer: {a}")
      expected2 = bin(a)[2:]
      returned2 = b_rep(a, 2)

      expected8 = oct(a)[2:]
      returned8 = b_rep(a, 8)
      expected16 = hex(a)[2:].upper()
      returned16 = b_rep(a, 16)

      print()
      print("%-20s %-20s%10s%-20s%-20s" %
            ('b-representation', 'Returned Value', ' ', 'Expected Value',
             'Test Passed?'))
      print("%-20s %-20s%10s%-20s%-15s" % ('2-representation', returned2, ' ',
                                           expected2, returned2 == expected2))
      print("%-20s %-20s%10s%-20s%-15s" % ('8-representation', returned8, ' ',
                                           expected8, returned8 == expected8))
      print("%-20s %-20s%10s%-20s%-15s" %
            ('16-representation', returned16, ' ', expected16, returned16
             == expected16))

    elif user_in == '3':
      print("\n" + "-" * 50 + "\n\nTesting Problem 3...\n\n")
      a = random.randint(4, 10)
      b = random.randint(2, 10)

      a2 = bin(a)[2:]
      b2 = bin(b)[2:]

      expected = b_rep(a + b, 2)
      returned = binary_add(a2, b2)
      print("%-30s%-20s%-20s%-20s" %
            (' ', 'Integer a', 'Integer b', 'Expected sum'))
      print("%-30s%-20s%-20s%-20s" % ('Decimal representation', a, b, a + b))
      print("%-30s%-20s%-20s%-20s" %
            ('Binary representation', a2, b2, expected))

      print("\n\nReturned sum:", returned)

      if expected == returned:
        print("Test passed.")
      else:
        print("Test failed.")

    elif user_in == '4':
      print("\n" + "-" * 50 + "\n\nTesting Problem 4...\n\n")
      a = random.randint(4, 10)
      b = random.randint(2, 10)

      a2 = bin(a)[2:]
      b2 = bin(b)[2:]

      expected = b_rep(a * b, 2)
      returned = binary_mul(a2, b2)
      print("%-30s%-20s%-20s%-20s" %
            (' ', 'Integer a', 'Integer b', 'Expected Product'))
      print("%-30s%-20s%-20s%-20s" % ('Decimal representation', a, b, a * b))
      print("%-30s%-20s%-20s%-20s" %
            ('Binary representation', a2, b2, expected))

      print("\n\nReturned product:", returned)

      if expected == returned:
        print("Test passed.")
      else:
        print("Test failed.")
    elif user_in == '5':
      your_tester.test()
    elif user_in.upper() == 'Q':
      print("Goodbye!")
      break
    else:
      print("Invalid selection.  Please try again.")


if __name__ == "__main__":
  main()
  sys.exit(0)
