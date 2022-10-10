import os


class Validation:
    @staticmethod
    def numeric_validation(message=''):
        try:
            value = int(input(message))
        except ValueError as e:
            print(e)
            return Validation.numeric_validation('Enter new value: ')
        return value

    @staticmethod
    def size_validation(message='Enter the size of your arrays: '):
        n = Validation.numeric_validation(message)
        if n > 0:
            return n
        print('Size should be greater than zero!')
        return Validation.size_validation('Enter new value: ')

    @staticmethod
    def position_validation(message='Enter the position: '):
        n = Validation.numeric_validation(message)
        if n >= 0:
            return n
        print('Position cannot be less than zero!')
        return Validation.position_validation('Enter new value: ')

    @staticmethod
    def interval_validation(message='Enter the endpoints of the interval: '):
        a, b = Validation.position_validation(message), Validation.position_validation('')
        if a >= b:
            print('a should be less than b!')
            return Validation.interval_validation('Enter new value: ')
        return a, b

    @staticmethod
    def file_validation():
        file_name = input('Enter the file name: ')
        if not os.path.isfile(file_name):
            print('Inappropriate file name!')
            return Validation.file_validation()
        return file_name
