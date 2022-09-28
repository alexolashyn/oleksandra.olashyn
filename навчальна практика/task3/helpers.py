def numeric_input(message=''):
    try:
        number = int(input(message))
    except:
        print('Please use numeric digits!')
        return numeric_input(message)
    return number


def size_input():
    print('Enter the size of your arrays: ', end='')
    n = numeric_input()
    if n > 0:
        return n
    print('Size should be greater than zero!')
    return size_input()


def index_input():
    print('Enter the index of the element: ', end='')
    n = numeric_input()
    if n >= 0:
        return n
    print('Size should be greater or equal to zero!')
    return index_input()


def interval_input():
    print('Enter the start and end of the interval: ', end='')
    a, b = numeric_input(), numeric_input()
    if a <= b:
        return a, b
    print('a should be lower or equal to b')
    return interval_input()


def main_algorithm(x, y, z):
    print('Enter the element, which you\'d like to find: ', end='')
    element = numeric_input()
    if (element == x.find_maximum() and x.find_position(element) < x.__len__() / 2) and y.check_negative():
        y.cube_of_value()
    print('Your result:\n', x, '\n', y, '\n', z)


def list_changing(x, y, z):
    options = ['4', '5', '6']
    new_users_choice = input(
        '4 - to insert element to the certain position\n5 - to delete element from the position\n6 - to continue\n')
    if not (new_users_choice in options):
        print('Choose an option from the menu!')
    else:
        if new_users_choice == '6':
            main_algorithm(x, y, z)
            return
        lists = [x, y, z]
        for index in range(3):
            if new_users_choice == '4':
                element, position = numeric_input('Enter some element: '), index_input()
                lists[index].insert(element, position)
            else:
                position = index_input()
                lists[index].remove(position)
        if x.is_empty():
            print('Your lists is empty!')
        return list_changing(x, y, z)
