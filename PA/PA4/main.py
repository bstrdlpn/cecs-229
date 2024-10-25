import random, math
import numpy as np
from plotting import plot
import pa4, your_tester
import image, png
import time


def print_points(pts_set, cols):
    for i in range(0, len(pts_set), cols):
        regex = "%-20s" * cols
        print(regex % tuple(list(pts_set)[i:i + cols]))
        if i % cols == 0:
            print()
        i += 1
    print()


print("Welcome to the PA #4 Tester")

while True:
    S = {
        2 + 2j, 3 + 2j, 1.75 + 1j, 2 + 1j, 2.25 + 1j, 2.5 + 1j, 2.75 + 1j,
        3 + 1j, 3.25 + 1j
    }
    user_in = input(
        "\n" + "-" * 50 +
        "\nWhich problem would you like to test?"
        "\n1.  Problem 1: translate(S, z0)"
        "\n2.  Problem 2: scale(S, k)"
        "\n3.  Problem 3: rotate(S, tau)"
        "\n4.  Problem 4: Vec class"
        "\n5.  Run your own tester"
        "\n6.  Quit"
        "\n\n7. I'm feeling extra."
        "\n\nEnter your selection: "
    )
    if user_in == '1':
        print("\n" + "-" * 50 + "\n\nTesting Problem 1...\n")
        print("ORIGINAL VALUES:")
        print_points(S, 3)

        T1 = pa4.translate(S, -3 -
                           2j)  # values translated by -3-2i will be plotted in red
        T2 = pa4.translate(
            S, 3 - 2j)  # values translated by 3-2i will be plotted in green
        T3 = pa4.translate(
            S, -3 + 2j)  # values translated by -3+2i will be plotted in blue
        T4 = pa4.translate(
            S, 3 + 2j)  # values translated by 3+2i will be plotted in yellow

        expected1 = {
            0j, (-0.25 - 1j), (-1 + 0j), -1j, (-1 - 1j), (-1.25 - 1j),
            (-0.75 - 1j), (0.25 - 1j), (-0.5 - 1j)
        }
        expected2 = {(6 - 1j), (6.25 - 1j), (5 + 0j), (6 + 0j), (5 - 1j),
                     (5.75 - 1j), (5.5 - 1j), (4.75 - 1j), (5.25 - 1j)}
        expected3 = {(-1 + 3j), (-1.25 + 3j), (-0.75 + 3j), (-1 + 4j), (-0.5 + 3j),
                     4j, (-0.25 + 3j), 3j, (0.25 + 3j)}
        expected4 = {(4.75 + 3j), (5.5 + 3j), (5.25 + 3j), (5 + 3j), (5 + 4j),
                     (6 + 4j), (5.75 + 3j), (6 + 3j), (6.25 + 3j)}

        print(' ' * 10 + '-' * 30)
        print("\nSHIFT LEFT 3, DOWN 2:")
        print("Expected Set:")
        print_points(expected1, 3)
        print("Returned Set:")
        print_points(T1, 3)

        print(' ' * 10 + '-' * 30)
        print("\nSHIFT RIGHT 3, DOWN 2:")
        print("Expected Set:")
        print_points(expected2, 3)
        print("Returned Set:")
        print_points(T2, 3)

        print(' ' * 10 + '-' * 30)
        print("\nSHIFT LEFT 3, UP 2:")
        print("Expected Set:")
        print_points(expected3, 3)
        print("Returned Set:")
        print_points(T3, 3)

        print(' ' * 10 + '-' * 30)
        print("\nSHIFT RIGHT 3, UP 2:")
        print("Expected Set:")
        print_points(expected4, 3)
        print("Returned Set:")
        print_points(T4, 3)

        if T1 == expected1 and T2 == expected2 and T3 == expected3 and T4 == expected4:
            print("Test PASSED.")
        else:
            print("Test FAILED.")

        plot(sets=[S, T1, T2, T3, T4], colors=['black', 'r', 'g', 'b', 'y'])

    elif user_in == '2':
        print("\n" + "-" * 50 + "\n\nTesting Problem 2...\n\n")

        T1 = pa4.translate(S, -3 -
                           2j)  # values translated by -3-2i will be plotted in red
        T2 = pa4.translate(
            S, 3 - 2j)  # values translated by 3-2i will be plotted in green
        T3 = pa4.translate(
            S, -3 + 2j)  # values translated by -3+2i will be plotted in blue
        T4 = pa4.translate(
            S, 3 + 2j)  # values translated by 3+2i will be plotted in yellow
        sets = [S, T1, T2, T3, T4]

        scaled_sets = [pa4.scale(A, 2) for A in sets]
        expected1 = {(3.5 + 2j), (4.5 + 2j), (5 + 2j), (4 + 2j), (5.5 + 2j),
                     (6 + 2j), (6.5 + 2j), (4 + 4j), (6 + 4j)}
        expected2 = {
            0j, (-2.5 - 2j), (0.5 - 2j), (-2 + 0j), (-1 - 2j), (-2 - 2j),
            (-1.5 - 2j), (-0.5 - 2j), -2j
        }
        expected3 = {(9.5 - 2j), (10.5 - 2j), (11.5 - 2j), (12.5 - 2j), (12 - 2j),
                     (10 - 2j), (11 - 2j), (10 + 0j), (12 + 0j)}
        expected4 = {(-2 + 6j), (-1.5 + 6j), (-1 + 6j), (-2.5 + 6j), (-0.5 + 6j),
                     6j, (-2 + 8j), (0.5 + 6j), 8j}
        expected5 = {(10 + 8j), (12 + 6j), (12 + 8j), (12.5 + 6j), (10 + 6j),
                     (9.5 + 6j), (10.5 + 6j), (11 + 6j), (11.5 + 6j)}
        expected = [expected1, expected2, expected3, expected4, expected5]
        for i in range(len(scaled_sets)):

            print("Original Set:")
            print_points(sets[i], 3)
            print("Expected after Scaling by 2:")
            print_points(expected[i], 3)
            print("Returned:")
            print_points(scaled_sets[i], 3)
            if expected[i] == scaled_sets[i]:
                print("Test PASSED!\n")
            else:
                print("Test FAILED.\n")
            print(' ' * 10 + '-' * 30)

        plot(sets + scaled_sets,
             colors=['gray'
                     for i in range(len(sets))] + ['black', 'r', 'g', 'b', 'y'])

    elif user_in == '3':
        print("\n" + "-" * 50 + "\n\nTesting Problem 3...\n\n")
        T1 = pa4.translate(S, -3 -
                           2j)  # values translated by -3-2i will be plotted in red
        T2 = pa4.translate(
            S, 3 - 2j)  # values translated by 3-2i will be plotted in green
        T3 = pa4.translate(
            S, -3 + 2j)  # values translated by -3+2i will be plotted in blue
        T4 = pa4.translate(
            S, 3 + 2j)  # values translated by 3+2i will be plotted in yellow
        sets = [S, T1, T2, T3, T4]

        r = int(
            input(
                "Select the angle to rotate by:\n1. pi/2\n2. -pi/2:\nYour selection: "
            ))
        if r == 1:
            rotated_sets = [pa4.rotate(A, math.pi / 2) for A in sets]
            expected = [{(-1 + 1.75j), (-2 + 2j), (-1 + 2.25j),
                         (-1 + 2j), (-1 + 2.5j), (-2 + 3j), (-1 + 2.75j), (-1 + 3j),
                         (-1 + 3.25j)},
                        {
                            0j, (1 - 0.25j), (1 + 0j), (1 - 0.75j), (1 + 0.25j),
                            (1 - 0.5j), (-0 - 1j), (1 - 1j), (1 - 1.25j)
                        },
                        {(1 + 4.75j), 5j, (1 + 5.25j), (1 + 5.75j), 6j, (1 + 6j),
                         (1 + 6.25j), (1 + 5j), (1 + 5.5j)},
                        {(-3 - 0.75j), (-3 - 0.25j), (-3 + 0j), (-3 + 0.25j),
                         (-4 - 1j), (-3 - 1j), (-3 - 1.25j), (-4 + 0j), (-3 - 0.5j)},
                        {(-3 + 4.75j),
                         (-4 + 5j), (-3 + 5j), (-3 + 5.25j), (-3 + 5.5j), (-4 + 6j),
                         (-3 + 5.75j), (-3 + 6j), (-3 + 6.25j)}]
            for i in range(len(rotated_sets)):
                print("Original Set:")
                print_points(sets[i], 3)
                print("Expected after rotating by pi/2:")
                print_points(expected[i], 3)
                print("Returned:")
                print_points(rotated_sets[i], 3)
                print(' ' * 10 + '-' * 30)
            plot(sets + rotated_sets,
                 colors=['gray'
                         for i in range(len(sets))] + ['black', 'r', 'g', 'b', 'y'])
        elif r == 2:
            expected2 = [{(1 - 3.25j), (1 - 2.25j), (1 - 2j), (1 - 2.75j), (1 - 3j),
                          (2 - 3j), (1 - 2.5j), (2 - 2j), (1 - 1.75j)},
                         {
                             0j, (-1 + 1j), (-1 + 1.25j), 1j, (-1 - 0j),
                             (-1 + 0.75j), (-1 - 0.25j), (-1 + 0.5j), (-1 + 0.25j)
                         },
                         {(-1 - 6.25j), (-1 - 6j), -6j, (-1 - 5.25j), (-1 - 5.75j),
                          -5j, (-1 - 5j), (-1 - 4.75j), (-1 - 5.5j)},
                         {(3 + 0.5j), (3 + 0.75j), (4 + 0j), (3 + 1.25j), (3 + 1j),
                          (4 + 1j), (3 + 0.25j), (3 + 0j), (3 - 0.25j)},
                         {(3 - 4.75j), (3 - 6j), (4 - 6j), (3 - 6.25j), (3 - 5.25j),
                          (3 - 5.5j), (3 - 5j), (4 - 5j), (3 - 5.75j)}]
            rotated_sets2 = [pa4.rotate(A, -1 * math.pi / 2) for A in sets]
            for i in range(len(rotated_sets2)):
                print("Original Set:")
                print_points(sets[i], 3)
                print("Expected after rotating by -pi/2:")
                print_points(expected2[i], 3)
                print("Returned:")
                print_points(rotated_sets2[i], 3)
                print(' ' * 10 + '-' * 30)

            plot(sets + rotated_sets2,
                 colors=['gray'
                         for i in range(len(sets))] + ['black', 'r', 'g', 'b', 'y'])

        else:
            print("Invalid selection. Returning to main menu...\n\n")
    elif user_in == '4':
        print("\n" + "-" * 50 + "\n\nTesting Problem 4...\n\n")
        u = pa4.Vec([1, 2, 3])
        w = pa4.Vec([0, 1, -1])
        v = pa4.Vec([0, -3])

        print("u = ", u)
        print("w = ", w)
        print("\nEuclidean norm of u:", abs(u))
        print("Expected:", math.sqrt(sum([ui ** 2 for ui in u.elements])))
        print("\nEuclidean norm of v:", abs(v))
        print("Expected: 3")
        print("\nu left scalar multiplication by 2:", 2 * u)
        print("Expected: [2, 4, 6]")
        print("\nw right scalar multiplication by -1:", w * -1)
        print("Expected: [0, -1, 1]")
        print("\nVector addition:", u + w)
        print("Expected: [1, 3, 2]")
        print("\nVector addition:", u - w)
        print("Expected: [1, 1, 4]")
        print("\nDot product:", w * u)
        print("Expected: -1")

        try:
            print("\nDot product:", v * u)
            print(
                "If this line prints, you forgot to raise a ValueError for taking the dot product of vectors of different lengths"
            )
        except ValueError:
            print("If this line prints, a ValueError was correctly raised.")

    elif user_in == '5':
        print("\n" + "-" * 50 + "\n\nRunning your own tester...\n\n")
        your_tester.test()

    elif user_in == '6' or user_in.upper() == 'Q':
        break

    elif user_in == '7':
        ready = input("Did you already complete problems 1 - 3? Y/N: ")
        if ready.upper() == 'N':
            print("Come back when you are done with problems 1 - 3.")
        elif ready.upper() == 'Y':
            print("\n\nHere is something a little extra...")
            time.sleep(1)
            print(
                "\nI am going to use complex numbers to represent dark pixels of img01.png"
            )

            img = image.file2image('img01.png')
            gray_img = image.color2gray(img)
            complex_img = image.gray2complex(gray_img)

            time.sleep(3)
            print("Okay.  Take a look at the 'Output' window...\n")
            plot([complex_img], colors=['black'], time=15)
            print(
                "\n\nHmm, that didn't look quite right, did it?  It seems like we should probably rotate the points.\n\n"
            )
            tau = input(
                "By how many radians should we rotate the points to make the image upright?\nYour response: "
            )
            if tau.strip() == '-pi/2':
                print(
                    "\nThat's right!  Let's rotate them!  I am counting on your rotate() function working correctly, btw..."
                )
            else:
                tau = input(
                    "Oof! that's not right.  I'll give you one more try.\nYour response: "
                )

                if tau.replace(' ', '').lower() == '-pi/2':
                    print("\nGood job!  Now let's rotate it!")
                    time.sleep(3)
                    print(
                        "\nI am counting on your rotate() function working correctly, btw..."
                    )
                else:
                    tau = math.pi / 2
                    print("\nNope.  The correct answer is -pi/2.")
                    time.sleep(3)
                    print("Anyway, let's rotate it by -pi/2.")
            rotated_img = pa4.rotate(complex_img, -math.pi / 2)
            time.sleep(3)
            print(
                "\nIf your rotate() function works correctly, then you are well on your way to creating the next Photoshoppe 2.0!"
            )
            time.sleep(3)
            print(
                "\nLook at the plot now that I have used your function to rotate the points..."
            )
            time.sleep(3)
            print(
                "\nThe gray points are the BEFORE, the black points are the AFTER..."
            )
            plot([complex_img, rotated_img], colors=['gray', 'black'], time=15)
            print(
                "\n\nAh, but wait! There's more: thanks to your trusty scale() function, I can scale the image by any factor!"
            )
            time.sleep(3)
            k = float(
                input(
                    "\nWhat would you like to scale the points by?\nYour response: ")
            )
            print("\nYour wish is my command...")
            time.sleep(2)
            scaled_img = pa4.scale(rotated_img, k)
            print("\nOkay, moment of truth...")
            time.sleep(2)
            print("\nHere is the plot of the scaled image...\n")
            time.sleep(3)
            print(
                "\nThe gray points are the BEFORE, the black points are the AFTER..."
            )
            plot([rotated_img, scaled_img], colors=['gray', 'black'], time=15)

            print("\n\nLast trick...let's translate the image!")
            time.sleep(3)
            h = float(input("\nPick a horizontal translation: "))
            v = float(input("Now pick a vertical translation: "))
            translated_img = pa4.translate(scaled_img, h + 1j * v)
            print("Here it goes!!!")
            time.sleep(3)
            print(
                "\nThe gray points are the BEFORE, the black points are the AFTER..."
            )
            plot([scaled_img, translated_img], colors=['gray', 'black'], time=15)
            print(
                "\n\nBe proud! Your Photoshoppe 2.0 will be ready for launch in no time!"
            )
        else:
            print("You're response is too extra.  I am sending you back to main...")
    else:
        print("Invalid selection.  Please try again.")
