def computeDeriv(poly):
    '''
    Computes and returns the derivative of a polynomial function as a list of
    floats. If the derivative is 0, returns [0.0].

    poly: list of numbers, length > 0
    returns: list of numbers (floats)
    '''
    # FILL IN YOUR CODE HERE...
    result = []
    exp = 0
    for i in poly:
        res = float(i*exp)
        exp = exp + 1
        result.append(res)
    if len(result) > 1:
        del result[0]
    return result


print computeDeriv([-13.39, 0.0, 17.5, 3.0, 1.0])
print computeDeriv([6, 1, 3, 0])
print computeDeriv([20])