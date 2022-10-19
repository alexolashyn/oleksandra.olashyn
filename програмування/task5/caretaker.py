class Caretaker:
    def __init__(self, collection):
        self.states = []
        self.container = collection
        self.index = 0

    def backup(self):
        temp_memento = self.container.save()
        self.states.append(temp_memento)
        self.index += 1

    def undo(self):
        try:
            if self.index == 1:
                raise IndexError
            self.index -= 1
            memento = self.states[self.index - 1]
            self.container.restore(memento)
        except IndexError:
            print('Inappropriate operation!')

    def redo(self):
        try:
            self.index += 1
            memento = self.states[self.index - 1]
            self.container.restore(memento)
        except IndexError:
            print('Inappropriate operation!')
