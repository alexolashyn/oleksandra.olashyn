from decimal import Decimal


class Validation:
    @staticmethod
    def year_validation(value):
        try:
            temp = int(value)
            if temp < 2019:
                raise ValueError('Inappropriate year value!')
        except ValueError as e:
            raise ValueError(e)
        return value

    @staticmethod
    def month_validation(value, year):
        try:
            temp = int(value)
            if temp not in range(1, 13):
                raise ValueError('Inappropriate month value!')
            if int(year) == 2019 and temp < 10:
                raise ValueError('Inappropriate month value!')
        except ValueError as e:
            raise ValueError(e)
        return value

    @staticmethod
    def day_validation(value, month, year):
        month_30 = ['4', '6', '9', '11']
        try:
            temp = int(value)
            if temp not in range(1, 32):
                raise ValueError('Inappropriate day value!')
            if month == '10' and year == '2019' and temp < 23:
                raise ValueError('Inappropriate day value!')
            if month in month_30 and temp == 31:
                raise ValueError('Inappropriate day value!')
            if month == '2' and int(year) % 4 == 0 and temp > 29:
                raise ValueError('Inappropriate day value!')
            if month == '2' and int(year) % 4 != 0 and temp > 28:
                raise ValueError('Inappropriate day value!')
        except ValueError as e:
            raise ValueError(e)
        return value

    @staticmethod
    def inappropriate_date(value, start_date):
        try:
            if start_date > value:
                raise ValueError('Inappropriate date!')
        except AttributeError as e:
            raise AttributeError(e)
        return value

    @staticmethod
    def name_validation(value):
        for letter in value:
            if not letter.isalpha():
                raise ValueError('Inappropriate action value!')
        return value

    @staticmethod
    def price_validation(value):
        try:
            temp = float(value)
            temp = Decimal(str(temp)) % 1
            if len(str(temp)) > 4:
                raise ValueError('Inappropriate price value!')
            if temp < 0:
                raise ValueError('Inappropriate price value!')
        except ValueError as e:
            raise ValueError(e)
        return float(value)

    @staticmethod
    def check_interval(self, other):
        marker = False
        for booking in self.container:
            if other.start_date > booking.start_date and other.start_date > booking.end_date:
                marker = True
                break
            elif booking.start_date > other.start_date and booking.start_date > other.end_date:
                marker = True
                break
        if marker:
            self.append(other)


