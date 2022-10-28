from strategy import *


class Context:
    def __init__(self):
        self.strategy = None

    def get_strategy(self):
        return self.strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def generate_arr(self, arr):
        self.strategy.list_generation(arr)

