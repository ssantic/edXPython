def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    power = 1
    if x <= 0 or b <= 0:
        print 'Both inputs must be positive integers.'
    else:
        while b**power <= x:
            power = power + 1
        if b**power > x:
            power = power - 1
        return power


def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length,
    then the extra elements should appear at the end.
    """

    join = []
    smaller = min(s1, s2, key=len)
    for num in range(len(smaller)):
        join.append(s1[num])
        join.append(s2[num])
    join = ''.join(join)
    if len(s1) != len(s2):
        smaller = len(smaller)
        join = join + max(s1, s2, key=len)[smaller:]
    return join


def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length,
    then the extra elements should appear at the end.
    """

    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            return out+s2
        if s2 == '':
            return out+s1
        else:
            return helpLaceStrings(s1[1:], s2[1:], out+s1[0]+s2[0])

    return helpLaceStrings(s1, s2, '')


def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """

    if n == 0:
        return True
    for i in (6, 9, 20):
        if n >= i and McNuggets(n - i):
            return True
    return False


def fixedPoint(f, epsilon):
    """
    f: a function of one argument that returns a float
    epsilon: a small float

    returns the best guess when that guess is less than epsilon
    away from f(guess) or after 100 trials, whichever comes first.
    """
    guess = 1.0
    for i in range(100):
        if abs(f(guess) - guess) < epsilon:
            return guess
            print guess
        else:
            guess = f(guess)
            print guess
    return guess


def sort1(lst):
    swapFlag = True
    iteration = 0
    while swapFlag:
        swapFlag = False
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                temp = lst[i+1]
                lst[i+1] = lst[i]
                lst[i] = temp
                swapFlag = True
            iteration += 1
    return lst


def sort2(lst):
    for iteration in range(len(lst)):
        minIndex = iteration
        minValue = lst[iteration]
        for j in range(iteration+1, len(lst)):
            if lst[j] < minValue:
                minIndex = j
                minValue = lst[j]
        temp = lst[iteration]
        lst[iteration] = minValue
        lst[minIndex] = temp
    return lst


def sort3(lst):
    out = []
    for iteration in range(0,len(lst)):
        new = lst[iteration]
        inserted = False
        for j in range(len(out)):
            if new < out[j]:
                out.insert(j, new)
                inserted = True
                break
        if not inserted:
            out.append(new)
    return out


def sort4(lst):
    def unite(l1, l2):
        if len(l1) == 0:
            return l2
        elif len(l2) == 0:
            return l1
        elif l1[0] < l2[0]:
            return [l1[0]] + unite(l1[1:], l2)
        else:
            return [l2[0]] + unite(l1, l2[1:])

    if len(lst) == 0 or len(lst) == 1:
        return lst
        print lst
    else:
        front = sort4(lst[:len(lst)/2])
        back = sort4(lst[len(lst)/2:])
        print lst

        return unite(front, back)





