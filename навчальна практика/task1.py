def all_possible_variants(n, m):
    interval = 0
    maximum_possible_interval = (n-m)/(m-1)
    result = 0
    while interval <= maximum_possible_interval:
        trees_with_intervals = m+(m-1)*interval
        result += (n-trees_with_intervals+1)
        interval += 1
    return result


def check_users_input():
    n = input('Enter amount of all trees: ')
    m = input('Enter amount of remaining trees: ')
    try:
        n = int(n)
        m = int(m)
    except:
        print('Please use numeric digits.')
        return check_users_input()
    if m > n:
        print('Amount of remaining trees cannot be greater than amount of all trees.')
        return check_users_input()
    if (n <= 0) or (m < 0):
        print('Amount of remaining trees should be greater or equal to zero.\nAmount of all trees should be greater than zero.')
        return check_users_input()
    return n, m


n, m = check_users_input()
print('There are ', all_possible_variants(
    n, m), ' ways to cut down some of n trees so that after cutting there are m trees left')
