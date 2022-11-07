import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

def power_of_two(n):
    """
    this function finds out power of 2
    :param n:int
    :return:none
    """
    try:
        result = (n & n - 1)
        output = True if result == 0 else False
        print(output)
        # if (result == 0):
        #     print(True)
        # else:
        #     print(False)
    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    result = int(input("enter a number: "))
    power_of_two(result)
