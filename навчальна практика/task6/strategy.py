from linkedlist import LinkedList
from iterator import Numbers
import abc
from validation import Validation


class Strategy(LinkedList):
    @abc.abstractmethod
    def list_generation(self, arr):
        pass


class FirstStrategy(Strategy):
    def list_generation(self, arr):
        a = Validation.numeric_validation('Enter the star of sequence: ')
        step = Validation.numeric_validation('Enter the step: ')
        length = Validation.size_validation()
        position = Validation.position_validation()
        for x in Numbers(a, step, length):
            arr.insert(x, position)
            position += 1


class SecondStrategy(Strategy):
    def list_generation(self, arr):
        file_name = Validation.file_validation()
        position = Validation.position_validation()
        with open(file_name, "r") as file:
            for line in file:
                for x in line.split():
                    try:
                        arr.insert(int(x), position)
                        position += 1
                    except:
                        continue
        file.close()