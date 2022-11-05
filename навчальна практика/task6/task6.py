from context import Context
from strategy import *
from linkedlist import LinkedList
import helpers
from observer import Observer

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
message = '1 - to select the First Strategy' \
          '\n2 - to select the Second Strategy' \
          '\n3 - to get lists generated' \
          '\n4 - to delete element from position' \
          '\n5 - to delete elements between positions' \
          '\n6 - to use main method' \
          '\n7 - to print lists' \
          '\n8 - to unsubscribe from the event' \
          '\n9 - to restore subscription' \
          '\n10 - to exit\n'
actions = ['Add', 'Delete', 'Main list method executed']


def users_menu():
    lists = {
        'x': LinkedList(),
        'y': LinkedList(),
        'z': LinkedList()
    }
    observer = Observer()
    observer.observe('Add')
    observer.observe('Delete')
    observer.observe('Main list method executed')
    context = Context()
    while True:
        users_choice = input(message)
        if users_choice not in options:
            print('Choose an option from the menu!')
            return users_menu()
        else:
            if users_choice == '1':
                context.set_strategy(FirstStrategy())
            if users_choice == '2':
                context.set_strategy(SecondStrategy())
            if users_choice == '3':
                for key in lists:
                    helpers.generate_arr(lists[key], context, observer)
            if users_choice == '4':
                for key in lists:
                    helpers.remove(lists[key], observer)
            if users_choice == '5':
                for key in lists:
                    helpers.remove_in_interval(lists[key], observer)
            if users_choice == '6':
                helpers.list_method(lists['x'], lists['y'], observer)
            if users_choice == '7':
                for key in lists:
                    print(key, ': ', lists[key])
            if users_choice == '8':
                key = input('Enter the name of event, which you\'d like to unsubscribe from: ')
                if key in actions:
                    observer.unsubscribe(key)
                else:
                    print('Your input is not valid!')
            if users_choice == '9':
                key = input('Enter the name of event, which you\'d like to subscribe to: ')
                if key in actions:
                    observer.restore_subscription(key)
                else:
                    print('Your input is not valid!')
            if users_choice == '10':
                print('The session is over!')
                break


users_menu()
