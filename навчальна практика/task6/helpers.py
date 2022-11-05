from validation import Validation
import copy
from event import *


def generate_arr(arr, context, observer):
    if context is None:
        print('You have not chosen the strategy yet!')
        return
    previous = copy.deepcopy(arr)
    context.generate_arr(arr)
    current = copy.deepcopy(arr)
    Event('Add', current, previous, observer)


def empty_check(arr):
    if arr.is_empty():
        print('Inappropriate operation! The list ', arr, ' is already empty!')
        return False
    return True


def remove(arr, observer):
    if empty_check(arr):
        position = Validation.position_validation()
        previous = copy.deepcopy(arr)
        arr.remove(position)
        current = copy.deepcopy(arr)
        Event('Delete', current, previous, observer)


def remove_in_interval(arr, observer):
    if empty_check(arr):
        a, b = Validation.interval_validation()
        previous = copy.deepcopy(arr)
        arr.remove_in_interval(a, b)
        current = copy.deepcopy(arr)
        Event('Delete', current, previous, observer)


def list_method(x, y, observer):
    previous = copy.deepcopy(y)
    y.list_method(x)
    current = copy.deepcopy(y)
    Event('Main list method executed', current, previous, observer)