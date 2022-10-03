class Numbers:
    def __init__(self, a=0, b=1, step=1):
        self.a = a
        self.b = b
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0:
            if self.a <= self.b:
                x = self.a
                self.a += self.step
                return x
            else:
                raise StopIteration
        else:
            if self.a >= self.b:
                x = self.a
                self.a += self.step
                return x
            else:
                raise StopIteration

    def __str__(self):
        return str(self.a)

