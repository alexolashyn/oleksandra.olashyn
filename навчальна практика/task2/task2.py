import random as rnd
x = []
options = ['1', '2', '3']
operations = {
    'divide': 0,
    'compare': 0,
}


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


def input_or_generate_array(users_choice, n, a, b, arr=x):
    while len(arr) < n:
        if users_choice == '1':
            print('Your variant: ')
            element = numeric_input()
            arr.append(element)
        if users_choice == '2':
            arr.append(rnd.randint(a, b+1))
    return arr


def sorting(arr=x):
    if len(arr) > 1:
        sub_arr1, sub_arr2 = [], []
        for index in range(len(arr)):
            if(index < int(len(arr)/2)):
                sub_arr1.append(arr[index])
                continue
            sub_arr2.append(arr[index])
        operations['divide'] += 1
        sorting(sub_arr1)
        sorting(sub_arr2)
        sub_index1 = sub_index2 = 0
        arr.clear()
        while sub_index1 < len(sub_arr1) and sub_index2 < len(sub_arr2):
            if sub_arr1[sub_index1] < sub_arr2[sub_index2]:
                arr.append(sub_arr1[sub_index1])
                sub_index1 += 1
            else:
                arr.append(sub_arr2[sub_index2])
                sub_index2 += 1
            operations['compare'] += 1
        while sub_index1 < len(sub_arr1):
            arr.append(sub_arr1[sub_index1])
            sub_index1 += 1
        while sub_index2 < len(sub_arr2):
            arr.append(sub_arr2[sub_index2])
            sub_index2 += 1
    return arr


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
            print('Enter the start and end of the interval: ')
            a, b = numeric_input(), numeric_input()
        input_or_generate_array(users_choice, n, a, b)
        sorting()
        print(operations['compare'], ' - amount of comparisons, ',
              operations['divide'], ' - amount of dividing array')
        print(x)
        x.clear()
        operations['compare'] = operations['divide'] = 0
    return users_menu()


users_menu()
