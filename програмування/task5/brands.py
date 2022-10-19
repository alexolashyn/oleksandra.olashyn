from enum import Enum


class Brands(Enum):
    honda = 1
    bmw = 2
    audi = 3
    toyota = 4
    mercedes = 5

    def __gt__(self, other):
        return self.name.lower() > other.name.lower()

    def __str__(self):
        return str(self.name)
