from linkedlist import LinkedList
from helpers import *

x, y, z = LinkedList(), LinkedList(), LinkedList()
options = ['1', '2', '3']


def users_menu():
    users_choice = input(
        '1 - to enter elements of the lists\n2 - to get the lists randomly generated\n3 - to exit\n')
    if not (users_choice in options):
        print('Choose an option from the menu!')
    else:
        if users_choice == '3':
            print('The session is over!')
            return
        n = size_input()
        if users_choice == '1':
            x.input(n)
            y.input(n)
            z.input(n)
        if users_choice == '2':
            a, b = interval_input()
            x.generate(n, a, b)
            y.generate(n, a, b)
            z.generate(n, a, b)
        print('Enter the element, which you\'d like to find: ', end='')
        element = numeric_input()
        if (element == x.find_maximum() and x.find_position(element) <= x.__len__() / 2) and y.check_negative():
            y.cube_of_value()
        print('Your result:\n', x, '\n', y, '\n', z)
        x.clear()
        y.clear()
        z.clear()
    return users_menu()


users_menu()
