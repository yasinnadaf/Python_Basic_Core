def check_largest_num(num1, num2, num3):
    if (num1 > num2) and (num1 > num3):
        print('num1 is largest', num1)
    elif (num2 > num3) and (num2 > num1):
        print('num2 is largest', num2)
    else:
        print('num3 is largest', num3)


if __name__ == '__main__':
    check_largest_num(54, 89, 60)
