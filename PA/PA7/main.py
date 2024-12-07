import traceback
from random import randint
from structures import Vec, Matrix
from helpers import norm, count, frobenius_norm
import pa7
import numpy as np
from copy import deepcopy

menu = "-" * 40 + (
    "\nWhat would you like to test?\n1. Problem 1: qr_solve(A, b)\n2. Problem 2: determinant(A)\n3. "
    "Problem 3: eigen_wrapper(A)\n4. Problem 4: svd(A)\nQ. Quit.\n\nYour selection: "
)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
  print("Welcome to PA #7 Tester!")

  user_in = '0'
  while user_in.upper() != 'Q':
    user_in = input(menu)
    if user_in == '1':

      n = randint(3, 6)
      A = Matrix([[randint(-10, 10) for j in range(n)] for i in range(n)])
      x_expected = Vec([randint(-10, 10) for i in range(n)])
      b = A * x_expected
      print('-' * 30 + "\nTesting Problem 1: qr_solve(A, b) for...")
      print('A:\n', A)
      print('b: ', b)
      print('Expected:', x_expected)
      try:
        x_returned = pa7.qr_solve(A, b)
        print('Returned:', x_returned)
        if norm(x_expected - x_returned, 2) < 1e-7:
          print("Test passed!")
        else:
          print("Test failed!")
      except:
        error = traceback.format_exc()
        print(f"\nThe following unexpected error occurred:\n\n{error}")
    elif user_in == '2':
      n = randint(3, 6)
      rows = [[randint(-10, 10) for j in range(n)] for i in range(n)]
      A = Matrix(rows)
      expected = np.linalg.det(deepcopy(A.rows))

      print('-' * 30 + "\nTesting Problem 2: determinant(A) for...")
      print('A:\n', A)
      print('Expected:', expected)
      try:
        returned = pa7.determinant(A)
        print('Returned:', returned)
        if abs(expected - returned) < 1e-7:
          print("Test passed!")
        else:
          print("Test failed!")
      except:
        error = traceback.format_exc()
        print(f"\nThe following unexpected error occurred:\n\n{error}")

    elif user_in == '3':
      n = randint(3, 6)

      A = Matrix([[randint(-10, 10) for j in range(n)] for i in range(n)])

      print('-' * 30 + "\nTesting Problem 3: eigen_wrapper(A) for...")
      print('A:\n', A)
      try:
        returned = pa7.eigen_wrapper(A)
        print('Returned:\n')

        passed = []
        i = 1
        for val, vec in returned.items():
          print(
              "-" * 15 +
              f"\n{count[i]} eigenvalue \u03bb = {val}\n\n{count[i]} eigenvector v:\n{vec}"
          )
          Av = A * vec
          lam_v = val * vec
          print("\nA * v:\n", Av)
          print("\n\u03bb * v:\n", lam_v)
          i += 1
          passed.append(norm(Av - lam_v, 2) < 1e-7)
          print("\nA * v == \u03bb * v:", norm(Av - lam_v, 2) < 1e-7)

        if False in passed:
          print("\nTest failed!")
        else:
          print("\nTest passed!")
      except:
        error = traceback.format_exc()
        print(f"\nThe following unexpected error occurred:\n\n{error}")

    elif user_in == '4':
      n = randint(3, 6)
      A = Matrix([[randint(-10, 10) for j in range(n)] for i in range(n)])

      print('-' * 30 + "\nTesting Problem 4: svd(A) for...")
      print('A:\n', A)
      try:
        (U, Sigma, V) = pa7.svd(A)
        print("Returned:\n")
        print("U:\n", U)
        print("Sigma:\n", Sigma)
        print("V:\n", V)
        A_recon = U * Sigma * V.transpose()
        print("Reconstructed A:\n", A_recon)
        if frobenius_norm(A_recon - A) < 1e-7:
          print("Test passed!")
        else:
          print("Test failed!")
      except:
        error = traceback.format_exc()
        print(f"\nThe following unexpected error occurred:\n\n{error}")

    elif user_in.upper() != 'Q':
      print("Invalid selection.  Please try again.")
