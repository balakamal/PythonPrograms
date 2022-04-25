from functools import reduce


def findTheSecretIntegers(N, B):
    res = []
    for i in B:
        l = []

        for j in B:
            if i != j:
                l.append(j)
        res.append(reduce(lambda x, y: x ^ y, l))
    return res


n = int(input())
b = []
for _ in range(n):
    b.append(int(input()))
print(findTheSecretIntegers(n, b))
