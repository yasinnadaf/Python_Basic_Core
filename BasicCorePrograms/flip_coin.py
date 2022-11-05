import random


def flip_coin(num_of_flips):
    """
    This function prints the number of coin flips and its percentage
    :param num_of_flips:
    :return:
    """
    tail_count = 0
    head_count = 0
    for i in range(num_of_flips):
        rand = random.randint(1, 2)
        if rand == 1:
            tail_count += 1
            print( "tail")
        else:
            head_count += 1
            print('head')

    print('head:', head_count, 'tail:', tail_count)
    head_percentage = (head_count*100)/num_of_flips
    tail_percentage = (tail_count*100)/num_of_flips
    print('head% :', head_percentage)
    print('tail% :', tail_percentage)


if __name__ == '__main__':
    num_of_flips = int(input("enter number of coin to flip: "))
    flip_coin(num_of_flips)