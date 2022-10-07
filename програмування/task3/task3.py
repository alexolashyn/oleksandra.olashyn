from auto import Auto
from collection import Collection
from validation import Validation

auto_collection = Collection([])
auto_collection = Validation.input_file_validation(auto_collection)


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
            temp_auto = Auto(id=input('Enter ID: '), brand=input('Enter brand: '), model=input('Enter model: '),
                             registration_number=input('Enter registration number: '),
                             last_repaired_at=input('Enter date of last repairing(YYYY-MM-DD): '),
                             bought_at=input('Enter date of purchase: '), car_mileage=input('Enter mileage: '))
            temp_auto.bought_at, temp_auto.last_repaired_at = Validation.inappropriate_date(temp_auto.bought_at,
                                                                                            temp_auto.last_repaired_at)
            auto_collection.adding(temp_auto, 'input.json')
        if users_choice == '4':
            temp_id = input('Enter ID: ')
            temp_id = Validation.numeric_validation(temp_id)
            auto_collection.deleting(temp_id, 'input.json')
        if users_choice == '5':
            temp_id = input('Enter ID: ')
            temp_id = Validation.numeric_validation(temp_id)
            auto_collection.editing(temp_id, 'input.json')
        other_users_choice = input('Would you like to print the result in json-file(yes/no): ')
        while other_users_choice != 'yes' and other_users_choice != 'no':
            other_users_choice = input(
                'Choose suggested option!\nWould you like to print the result in json-file(yes/no): ')
        if other_users_choice == 'yes':
            auto_collection.in_json(input('Enter the name of file: '))
        auto_collection.in_json('input.json')
    return users_menu()


users_menu()
