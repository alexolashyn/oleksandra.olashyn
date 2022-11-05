from logger import Logger


class Observer:
    observers = []

    def backup(self):
        self.observers.append(self)

    def __init__(self):
        self.dictionary = {}
        self.subscription = {}
        self.backup()

    def unsubscribe(self, key):
        if self.subscription[key]:
            self.subscription[key] = False
        else:
            print('You\'ve already unsubscribed from this event!')
            return

    def restore_subscription(self, key):
        if self.subscription[key]:
            print('You\'ve already subscribed to this event!')
            return
        self.subscription[key] = True

    def observe(self, action):
        log = Logger.in_file
        self.dictionary[action] = log
        for key in self.dictionary:
            self.subscription[key] = True



