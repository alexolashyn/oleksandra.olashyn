from auto import Auto
from collection import Collection
from validation import Validation


def users_menu():
    options = ['1', '2', '3', '4', '5', '6']
    auto_collection = Collection([])
    auto_collection.from_json('input.json')
    print(auto_collection)
    users_choice = input(
        '1 - to sort the collection\n2 - to search for something in the collection\n3 - to add an element\n4 - to delete an element\n5 - to edit an element\n6 - to exit\n')
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
            temp_id = input('Enter ID: ')
            temp_brand = input('Enter brand: ')
            temp_model = input('Enter model: ')
            temp_registration_number = input('Enter registration number: ')
            temp_last_repaired_at = input('Enter date of last repairing(YYYY-MM-DD): ')
            temp_bought_at = input('Enter date of purchase: ')
            temp_car_mileage = input('Enter mileage: ')
            temp_auto = Auto(temp_id, temp_brand, temp_model, temp_registration_number, temp_last_repaired_at,
                             temp_bought_at, temp_car_mileage)
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
                'Choose suggested option!\nWould20 you like to print the result in json-file(yes/no): ')
        if other_users_choice == 'yes':
            auto_collection.in_json('output.json')
        auto_collection.in_json('input.json')
    return users_menu()


users_menu()
