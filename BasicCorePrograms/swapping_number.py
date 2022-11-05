def swapping_number(num1, num2):
    """
    this function finds out the swapping of two numbers
    :param num1:
    :param num2:
    :return:
    """
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2
    print("after swapping num1:", num1, "\n after swapping num2:", num2)


if __name__ == '__main__':
    swapping_number(45, 80)


