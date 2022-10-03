def numeric_input(message=''):
    try:
        number = int(input(message))
    except:
        return numeric_input('Please use numeric digits!\nEnter value: ')
    return number


def interval_step_input():
    print('Enter the endpoints of the interval and the step: ', end='')
    a, b, step = numeric_input(), numeric_input(), numeric_input()
    if (a < b and step > 0) or (a > b and step < 0):
        return a, b, step
    print(
        'If step > 0, a should be less than  b\nIf step < 0 a should be greater than b\nIf step cannot be equal to zero')
    return interval_step_input()


def find_maximum_position(arr):
    maximum = arr[0]
    maximum_position = 0
    for index in range(len(arr)):
        if arr[index] > maximum:
            maximum = arr[index]
            maximum_position = index
    return maximum, maximum_position


def main_algorithm(arrays):
    print('Enter the element, which you\'d like to find: ', end='')
    element = numeric_input()
    maximum, maximum_position = find_maximum_position(arrays[0])
    negatives = [num for num in arrays[1] if num <= 0]
    if element == maximum and maximum_position < len(arrays[0]) / 2 and len(negatives) == len(arrays[1]):
        arrays[1] = [x ** 3 for x in arrays[1]]
    for index in range(len(arrays)):
        print(arrays[index])
