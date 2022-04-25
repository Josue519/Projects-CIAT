def summation(lower, upper):
    """ Arguments: a lower bound and an upper bound
    retuns: the sum of the number from lower through
    upper. """

    result = 0
    while lower <= upper:
        result += lower
        lower += 1
    return result


