import math
import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)


def wind_chil(t, v):
    """
    this function calculate wind chill
    :param t:
    :param v:
    :return:
    """
    try:
        w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * (math.pow(v, 0.16));
        print(w)
    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    t = int(input("enter number: "))
    v = int(input("enter number: "))
    wind_chil(t, v)