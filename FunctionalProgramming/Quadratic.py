import math


def quadratic():
    """
    Description:
        In this function the two roots of quadratic equation is found.
        a, b, c are the three inputs to find the delta value.
    """

    a = int(input("Enter value for a : "))
    b = int(input("Enter value for b : "))
    c = int(input("Enter value for c : "))

    delta = abs(b * b - 4 * a * c)
    root1 = (-b + math.pow(delta, 1 / 2)) / (2 * a)
    root2 = (-b - math.pow(delta, 1 / 2)) / (2 * a)
    print("The First Root Of Equation Is ", root1)
    print("The Second Root Of Equation Is ", root2)


quadratic()
