def numeric_input():
    try:
        number = int(input())
    except:
        print('Please use numeric digits!')
        return numeric_input()
    return number


def size_input():
    print('Enter the size of your arrays: ', end='')
    n = numeric_input()
    if n > 0:
        return n
    print('Size should be greater than zero!')
    return size_input()


def interval_input():
    print('Enter the start and end of the interval: ', end='')
    a, b = numeric_input(), numeric_input()
    if a <= b:
        return a, b
    print('a should be lower or equal to b')
    return interval_input()