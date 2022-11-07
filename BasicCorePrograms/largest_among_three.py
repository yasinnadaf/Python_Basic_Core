import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

def check_largest_num(num1, num2, num3):
    """
    This function will give the largest number among 3num.
    :param num1: int
    :param num2: int
    :param num3: int
    :return: none
    """
    try:
        if (num1 > num2) and (num1 > num3):
            print('num1 is largest', num1)
        elif (num2 > num3) and (num2 > num1):
            print('num2 is largest', num2)
        else:
            print('num3 is largest', num3)
    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    check_largest_num(54, 89, 60)
