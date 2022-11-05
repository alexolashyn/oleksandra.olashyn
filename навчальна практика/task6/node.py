class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __eq__(self, other):
        return self.value == other

    def __str__(self):
        return str(self.value)