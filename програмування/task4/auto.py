from validation import Validation


class Auto(object):
    def __init__(self, **kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def __str__(self):
        output = '-' * 50 + '\n'
        fields = self.__dict__
        for field in fields:
            str_field = str(field.lstrip('_'))
            output += str_field + ': ' + str(getattr(self, field)) + ', '
        output += '\n' + '-' * 50 + '\n'
        return output

    @property
    def id(self):
        return self._id

    @id.setter
    @Validation.numeric_validation
    def id(self, value):
        self._id = value

    @property
    def brand(self):
        return self._brand

    @brand.setter
    @Validation.brand_validation
    def brand(self, value):
        self._brand = value

    @property
    def model(self):
        return self._model

    @model.setter
    @Validation.model_validation
    def model(self, value):
        self._model = value

    @property
    def registration_number(self):
        return self._registration_number

    @registration_number.setter
    @Validation.registration_number_validation
    def registration_number(self, value):
        self._registration_number = value

    @property
    def bought_at(self):
        return self._bought_at

    @bought_at.setter
    @Validation.date_validation
    def bought_at(self, value):
        self._bought_at = value

    @property
    def last_repaired_at(self):
        return self._last_repaired_at

    @last_repaired_at.setter
    @Validation.date_validation
    @Validation.inappropriate_date
    def last_repaired_at(self, value):
        self._last_repaired_at = value

    @property
    def car_mileage(self):
        return self._car_mileage

    @car_mileage.setter
    @Validation.numeric_validation
    def car_mileage(self, value):
        self._car_mileage = value

