def alphabet_check(ch):

    # if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
    if ch in ['a', 'e', 'i', 'o', 'u']:
        print(ch, 'is vowel')
    else:
        print(ch, 'is consonant')


if __name__ == '__main__':
    ch = str(input("Enter a character to check: "))
    alphabet_check(ch)