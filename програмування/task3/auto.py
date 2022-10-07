from validation import Validation


class Auto:
    def __init__(self, **kwargs):
        for key in kwargs:
            value = Validation.validation_menu(str(key), kwargs[key])
            setattr(self, str(key), value)

    def __str__(self):
        output = '-' * 50 + '\n'
        fields = self.__dict__
        for field in fields:
            output += field + ': ' + str(getattr(self, field)) + ', '
        output += '\n' + '-' * 50 + '\n'
        return output
