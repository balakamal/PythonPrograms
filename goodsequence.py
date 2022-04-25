from collections import Counter


def countOperations(A):
    res = 0
    even, odd = [A[i] for i in range(len(A)) if i % 2 == 0], [
        A[i] for i in range(len(A)) if i % 2 != 0]
    even_counts, odd_counts = Counter(even), Counter(odd)
    even_Keymax, odd_Keymax = max(even_counts, key=lambda x: even_counts[x]), max(
        odd_counts, key=lambda x: odd_counts[x])

    for i in even:
        if i != even_Keymax:
            res += 1
    for j in odd:
        if j != odd_Keymax:
            res += 1
    return(res)


a = list(map(int, input().split(',')))
print(countOperations(a))
