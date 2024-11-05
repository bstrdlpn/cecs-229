import math
import numpy as np
from random import randint
from random import random


import pa5
import tester
from Vec import Vec
from vec_plotting import plot



def initialize_matrices(m, n):
  rows = [[randint(-10, 10) for j in range(n)] for i in range(m)]
  matrix = pa5.Matrix(rows)
  expected_rows = np.array(rows)
  return [expected_rows, matrix]

print("Welcome to the PA #5 Tester")

while True:

  user_in = input(
      "\n" + "-" * 50 +
      "\nWhat would you like to test?\n1.  Problem 1: Matrix constructor"
      "\n2.  Problem 1: Matrix getter methods"
      "\n3.  Problem 1: Matrix setter methods"
      "\n4.  Problem 1: Matrix operators"
      "\n5.  Problem 2: rotate_2Dvec()"
      "\n6.  Run your own tester."
      "\nQ.  Quit\n\nEnter your selection: "
  )

  if user_in == '1':
    print("\n" + "-" * 50 + "\n\nTesting Matrix constructor...\n")
    m = randint(2, 5)
    n = randint(2, 5)
    print(f"Creating Matrix object with {m} rows and {n} columns...")
    expected_rows, matrix = initialize_matrices(m, n)
    expected_cols = expected_rows.transpose()

    result_rows = matrix.rows
    result_cols = matrix.cols

    print("\nExpected rows:\n", expected_rows)
    print("\nReturned Matrix rows:\n", result_rows)

    print("\n\nExpected columns:\n", expected_cols)
    print("\nReturned Matrix columns:\n", result_cols)

    if np.array_equal(result_rows, np.array(expected_rows)) and np.array_equal(result_cols, np.array(expected_cols)):
      print("\nTest Passed!")
    else:
      print("\nTest Failed!")

  # ---------------- OPTION 2 ------------------ #
  elif user_in == '2':
    print("\n" + "-" * 50 + "\n\nTesting Matrix getter methods...\n")
    m = randint(2, 5)
    n = randint(2, 5)
    print(f"Creating Matrix object with {m} rows and {n} columns...")
    expected_rows, matrix = initialize_matrices(m, n)
    expected_cols = expected_rows.transpose()
    print(expected_rows)

    # getting row
    i = randint(1, m)
    print(f"\nTesting matrix.get_row({i})")
    returned_row = matrix.get_row(i)
    expected_row = expected_rows[i - 1]
    print(f"\tExpected: {list(expected_row)}\n\tReturned: {returned_row}")
    if np.array_equal(np.array(returned_row), expected_row):
      print("\tTest Passed!")
    else:
      print("\tTest Failed!")

    # getting column
    j = randint(1, n)
    print(f"\nTesting matrix.get_col({j})")
    returned_col = matrix.get_col(j)
    expected_col = expected_cols[j - 1]
    print(f"\tExpected: {list(expected_col)}\n\tReturned: {returned_col}")
    if np.array_equal(np.array(returned_col), expected_col):
      print("\tTest Passed!")
    else:
      print("\tTest Failed!")

    # getting entry
    i = randint(1, m)
    j = randint(1, n)
    print(f"\nTesting matrix.get_entry({i}, {j})")
    returned_ele = matrix.get_entry(i, j)
    expected_ele = expected_rows[i - 1][j - 1]
    print(f"\tExpected: {expected_ele}\n\tReturned: {returned_ele}")
    if returned_ele == expected_ele:
      print("\tTest Passed!")
    else:
      print("\tTest Failed!")

    # getting rows
    print("\nTesting matrix.get_rows()")
    returned_rows = matrix.get_rows()
    print(f"\tExpected:\n\t{expected_rows}\n\tReturned:\n\t{returned_rows}")
    if np.array_equal(np.array(returned_rows), expected_rows):
      print("\tTest Passed!")
    else:
      print("\tTest Failed!")

    # getting columns
    print("\nTesting matrix.get_columns()")
    returned_cols = matrix.get_columns()
    print(f"\tExpected:\n\t{expected_cols}\n\tReturned:\n\t{returned_cols}")
    if np.array_equal(np.array(returned_cols), expected_cols):
      print("\tTest Passed!")
    else:
      print("\tTest Failed!")


    # getting diag

    for d in range(n):
      print(f"\nTesting matrix.get_diag({d})")
      expected_diag = np.diag(expected_rows, k=d)
      returned_diag = matrix.get_diag(d)
      print(f"\tExpected:\n\t{expected_diag}\n\tReturned:\n\t{returned_diag}")
      if np.array_equal(np.array(returned_diag), expected_diag):
        print("\tTest Passed!")
      else:
        print("\tTest Failed!")

    for d in reversed(range(-1*m + 1, 0)):
      print(f"\nTesting matrix.get_diag({d})")
      expected_diag = np.diag(expected_rows, k=d)
      returned_diag = matrix.get_diag(d)
      print(f"\tExpected:\n\t{list(expected_diag)}\n\tReturned:\n\t{returned_diag}")
      if np.array_equal(np.array(returned_diag), expected_diag):
        print("\tTest Passed!")
      else:
        print("\tTest Failed!")

  # ---------------- OPTION 3 ------------------ #
  elif user_in == '3':
    print("\n" + "-" * 50 + "\n\nTesting Matrix setter methods...\n")
    m = randint(2, 5)
    n = randint(2, 5)
    print(f"Creating Matrix object with {m} rows and {n} columns...")
    expected_rows, matrix = initialize_matrices(m, n)
    print(expected_rows)

    new_row = [randint(-10, 10) for i in range(n)]
    i = randint(1, m)
    print(f"\nTesting matrix.set_row({i}, {new_row})")

    matrix.set_row(i, new_row)
    expected_rows[i - 1] = new_row
    expected_cols = expected_rows.transpose()
    print(f"Expected matrix:\n{expected_rows}\n\nReturned matrix:\n{matrix}")
    print(f"\nExpected rows: {expected_rows.tolist()}\nReturned rows: {matrix.rows}")
    print(f"\nExpected columns: {expected_cols.tolist()}\nReturned columns: {matrix.cols}")

    if np.array_equal(np.array(matrix.rows), expected_rows) and np.array_equal(np.array(matrix.cols), expected_cols):
      print("\n\tTest Passed!")
    else:
      print("\n\tTest Failed!")

    new_col = [randint(-10, 10) for i in range(m)]
    j = randint(1, n)
    print(f"\n\nTesting matrix.set_col({j}, {new_col})")

    matrix.set_col(j, new_col)

    expected_cols[j - 1] = new_col
    expected_rows = expected_cols.transpose()
    print(f"Expected matrix:\n{expected_rows}\n\nReturned matrix:\n{matrix}")

    print(f"\nExpected rows: {expected_rows.tolist()}\nReturned rows: {matrix.rows}")
    print(f"\nExpected columns: {expected_cols.tolist()}\nReturned columns: {matrix.cols}")

    if np.array_equal(np.array(matrix.rows), expected_rows) and np.array_equal(np.array(matrix.cols), expected_cols):
      print("\n\tTest Passed!")
    else:
      print("\n\tTest Failed!")

    new_ele = randint(-10, 10)
    i = randint(1, m)
    j = randint(1, n)
    print(f"\n\nTesting matrix.set_entry({i}, {j}, {new_ele})")

    matrix.set_entry(i, j, new_ele)

    expected_rows[i - 1][j - 1] = new_ele
    expected_cols[j - 1][i - 1] = new_ele
    print(f"Expected matrix:\n{expected_rows}\n\nReturned matrix:\n{matrix}")

    print(f"\nExpected rows: {expected_rows.tolist()}\nReturned rows: {matrix.rows}")
    print(f"\nExpected columns: {expected_cols.tolist()}\nReturned columns: {matrix.cols}")

    if np.array_equal(np.array(matrix.rows), expected_rows) and np.array_equal(np.array(matrix.cols), expected_cols):
      print("\n\tTest Passed!")
    else:
      print("\n\tTest Failed!")

  # ---------------- OPTION 4 ------------------ #
  elif user_in == '4':
    print("\n" + "-" * 50 + "\n\nTesting Matrix operators...\n")
    m = randint(2, 5)
    n = randint(2, 5)
    k = randint(2, 5)
    while n == k:
      k = randint(2, 5)
    print(f"Creating Matrix object with {m} rows and {n} columns...")
    exp_A, mat_A = initialize_matrices(m, n)
    print("A = \n", exp_A)

    print(f"\nCreating Matrix object with {m} rows and {n} columns...")
    exp_B, mat_B = initialize_matrices(m, n)
    print("B = \n", exp_B)

    print(f"\nCreating Matrix object with {n} rows and {k} columns...")
    exp_C, mat_C = initialize_matrices(n, k)
    print("C = \n", exp_C)

    print(f"\nCreating Vec object with {k} elements...")
    vec_k = Vec([randint(-10, 10) for i in range(k)])
    print("v =", vec_k)

    alpha = randint(-10, 10) + round(random(), 1)
    print(f"\nCreated scalar alpha = {alpha}")

    beta = randint(-10, 10)
    print(f"\nCreated scalar beta = {beta}")

    print('-'*20)
    print(f"\nTesting A+B:")
    expected = exp_A + exp_B
    result1 = mat_A + mat_B
    print(f"\nExpected:\n{expected}\n\nReturned:\n{result1}")
    if np.array_equal(np.array(result1.rows), expected):
      print("\n\tTest Passed!")
    else:
      print("\n\tTest Failed!")

    print('-'*20)
    print(f"\nTesting A-B:")
    expected = exp_A - exp_B
    result1 = mat_A - mat_B
    print(f"\nExpected:\n{expected}\n\nReturned:\n{result1}")
    if np.array_equal(np.array(result1.rows), expected):
      print("\n\tTest Passed!")
    else:
      print("\n\tTest Failed!")
    print('-'*20)
    print(f"\nTesting {alpha} * A:")
    expected = alpha * exp_A
    result1 = alpha * mat_A
    print(f"\nExpected:\n{expected}\n\nReturned:\n{result1}")
    if np.array_equal(np.array(result1.rows), expected):
      print("\n\tTest Passed!")
    else:
      print("\n\tTest Failed!")

    print('-'*20)
    print(f"\nTesting {beta} * A:")
    expected = beta * exp_A
    result1 = beta * mat_A
    print(f"\nExpected:\n{expected}\n\nReturned:\n{result1}")
    if np.array_equal(np.array(result1.rows), expected):
      print("\n\tTest Passed!")
    else:
      print("\n\tTest Failed!")

    print('-'*20)
    print(f"\nTesting A * {alpha}:")
    expected = alpha * exp_A
    result1 = mat_A * alpha
    print(f"\nExpected:\n{expected}\n\nReturned:\n{result1}")
    if np.array_equal(np.array(result1.rows), expected):
      print("\n\tTest Passed!")
    else:
      print("\n\tTest Failed!")

    print('-'*20)
    print(f"\nTesting A * {beta}:")
    expected = exp_A * beta
    result1 = mat_A * beta
    print(f"\nExpected:\n{expected}\n\nReturned:\n{result1}")
    if np.array_equal(np.array(result1.rows), expected):
      print("\n\tTest Passed!")
    else:
      print("\n\tTest Failed!")

    print('-'*20)
    print(f"\nTesting C * {vec_k}:")
    vec = np.array(vec_k.elements).transpose()
    expected = np.dot(exp_C , np.array(vec_k.elements))

    result1 = mat_C * vec_k
    print(f"\nExpected: {expected}\n\nReturned: {result1}")
    if np.array_equal(np.array(result1.elements), expected):
      print("\n\tTest Passed!")
    else:
      print("\n\tTest Failed!")

    print('-'*20)
    print(f"\nTesting B * C:")

    expected = np.dot(exp_B , exp_C)
    result1 = mat_B * mat_C
    print(f"\nExpected:\n{expected}\n\nReturned:\n{result1}")
    if np.array_equal(np.array(result1.rows), expected):
      print("\n\tTest Passed!")
    else:
      print("\n\tTest Failed!")

  # ---------------- OPTION 5 ------------------ #
  elif user_in == '5':
    print("\n" + "-" * 50 + "\n\nTesting rotate_2Dvec(vec, tau)...\n")
    vec = Vec([1, 0])
    tau1 = math.pi / 2
    result1 = pa5.rotate_2Dvec(vec, tau1)
    expected1 = Vec([0, 1])
    print(f"Vec v = {vec}\t\ttau = pi/2")
    print(f"Expected: {expected1}")
    print(f"Received: {result1}")
    if result1 == expected1:
      print("Test PASSED.")
    else:
      print("Test FAILED.")
    p = input("Display plot? Y/N: ")
    if p.upper() == 'Y':
      plot([vec, result1])

    tau2 = math.pi / 4
    result2 = pa5.rotate_2Dvec(vec, tau2)
    expected2 = Vec([2 ** -0.5, 2 ** -0.5])
    print(f"\nVec v = {vec}\t\ttau = pi/4")
    print(f"Expected: {expected2}")
    print(f"Received: {result2}")
    if result2 == expected2:
      print("Test PASSED.")
    else:
      print("Test FAILED.")

    p = input("Display plot? Y/N: ")
    if p.upper() == 'Y':
      plot([vec, result2])

  # ---------------- OPTION 6 ------------------ #
  elif user_in == '6':
    print("\n" + "-" * 50 + "\n\nRunning tester.test()...\n")
    tester.test()
  # ---------------- OPTION Q ------------------ #
  if user_in.upper() == 'Q':
    print("\n" + "-" * 50 + "\n\nGoodbye!")
    break
