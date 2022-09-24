import random as rnd
arrays = [[], [], []]
options = ['1', '2', '3']


def numeric_input():
    try:
        number = int(input())
    except:
        print('Please use numeric digits.')
        return numeric_input()
    return number


def input_size():
    print('Enter the size of your arrays: ')
    n = numeric_input()
    if n > 0:
        return n
    print('Size should be greater than zero')
    return input_size()


def input_interval():
    print('Enter the start and end of the interval: ')
    a, b = numeric_input(), numeric_input()
    if a <= b:
        return a, b
    print('a should be lower or equal to b')
    return input_interval()


def input_or_generate_array(users_choice, arr, n, a, b):
    while len(arr) < n:
        if users_choice == '1':
            print('Your variant: ')
            element = numeric_input()
            arr.append(element)
        if users_choice == '2':
            arr.append(rnd.randint(a, b))


def find_max(arr):
    max = arr[0]
    for element in arr:
        if(element > max):
            max = element
    return max


def check_arrays(x, y):
    print('Enter the number, which you\'d like to find out in array x:')
    k = numeric_input()
    max_x, max_y = find_max(x), find_max(y)
    if k != max_x:
        return x, y
    for index in range(int(len(x)/2)):
        if(k == x[index]):
            break
        if(index == int(len(x)/2)-1):
            return x, y
    for element in y:
        if element > 0:
            return x, y
    index = 0
    while y[index] != max_y:
        y[index] = (y[index]**3)
        index += 1


def users_menu():
    users_choice = input(
        '1 - to enter elements of arrays\n2 - to get arrays randomly generated\n3 - to exit\n')
    if not(users_choice in options):
        print('Choose an option from the menu')
    else:
        if users_choice == '3':
            print('The session is over')
            return 0
        n = input_size()
        a, b = 0, 0
        if users_choice == '2':
            a, b = input_interval()
        for arr in arrays:
            input_or_generate_array(users_choice, arr, n, a, b)
        (check_arrays(arrays[0], arrays[1]))
        print('Your result:')
        for arr in arrays:
            print(arr)
            arr.clear()
    return users_menu()


users_menu()
