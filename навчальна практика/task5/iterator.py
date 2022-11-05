class Numbers:
    def __init__(self, a=0, step=1, length=1):
        self.a = a
        self.step = step
        self.length = length

    def __iter__(self):
        return self

    def __next__(self):
        if self.length > 0:
            x = self.a
            self.a += self.step
            self.length -= 1
            return x
        else:
            raise StopIteration

    def __str__(self):
        return str(self.a)
