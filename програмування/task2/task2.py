import numpy as np
import random as rnd
options = ['1', '2', '3']
MINIMUM_POSSIBLE_VALUE = 1
MAXIMUM_POSSIBLE_VALUE = 99


def numeric_input():
    try:
        number = int(input())
    except:
        print('Please use numeric digits!')
        return numeric_input()
    return number


def input_order():
    print('Enter the order of your matrix: ')
    order = numeric_input()
    if order > 0:
        return order
    print('The order should be greater than zero!')
    return input_order()


def interval_input():
    print('Enter the endpoints of the interval: ')
    a, b = numeric_input(), numeric_input()
    if (a <= b) and (a >= MINIMUM_POSSIBLE_VALUE or b <= MAXIMUM_POSSIBLE_VALUE):
        return a, b
    print('a<b\na>=1, b<=99')
    return interval_input()


def generate_order():
    a, b = interval_input()
    n = rnd.randint(a, b)
    return n


def init_matrix(matrix, order):
    element = 1
    n = order
    for row in range(order):
        for column in range(order):
            if(column >= n and row != 0):
                continue
            matrix[row][column] = element
        n -= 1
        element += 1
    return matrix


def print_matrix(matrix, order):
    for row in range(order):
        for column in range(order):
            if matrix[row][column]/10 >= 1:
                print(int(matrix[row][column]), end=" ")
                continue
            print(int(matrix[row][column]), end="  ")
        print('\n')


def users_menu():
    users_choice = input(
        'Choose an option:\n1 - to enter the order of your matrix\n2 - to get the order of your matrix randomly generated\n3 - to exit\n')
    if not(users_choice in options):
        print('Choose an option from the menu!')
    else:
        if users_choice == '3':
            print('The session is over!')
            return
        if users_choice == '1':
            order = input_order()
        if users_choice == '2':
            order = generate_order()
        matrix = np.zeros((order, order))
        init_matrix(matrix, order)
        print_matrix(matrix, order)
    return users_menu()


users_menu()