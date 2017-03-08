def zbits(n, k):
    """
    :param n: length of string
    :param k: number of zero bits
    :return: a set of strings
    """
    # initialize the set
    strings = set()
    position_index = range(0, n)
    # loop over the iterator
    for item in combinations(position_index, k):
        # create a list of n '1's
        string = ['1'] * len(position_index)
        # loop over the elements in each item
        for element in item:
            string[element] = '0'
        # join the elements into a single string
        strings.add(''.join(string))
    return strings
