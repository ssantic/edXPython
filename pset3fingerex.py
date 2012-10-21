def iterPower (base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''

    result = 1
    if exp == 0:
        return result
    while exp > 0:
     result = result*base
     exp = exp - 1
    return result



def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''

    if exp == 0:
        return 1
    else:
        base = base * recurPower(base, exp - 1)
    return base



def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp

    This function recursively computes exponentials using multiplication
    and remainders.
    '''

    if exp == 0:
        return 1
    elif exp%2 == 0:
        base = recurPowerNew(base*base, exp/2)
    else:
        base = base * recurPowerNew(base, exp - 1)
    return base



def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''

    result = min(a,b)
    while result > 1:
        if a%result == 0 and b%result == 0:
            return result
        else:
            result = result - 1
    return result



def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''

    if b == 0:
        return a
    else:
        return gcdRecur(b, a%b)


def lenIter(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''

    result = 0
    for letter in aStr:
        result = result + 1
    return result



def lenRecur(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''

    if aStr == '':
        return 0
    else:
        return 1 + lenRecur(aStr[1:])



def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise

    This example uses the bisection search algorithm.
    '''

    mid = len(aStr)/2
    if aStr == '' or len(aStr) == 1:
        return char == aStr
    elif char == aStr[mid]:
            return True
    elif char < aStr[mid]:
        aStr = aStr[: mid]
        return isIn(char, aStr)
    else:
        aStr = aStr[mid + 1:]
        return isIn(char, aStr)



def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''

    return aTup[0::2]



def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''

    count = 0
    for i in aDict:
     count = count + len(aDict[i])
    return count



def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''

    if aDict:
     return max(aDict.items(), key=lambda x: len(x[1]))[0]

