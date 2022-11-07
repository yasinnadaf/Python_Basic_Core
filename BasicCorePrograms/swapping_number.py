import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)


def swapping_number(num1, num2):
    """
    this function finds out the swapping of two numbers
    :param num1:int
    :param num2:int
    :return:none
    """
    try:
        num1 = num1 + num2
        num2 = num1 - num2
        num1 = num1 - num2
        print("after swapping num1:", num1, "\n after swapping num2:", num2)
    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    swapping_number(45, 80)


