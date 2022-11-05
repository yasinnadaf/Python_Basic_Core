def is_leapyear(year):
    """
    this function finds out weather the year is leap year or not
    :param year: int
    :return: none
    """

    if (year % 400 == 0) | (year % 4 == 0 & year != 100):
        print("it is a leap year")
    else:
        print("it is not a leap year")


if __name__ == '__main__':
    year = int(input("Enter a year to check: "))
    is_leapyear(year)