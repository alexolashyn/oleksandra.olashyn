from django.db import models


class Auto(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    registration_number = models.CharField(max_length=8)
    bought_at = models.CharField(max_length=10)
    repaired_at = models.CharField(max_length=10)
    car_mileage = models.PositiveIntegerField(default=1000)

    def __str__(self):
        return str(self.id) + " " + str(self.brand) + " " + str(self.model) + " " + str(
            self.registration_number) + " " + str(self.bought_at) + " " + str(self.repaired_at) + " " + str(
            self.car_mileage) + "\n"
