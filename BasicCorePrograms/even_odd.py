def check_even_odd(num):
    """
    this function finds out even & odd number
    :param num:
    :return:
    """


    output = "number is even" if num % 2 == 0 else "number is odd"
    print(output)

    # if num % 2 == 0:
    #    print("number is even")
    # else:
    #     print("number is odd")


if __name__ == '__main__':
    num = int(input("Enter a number to check: "))
    check_even_odd(num)

# success statement if condition else failure statement