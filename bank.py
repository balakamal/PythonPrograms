n = int(input())
l = 7
k = 1
j = 1
res = 0
for _ in range(1, n+1):
    if(l < 1):
        l = 7
        k += 1
        j = k
    res += j
    j += 1
    l -= 1

print(res)
