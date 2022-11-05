import math


def distance_find(x, y):
    """
    this function is to find distance
    :param x:
    :param y:
    :return:
    """
    dist = math.sqrt(x*y + x*y)
    print(dist)


if __name__ == '__main__':
    x = int(input('enter number '))
    y = int(input('enter number '))
    distance_find(x, y)