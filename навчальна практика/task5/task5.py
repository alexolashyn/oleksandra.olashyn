from context import Context
from strategy import *
from linkedlist import LinkedList
import helpers

options = ['1', '2', '3', '4', '5', '6', '7', '8']
message = '1 - to select the First Strategy' \
          '\n2 - to select the Second Strategy' \
          '\n3 - to get lists generated' \
          '\n4 - to delete element from position' \
          '\n5 - to delete elements between positions' \
          '\n6 - to use main method' \
          '\n7 - to print lists' \
          '\n8 - to exit\n'


def users_menu():
    lists = {
        'x': LinkedList(),
        'y': LinkedList(),
        'z': LinkedList()
    }
    context = None
    while True:
        users_choice = input(message)
        if users_choice not in options:
            print('Choose an option from the menu!')
            return users_menu()
        else:
            if users_choice == '1':
                context = Context()
                context.set_strategy(FirstStrategy())
            if users_choice == '2':
                context = Context()
                context.set_strategy(SecondStrategy())
            if users_choice == '3':
                for key in lists:
                    helpers.generate_arr(lists[key], context)
            if users_choice == '4':
                for key in lists:
                    helpers.remove(lists[key])
            if users_choice == '5':
                for key in lists:
                    helpers.remove_in_interval(lists[key])
            if users_choice == '6':
                helpers.list_method(lists['x'], lists['y'])
            if users_choice == '7':
                for key in lists:
                    print(key, ': ', lists[key])
            if users_choice == '8':
                print('The session is over!')
                break


users_menu()
