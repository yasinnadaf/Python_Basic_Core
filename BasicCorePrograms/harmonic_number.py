import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)


def harmonic_value(num):
    """
    this function calculates the harmonic number
    :param num:int
    :return:none
    """
    try:
        sum = 0
        for i in range(1, num + 1):
            sum = sum + (1 / i)
            print(sum)
    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    num = int(input("enter a number: "))
    harmonic_value(num)

