import math


def quadratic(a,b,c):
    """
    this function is to find the quadratic roots of equation
    :param a:
    :param b:
    :param c:
    :return:
    """
    delta = b*b - 4 *a*c
    if delta < 0:
        print("data does not exist")
    else:
        root1 = (-b + math.sqrt(delta)) / (2*a)
        root2 = (-b - math.sqrt(delta)) / (2*a)
        print('root1:', root1)
        print(('root2:', root2))


if __name__ == '__main__':
    a = int(input("enter number1: "))
    b = int(input("enter number2:  "))
    c = int(input("enter number3: "))
    quadratic(a,b,c)