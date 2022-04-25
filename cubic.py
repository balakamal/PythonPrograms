import math


def sumOfTwoCubes(n):
    lo = 1
    hi = round(math.pow(n, 1 / 3))

    while (lo <= hi):
        curr = (lo * lo * lo + hi * hi * hi)
        if (curr == n):
            return True
        if (curr < n):
            lo += 1
        else:
            hi -= 1
    return False


def iscubicsumexists(A, n):
    res = 0
    for i in A:
        if sumOfTwoCubes((i)):
            res += 1
    return res


n = int(input())
a = list(map(int, input().split(',')))
print(iscubicsumexists(a, n))
