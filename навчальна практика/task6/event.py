class Event:
    def __init__(self, action, current, previous, observer):
        self.action = action
        self.current = current
        self.previous = previous
        self.observer = observer
        if observer.subscription[action]:
            for x in self.observer.observers:
                if self.action in x.dictionary:
                    x.dictionary[self.action](self)

    def __str__(self):
        result = 'action: ' + self.action + ', current: ' + str(self.current) + ', previous: ' + str(self.previous)
        return result
