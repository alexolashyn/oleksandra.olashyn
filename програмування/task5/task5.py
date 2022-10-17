from collection import Collection
from validation import Validation
from caretaker import Caretaker


@Validation.input_file_validation
def init_collection(collection):
    return collection


def users_menu():
    options = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    print(auto_collection)
    while True:
        users_choice = input(
            '1 - to sort the collection'
            '\n2 - to search for something in the collection'
            '\n3 - to add an element'
            '\n4 - to delete an element'
            '\n5 - to edit an element'
            '\n6 - to undo'
            '\n7 - to redo'
            '\n8 - to print the collection in json-file'
            '\n9 - to exit\n')
        if users_choice not in options:
            print('Choose an option from the menu')
        else:
            if users_choice == '9':
                print('The session is over')
                break
            if users_choice == '1':
                auto_collection.sorting()
                caretaker.backup()
            if users_choice == '2':
                auto_collection.searching()
            if users_choice == '3':
                auto_collection.adding(file_name, id=input('Enter ID: '), brand=input('Enter brand: '),
                                       model=input('Enter model: '),
                                       registration_number=input('Enter registration number: '),
                                       bought_at=input('Enter date of purchase: '),
                                       last_repaired_at=input('Enter date of last repairing: '),
                                       car_mileage=input('Enter mileage: '))
                caretaker.backup()
            if users_choice == '4':
                auto_collection.deleting()
                caretaker.backup()
            if users_choice == '5':
                auto_collection.editing(file_name)
                caretaker.backup()
            if users_choice == '6':
                caretaker.undo()
            if users_choice == '7':
                caretaker.redo()
            if users_choice == '8':
                auto_collection.in_json(input('Enter the file name for output: '))
            auto_collection.in_json(file_name)
        return users_menu()


auto_collection = Collection([])
auto_collection, file_name = init_collection(auto_collection)
caretaker = Caretaker(auto_collection)
caretaker.backup()
users_menu()
