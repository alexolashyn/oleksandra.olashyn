import datetime as datetime


class Validation:
    @staticmethod
    def numeric_validation(value):
        try:
            temp = int(value)
        except:
            new = input('Use numeric digit!\nEnter new value: ')
            return Validation.numeric_validation(new)
        if temp <= 0:
            new = input('Value should be greater than zero!\nEnter new value: ')
            return Validation.numeric_validation(new)
        return temp

    @staticmethod
    def brand_validation(value):
        for letter in value:
            if not letter.isalpha() or not letter.islower():
                new = input('Brand consists of lowercase letters!\nEnter the brand: ')
                return Validation.brand_validation(new)
        return value

    @staticmethod
    def model_validation(value):
        for index in range(len(value)):
            if value[index].isdigit() or value[index].isalpha():
                continue
            else:
                new = input('Model consists of lowercase letters and(or) numbers!\nEnter the model: ')
                return Validation.model_validation(new)
        return value

    @staticmethod
    def registration_number_validation(value):
        for index in range(len(value)):
            if 1 < index < 6:
                if not value[index].isdigit():
                    new = input(
                        'A letter cannot be in ' + str(
                            index) + ' position!\nEnter the registration number in format AA1234BC: ')
                    return Validation.registration_number_validation(new)
            else:
                if not value[index].isalpha() or not value[index].isupper():
                    new = input(
                        'A digit or lowercase cannot be in ' + str(
                            index) + ' position!\nEnter the registration number in format AA1234BC: ')
                    return Validation.registration_number_validation(new)
        return value

    @staticmethod
    def year_check(year):
        temp = Validation.numeric_validation(year)
        if temp > 2022 or temp < 1980:
            new = input('Year cannot be greate than 2022!\nInput year: ')
            return Validation.year_check(new)
        return temp

    @staticmethod
    def month_check(month):
        temp = Validation.numeric_validation(month)
        if temp > 12:
            new = input('Month cannot be greate than 12!\nInput month: ')
            return Validation.month_check(new)
        return temp

    @staticmethod
    def day_check(day):
        temp = Validation.numeric_validation(day)
        if temp > 31:
            new = input('Day cannot be greate than 31!\nInput day: ')
            return Validation.day_check(new)
        return temp

    @staticmethod
    def date_validation(date):
        year, month, day = '', '', ''
        str_date = str(date)
        for index in range(len(str_date)):
            if ((index == 4 or index == 7) and str_date[index] != '-') and len(str_date) > 10:
                new = input('Incorrect input!\nEnter the date(YYYY-MM-DD): ')
                return Validation.date_validation(new)
            if index < 4:
                year += str_date[index]
            elif 4 < index < 7:
                month += str_date[index]
            elif index > 7:
                day += str_date[index]
        year, month, day = Validation.year_check(year), Validation.month_check(month), Validation.day_check(day)
        month_30 = [4, 6, 9, 11]
        if month == 2:
            if (year % 4 == 0 and day > 29) or (year % 4 != 0 and day > 28):
                new = input('Inappropriate days value for February!\nEnter the date(YYYY-MM-DD): ')
                return Validation.date_validation(new)
        if month in month_30 and day > 30:
            new = input('Inappropriate days value for selected month!\nEnter the date(YYYY-MM-DD): ')
            return Validation.date_validation(new)
        if year == 2022:
            if month > 10:
                new = input('Inappropriate month value for selected year!\nEnter the date(YYYY-MM-DD): ')
                return Validation.date_validation(new)
            if month == 10 and day > 5:
                new = input('Inappropriate days value for selected month and year!\nEnter the date(YYYY-MM-DD): ')
                return Validation.date_validation(new)
        date = datetime.date(year, month, day)
        return date

    @staticmethod
    def inappropriate_date(date_of_purchase, date_of_last_repairing):
        while date_of_last_repairing < date_of_purchase:
            date_of_purchase, date_of_last_repairing = input(
                'The day of last repairing cannot be earlier than the date of purchase!\nEnter new date of purchase: '), input(
                'Enter new date of last repairing: ')
            date_of_purchase = Validation.date_validation(date_of_purchase)
            date_of_last_repairing = Validation.date_validation(date_of_last_repairing)
        return date_of_purchase, date_of_last_repairing

    @staticmethod
    def id_validation(auto_list):
        id_arr = []
        for auto in auto_list:
            if auto.id in id_arr:
                new = auto.id + 1
                while new in id_arr:
                    new += 1
                auto.id = new
                print('ID is incorrect!\nNew ID = ', new)
            id_arr.append(auto.id)
        id_arr.clear()

    @staticmethod
    def validation_menu(attribute, value, auto=None):
        if attribute == 'id':
            value = Validation.numeric_validation(value)
            return value
        if attribute == 'brand':
            value = Validation.brand_validation(value)
            return value
        if attribute == 'model':
            value = Validation.model_validation(value)
            return value
        if attribute == 'registration_number':
            value = Validation.registration_number_validation(value)
            return value
        if attribute == 'last_repaired_at':
            value = Validation.date_validation(value)
            if auto is not None:
                auto.bought_at, value = Validation.inappropriate_date(auto.bought_at, value)
            return value
        if attribute == 'bought_at':
            value = Validation.date_validation(value)
            if auto is not None:
                value, auto.last_repaired_at = Validation.inappropriate_date(value, auto.last_repaired_at)
            return value
        if attribute == 'car_mileage':
            value = Validation.numeric_validation(value)
            return value
