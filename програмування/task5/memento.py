import copy


class Memento:
    def __init__(self):
        self.container = []

    def set_container(self, collection):
        self.container = collection

    def get_container(self):
        temp_container = copy.deepcopy(self.container)
        return temp_container
