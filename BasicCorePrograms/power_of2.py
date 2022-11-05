def power_of_two(n):
    """
    this function finds out power of 2
    :param n:
    :return:
    """
    result = (n & n - 1)
    if (result == 0):
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    result = int(input("enter a number: "))
    power_of_two(result)
