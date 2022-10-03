from validation import Validation


class Auto:
    def __init__(self, id, brand, model, registration_number, last_repaired_at, bought_at, car_mileage):
        self.id = Validation.numeric_validation(id)
        self.brand = Validation.brand_validation(brand)
        self.model = Validation.model_validation(model)
        self.registration_number = Validation.registration_number_validation(registration_number)
        self.last_repaired_at = Validation.date_validation(last_repaired_at)
        self.bought_at = Validation.date_validation(bought_at)
        while self.last_repaired_at < self.bought_at:
            self.bought_at, self.last_repaired_at = Validation.inappropriate_date(self.bought_at, self.last_repaired_at)
        self.car_mileage = car_mileage

    def __str__(self):
        output = '\nID: ' + str(
            self.id) + ' Brand: ' + self.brand + ' Model: ' + self.model + ' Number: ' + self.registration_number + '\nDate of last repairing: ' + str(
            self.last_repaired_at) + ' Date of purchase: ' + str(self.bought_at) + ' Mileage: ' + str(
            self.car_mileage) + '\n' + '-' * 100
        return output
