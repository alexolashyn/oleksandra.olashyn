class Logger:
    memory = []

    def __init__(self):
        pass

    @staticmethod
    def update_memory(event):
        Logger.memory.append(event)

    @staticmethod
    def in_file(new_event):
        file = open('notifications.txt', 'w')
        Logger.update_memory(new_event)
        for event in Logger.memory:
            file.write(str(event) + '\n')
        file.close()


