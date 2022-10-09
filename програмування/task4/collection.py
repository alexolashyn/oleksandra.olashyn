import json
from auto import Auto
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

    @Validation.id_validation
    def unique_id(self):
        pass

    def from_json(self, file_name):
        with open(file_name, 'r') as json_file:
            auto_data = json.loads(json_file.read())
            for x in auto_data:
                temp = Auto()
                for key in x:
                    try:
                        setattr(temp, key, x[key])
                    except ValueError as e:
                        print(key, ': ', x[key], end=' - ')
                        print(e)
                        continue
                temp_dict = temp.__dict__
                if len(temp_dict) == len(x):
                    self.auto_list.append(temp)
                self.unique_id()
        json_file.close()

    def in_json(self, file_name):
        dictionaries = [auto.__dict__ for auto in self.auto_list]
        for index in range(len(dictionaries)):
            arr = [key.lstrip('_') for key in dictionaries[index]]
            dictionaries[index] = dict(zip(arr, list(dictionaries[index].values())))
        with open(file_name, 'w') as json_file:
            json.dump(dictionaries, json_file, indent=4, separators=(',', ': '))
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
                    print(dictionaries[index]['_brand'], dictionaries[index]['_model'], ' = ',
                          characteristic.lstrip('_'),
                          ': ',
                          dictionaries[index][characteristic])

    def editing(self, file_name):
        try:
            id = int(input('enter ID: '))
            for auto in self.auto_list:
                if getattr(auto, 'id') == id:
                    attribute = Collection.characteristic_menu('for editing')
                    value = input('Enter new value: ')
                    temp = Auto(bought_at=auto.bought_at)
                    try:
                        setattr(temp, attribute, value)
                        try:
                            setattr(temp, 'last_repaired_at', auto.last_repaired_at)
                            setattr(auto, attribute, value)
                        except ValueError as e:
                            raise ValueError(e)
                        self.in_json(file_name)
                    except ValueError as e:
                        print(e)
        except ValueError as e:
            print(e)

    def deleting(self):
        try:
            id = int(input('Enter id: '))
            for auto in self.auto_list:
                if getattr(auto, 'id') == id:
                    self.auto_list.remove(auto)
        except ValueError as e:
            print(e)

    def adding(self, file_name, **other):
        try:
            temp = Auto(**other)
            self.auto_list.append(temp)
            self.unique_id()
            self.in_json(file_name)
        except ValueError as e:
            print(e)
