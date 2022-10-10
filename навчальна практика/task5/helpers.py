from validation import Validation


def generate_list(arr, context):
    if context is None:
        print('You have not chosen the strategy!')
        return
    context.generate_list(arr)


def empty_check(arr):
    if arr.is_empty():
        print('Inappropriate operation! The list ', arr, ' is already empty!')
        return False
    return True


def remove(arr):
    if empty_check(arr):
        position = Validation.position_validation()
        arr.remove(position)


def remove_in_interval(arr):
    if empty_check(arr):
        a, b = Validation.interval_validation()
        arr.delete_between_pos(a, b)


def list_method(x, y):
    y.list_method(x)

