from collection import Collection
from validation import Validation


@Validation.input_file_validation
def init_collection(collection):
    return collection


def users_menu():
    options = ['1', '2', '3', '4', '5', '6']
    print(auto_collection)
    users_choice = input(
        '1 - to sort the collection'
        '\n2 - to search for something in the collection'
        '\n3 - to add an element'
        '\n4 - to delete an element'
        '\n5 - to edit an element'
        '\n6 - to exit\n')
    if users_choice not in options:
        print('Choose an option from the menu')
    else:
        if users_choice == '6':
            print('The session is over')
            return
        if users_choice == '1':
            auto_collection.sorting()
            print(auto_collection)
        if users_choice == '2':
            auto_collection.searching()
        if users_choice == '3':
            auto_collection.adding(file_name, id=input('Enter ID: '), brand=input('Enter brand: '),
                                   model=input('Enter model: '),
                                   registration_number=input('Enter registration number: '),
                                   bought_at=input('Enter date of purchase: '),
                                   last_repaired_at=input('Enter date of last repairing: '),
                                   car_mileage=input('Enter mileage: '))
        if users_choice == '4':
            auto_collection.deleting()
        if users_choice == '5':
            auto_collection.editing(file_name)
        other_users_choice = input('Would you like to print the result in json-file(yes/no): ')
        while other_users_choice != 'yes' and other_users_choice != 'no':
            other_users_choice = input(
                'Choose suggested option!\nWould you like to print the result in json-file(yes/no): ')
        if other_users_choice == 'yes':
            auto_collection.in_json(input('Enter the file action for output: '))
        auto_collection.in_json(file_name)
    return users_menu()


auto_collection = Collection([])
auto_collection, file_name = init_collection(auto_collection)
users_menu()
