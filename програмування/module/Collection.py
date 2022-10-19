from Booking import Booking
import json
from validation import Validation
from datetime import date


class Collection:
    def __init__(self, container=None):
        self.container = container

    def __str__(self):
        output = ''
        for index in range(len(self.container)):
            output += str(self.container[index])
        return output

    def append(self, value):
        self.container.append(value)

    def from_json(self, file_name):
        with open(file_name, 'r') as json_file:
            journey_data = json.loads(json_file.read())
            for x in journey_data:
                temp = Booking()
                marker = True
                for key in x:
                    try:
                        setattr(temp, key, x[key])
                    except ValueError as e:
                        print(e)
                        marker = False
                    except AttributeError as e:
                        print(e)
                        marker = False
                if marker:
                    self.append(temp)
        json_file.close()
        self.price_upper()

    def total_price(self):
        result_dict = {}
        for booking in self.container:
            d1, d2 = date(int(booking.start_date.year), int(booking.start_date.month),
                          int(booking.start_date.day)), date(int(booking.end_date.year), int(booking.end_date.month),
                                                             int(booking.end_date.day))
            delta = d2 - d1
            result_dict[booking.name] = delta.days * booking.price_per_day
        print(result_dict)

    def price_upper(self):
        for index in range(len(self.container)):
            if index % 2 != 0:
                self.container[index].price_per_day += 10

    def adding(self):
        temp_dict = {
            'name': input('Enter the name: '),
            'price_per_day': input('Enter the price: '),
            'start_date': {
                'year': input('Enter the start year value: '),
                'month': input('Enter the start month value: '),
                'day': input('Enter the start day value: ')
            },
            'end_date': {
                'year': input('Enter the end year value: '),
                'month': input('Enter the end month value: '),
                'day': input('Enter the end day value: ')
            }
        }
        try:
            temp = Booking(**temp_dict)
            Validation.check_interval(self, temp)
        except ValueError as e:
            print(e)
        except AttributeError as e:
            print(e)


