from .brands import Brands
import datetime


class Validation:
    @staticmethod
    def numeric_validation(value, errors_dict):
        try:
            temp = int(value)
            if temp <= 0:
                errors_dict['numeric_field'] = 'Inappropriate value!'
        except:
            errors_dict['numeric_field'] = 'Inappropriate value!'

    @staticmethod
    def brand_validation(value, errors_dict):
        value, marker = value.lower(), False
        for brand in Brands:
            if value == brand.name:
                marker = True
        if not marker:
            errors_dict["brand"] = "Inappropriate brand value!"

    @staticmethod
    def model_validation(value, errors_dict):
        for index in range(len(value)):
            if value[index].isdigit() or value[index].isalpha():
                continue
            else:
                errors_dict["model"] = "Inappropriate model value!"

    @staticmethod
    def registration_number_validation(value, errors_dict):
        if len(value) != 8:
            errors_dict["registration_number"] = "Inappropriate registration number length!"
        for index in range(len(value)):
            if 1 < index < 6:
                if not value[index].isdigit():
                    errors_dict["registration_number"] = 'A letter cannot be in ' + str(
                            index) + ' position!'
            else:
                if not value[index].isalpha():
                    errors_dict["registration_number"] = 'A digit or lowercase cannot be in ' + str(
                            index) + ' position!'

    @staticmethod
    def date_validation(date, errors_dict):
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
        except:
            errors_dict['date'] = 'Inappropriate date value!'

    @staticmethod
    def inappropriate_date(date_of_purchase, date_of_last_repairing, errors_dict):
        if date_of_last_repairing < date_of_purchase:
            errors_dict['repaired_at'] = 'Date of purchase must be lower that date of last repairing'

