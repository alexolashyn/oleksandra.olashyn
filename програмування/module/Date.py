from validation import Validation


class Date(object):
    def __init__(self, **kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def __str__(self):
        output = ''
        dictionary = self.__dict__
        for field in dictionary:
            output += dictionary[field] + '.'
        return output

    def __gt__(self, other):
        if int(self.year) == int(other.year):
            if int(self.month) == int(other.month):
                return int(self.day) > int(other.day)
            return int(self.month) > int(other.month)
        return int(self.year) > int(other.year)

    def __eq__(self, other):
        return self.year == other.year and self.month == other.month and self.day == other.day

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        try:
            self._year = Validation.year_validation(value)
        except ValueError as e:
            raise ValueError(e)

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        try:
            self._month = Validation.month_validation(value, self.year)
        except ValueError as e:
            raise ValueError(e)
        except AttributeError as e:
            raise AttributeError(e)

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        try:
            self._day = Validation.day_validation(value, self.month, self.year)
        except ValueError as e:
            raise ValueError(e)
        except AttributeError as e:
            raise AttributeError(e)
