from collections import Counter
n = int(input())
l = list(map(int, input().split(' ')))

counts = dict(Counter(l))
res = sorted(counts.items(), key=lambda x: (x[1], x[0]))
print(res[0][0])
