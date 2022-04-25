def arrayDivision(N, K, A):
    l = []
    for i in range(1, N):
        l.append(A[i - 1] - A[i])
    l.sort()
    res = A[N - 1] - A[0]
    for i in range(K - 1):
        res += l[i]

    return res


def main():
    N = int(input())
    K = int(input())
    A = []
    for _ in range(N):
        A.append(int(input()))
    print(arrayDivision(N, K, A))


main()
