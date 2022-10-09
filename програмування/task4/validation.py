import datetime
from brands import Brands


class Validation:
    @staticmethod
    def numeric_validation(func):
        def sub_numeric_validation(auto, value):
            try:
                value = int(value)
                if value <= 0:
                    raise ValueError('Use natural numbers!')
            except ValueError as e:
                raise ValueError(e)
            return func(auto, value)

        return sub_numeric_validation

    @staticmethod
    def brand_validation(func):
        def sub_brand_validation(auto, value):
            value, marker = value.lower(), False
            for data in Brands:
                if value == data.name:
                    marker = True
            if not marker:
                raise ValueError('There is no such brand!')
            return func(auto, value)

        return sub_brand_validation

    @staticmethod
    def model_validation(func):
        def sub_model_validation(auto, value):
            for char in value:
                if char.isalpha() or char.isdigit():
                    continue
                else:
                    raise ValueError(
                        'Model should include letters and(or) numbers!')
            return func(auto, value)

        return sub_model_validation

    @staticmethod
    def registration_number_validation(func):
        def sub_registration_number_validation(auto, value):
            if len(value) != 8:
                raise ValueError(
                    'Inappropriate length of the registration number!')
            for index in range(len(value)):
                if 1 < index < 6:
                    if not value[index].isdigit():
                        raise ValueError('A letter cannot be in ' + str(index) +
                                         ' position!')
                else:
                    if not value[index].isalpha() or not value[index].isupper():
                        raise ValueError('A digit or lowercase cannot be in ' + str(index) +
                                         ' position!')
            return func(auto, value)

        return sub_registration_number_validation

    @staticmethod
    def date_validation(func):
        def sub_date_validation(auto, value):
            try:
                datetime.datetime.strptime(value, '%Y-%m-%d')
            except ValueError as e:
                raise ValueError(e)
            year, month, day = value.split('-')
            if year > '2022':
                raise ValueError('Year cannot be greater than 2022!')
            if year < '1960':
                raise ValueError('Year cannot be less than 1960!')
            if year == '2022':
                if month >= '11':
                    raise ValueError('Inappropriate month value for selected year!')
                if month == '10' and day > '12':
                    raise ValueError('Inappropriate month value for selected year!')
            value = year + '-' + month + '-' + day
            return func(auto, value)

        return sub_date_validation

    @staticmethod
    def inappropriate_date(func):
        def sub_inappropriate_date(auto, value):
            if value < getattr(auto, 'bought_at'):
                raise ValueError(
                    'The date of last repairing cannot be earlier than the date of purchase!')
            return func(auto, value)

        return sub_inappropriate_date

    @staticmethod
    def id_validation(func):
        def sub_id_validation(collection):
            id_list = []
            for auto in collection.auto_list:
                while auto.id in id_list:
                    auto.id += 1
                id_list.append(auto.id)
            return func(collection)

        return sub_id_validation

    @staticmethod
    def input_file_validation(func):
        def sub_input_file_validation(collection):
            file_name = input('Enter file name: ')
            try:
                collection.from_json(file_name)
                return func(collection), file_name
            except:
                return sub_input_file_validation(collection)

        return sub_input_file_validation
