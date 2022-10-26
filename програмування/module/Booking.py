from validation import Validation
from Date import Date


class Booking(object):
    def __init__(self, **kwargs):
        for key in kwargs:
            try:
                setattr(self, key, kwargs[key])
            except ValueError as e:
                raise ValueError(e)
            except AttributeError as e:
                raise AttributeError(e)

    def __str__(self):
        output = '-' * 50 + '\n'
        fields = self.__dict__
        for field in fields:
            str_field = str(field.lstrip('_'))
            output += str_field + ': ' + str(getattr(self, field)) + ', '
        output += '\n' + '-' * 50 + '\n'
        return output

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = Validation.name_validation(value)

    @property
    def price_per_day(self):
        return self._price_per_day

    @price_per_day.setter
    def price_per_day(self, value):
        self._price_per_day = Validation.price_validation(value)

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        temp = Date()
        try:
            for key in value:
                setattr(temp, key, value[key])
        except ValueError as e:
            raise ValueError(e)
        except AttributeError as e:
            raise AttributeError(e)
        self._start_date = temp

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        temp = Date()
        try:
            for key in value:
                setattr(temp, key, value[key])
        except ValueError as e:
            raise ValueError(e)
        except AttributeError as e:
            raise AttributeError(e)
        try:
            start_date = self.start_date
            temp = Validation.inappropriate_date(temp, start_date)
        except ValueError as e:
            raise ValueError(e)
        except AttributeError as e:
            raise AttributeError(e)
        self._end_date = temp
