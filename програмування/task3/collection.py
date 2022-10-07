import json
from auto import Auto
import datetime
from validation import Validation


class Collection:
    def __init__(self, auto_list=None):
        self.auto_list = auto_list

    def __str__(self):
        output = ''
        for index in range(len(self.auto_list)):
            output += str(self.auto_list[index])
        return output

    def __len__(self):
        return len(self.auto_list)

    def append(self, value):
        self.auto_list.append(value)

    def from_json(self, file_name):
        with open(file_name, 'r') as json_file:
            auto_data = json.loads(json_file.read())
            for x in auto_data:
                x['bought_at'], x['last_repaired_at'] = Validation.inappropriate_date(x['bought_at'],
                                                                                      x['last_repaired_at'])
                self.auto_list.append(Auto(**x))

        Validation.id_validation(self.auto_list)
        json_file.close()

    @staticmethod
    def conversion(value):
        if isinstance(value, datetime.date):
            return value.__str__()

    def in_json(self, file_name):
        with open(file_name, 'w') as json_file:
            json.dump([auto.__dict__ for auto in self.auto_list], json_file, indent=4, separators=(',', ': '),
                      default=Collection.conversion)
        json_file.close()

    @staticmethod
    def characteristic_menu(message=''):
        options = ['brand', 'model', 'registration_number', 'last_repaired_at', 'bought_at', 'car_mileage']
        print('Choose an identifier', message)
        users_choice = input(
            'brand - by brand'
            '\nmodel - by model'
            '\nregistration_number - by registration number'
            '\nlast_repaired_at - by date of last repairing'
            '\nbought_at - by date of purchase'
            '\ncar_mileage - by car mileage\n')
        if users_choice not in options:
            print('Choose options from the list!')
            return Collection.characteristic_menu(message)
        return users_choice

    def sorting(self):
        characteristic = Collection.characteristic_menu('for sorting')
        self.auto_list = sorted(self.auto_list, key=lambda product: str(getattr(product, characteristic)).lower())

    def searching(self):
        item = input('Enter what you\'d like to find: ')
        dictionaries = [auto.__dict__ for auto in self.auto_list]
        for index in range(len(dictionaries)):
            for characteristic in dictionaries[index]:
                if item in str(dictionaries[index][characteristic]):
                    print(dictionaries[index]['brand'], dictionaries[index]['model'], ' = ', characteristic,
                          dictionaries[index][characteristic])

    def editing(self, id, file_name):
        for auto in self.auto_list:
            if auto.id == id:
                attribute = Collection.characteristic_menu('for editing')
                value = input('Enter new value: ')
                value = Validation.validation_menu(attribute, value, auto)
                setattr(auto, attribute, value)
        self.in_json(file_name)

    def deleting(self, id, file_name):
        for auto in self.auto_list:
            if auto.id == id:
                self.auto_list.remove(auto)
        self.in_json(file_name)

    def adding(self, other, file_name):
        self.auto_list.append(other)
        Validation.id_validation(self.auto_list)
        self.in_json(file_name)
