from Booking import Booking
from Collection import Collection
from validation import Validation

collection = Collection([])
collection.from_json('input.json')


def users_menu():
    options = ['1', '2', '3']
    print(collection)
    users_choice = input(
        '1 - to add new element'
        '\n2 - to get total price'
        '\n3 - to exit\n')
    if users_choice not in options:
        print('Choose an option from the menu')
    else:
        if users_choice == '3':
            print('The session is over')
            return
        if users_choice == '1':
            collection.adding()
        if users_choice == '2':
            collection.total_price()
    return users_menu()


users_menu()