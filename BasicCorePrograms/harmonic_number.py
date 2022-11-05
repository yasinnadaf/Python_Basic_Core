def harmonic_value(num):
    """
    this function calculates the harmonic number
    :param num:
    :return:
    """
    sum = 0
    for i in range(1, num+1):
        sum = sum + (1/i)
        print(sum)


if __name__ == '__main__':
    num = int(input("enter a number: "))
    harmonic_value(num)