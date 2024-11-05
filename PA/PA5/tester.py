import math

from Vec import Vec
from pa5 import Matrix, rotate_2Dvec
from vec_plotting import plot

def test():
    A = Matrix([[1, 2, 3], [4, 5, 6]])
    B = Matrix([[1, 0, 0], [0, 0, 1]])
    C = Matrix([[1, 0, 0], [0, 0, 3], [0, 2, 0]])
    alpha = 0.5
    v = Vec([1, 1, 1])
    u = Vec([3, 0, 1])
    print("Initial definitions:")
    print(f"\tMatrix A:\n{A}")
    print(f"\tMatrix B:\n{B}")
    print(f"\tMatrix C:\n{C}")
    print(f"Vector v = {v}")
    print(f"Vector u = {u}")
    print(f"Scalar alpha = {alpha}")

    print("\n\nOperations:")
    print(f"\talpha * A:\n{alpha * A}")
    print(f"\tB * alpha:\n{B * alpha}")
    print(f"\tA+B:\n{A + B}")
    print(f"\tA-B:\n{A - B}")
    print(f"\tA * v:\n{A * v}\n")
    print(f"\tA * C:\n{A * C}")
    print(f"\tC * A:")
    try:
        print(C * A)
    except ValueError as e:
        print("Error was correctly raised.")

    w = Vec([2, 0])
    tau = [-math.pi, -math.pi/2, -math.pi/3, -math.pi/4, math.pi/3, math.pi/2]
    names = ['-pi', '-pi/2', '-pi/3', '-pi/4', 'pi/3', 'pi/2']
    angles_dict = dict(zip(tau, names))
    vecs = [w]
    for t, label in angles_dict.items():
        w_rot = rotate_2Dvec(w, t)
        print(f"Rotated by {label} results in v = {w_rot}")
        vecs.append(w_rot)
    print()
    plot(vecs)