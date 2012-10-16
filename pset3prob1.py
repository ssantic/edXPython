def evaluatePoly(poly, x):
    '''
    Computes the value of a polynomial function at given value x. Returns that
    value as a float.

    poly: list of numbers, length > 0
    x: number
    returns: float
    '''
    # FILL IN YOUR CODE HERE...
    total = 0
    exp = 0
    for i in poly:
        total = total + i*x**exp
        exp = exp + 1
    return float(total)

print evaluatePoly([2, 0, 7, 1], 4)