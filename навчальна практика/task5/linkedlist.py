from node import *
from validation import Validation


class LinkedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        node = self.head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    def __str__(self):
        result = "["
        node = self.head
        if node:
            result += str(node.value)
            node = node.next
            while node:
                result += ", " + str(node.value)
                node = node.next
        result += "]"
        return result

    def is_empty(self):
        return self.head is None

    def append(self, other):
        node = self.head
        if not self.is_empty():
            while node.next:
                node = node.next
            node.next = Node(other)
        else:
            self.head = Node(other)

    def insert(self, value, position):
        if position < 0:
            print('Inappropriate position!')
            return
        if position == 0:
            self.head = Node(value, self.head)
        elif position >= self.__len__():
            self.append(value)
        else:
            i = 0
            node = self.head
            while node.next:
                if i == position - 1:
                    node.next = Node(value, node.next)
                node = node.next
                i += 1

    def remove(self, position):
        if self.is_empty():
            return
        index = 0
        node = self.head
        previous_node = None
        while node.next and index < position:
            previous_node = node
            node = node.next
            index += 1
        if index == 0:
            self.head = self.head.next
        else:
            previous_node.next = node.next

    def delete_between_pos(self, a, b):
        if a >= b:
            print('Inappropriate positions value!')
            return
        for i in range(b - a + 1):
            if self.is_empty():
                break
            self.remove(a)

    def clear(self):
        if self.is_empty():
            print('The list is already empty!')
            return
        node = self.head
        while node:
            self.head = node.next
            node = self.head

    def check_negative(self):
        node = self.head
        while node.next:
            if node.value > 0:
                return False
            node = node.next
        return True

    def find_maximum(self):
        if not self.is_empty():
            node = self.head
            maximum = node.value
            while node.next:
                node = node.next
                if node.value > maximum:
                    maximum = node.value
            return maximum
        else:
            return

    def find_position(self, value):
        if not self.is_empty():
            position = 0
            node = self.head
            while node.value != value:
                position += 1
                node = node.next
            return position
        else:
            return

    def cube_of_value(self):
        if not self.is_empty():
            maximum = self.find_maximum()
            node = self.head
            while node.value != maximum:
                node.value = node.value ** 3
                node = node.next
        else:
            return

    def list_method(self, other_list):
        wanted_element = Validation.numeric_validation('Enter element which you\'d like to find: ')
        if wanted_element == other_list.find_maximum() and other_list.find_position(
                wanted_element) < other_list.__len__() / 2:
            if self.check_negative():
                self.cube_of_value()
