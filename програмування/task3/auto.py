from validation import Validation


class Auto:
    def __init__(self, id, brand, model, registration_number, last_repaired_at, bought_at, car_mileage):
        bought_at, last_repaired_at = Validation.inappropriate_date(bought_at, last_repaired_at)
        fields = {
            'id': Validation.validation_menu('id', id),
            'brand': Validation.validation_menu('brand', brand),
            'model': Validation.validation_menu('model', model),
            'registration_number': Validation.validation_menu('registration_number', registration_number),
            'last_repaired_at': Validation.validation_menu('last_repaired_at', last_repaired_at),
            'bought_at': Validation.validation_menu('bought_at', bought_at),
            'car_mileage': Validation.validation_menu('car_mileage', car_mileage)
        }
        for field in fields:
            setattr(self, field, fields[field])

    def __str__(self):
        output = '-' * 50 + '\n'
        fields = [
            'id',
            'brand',
            'model',
            'registration_number',
            'last_repaired_at',
            'bought_at',
            'car_mileage']
        for field in fields:
            output += field + ': ' + str(getattr(self, field)) + ', '
        output += '\n' + '-' * 50 + '\n'
        return output
