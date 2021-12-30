n = int(input())
t = []
i = -1
ans = 0
for _ in range(n):
    b = int(input())
    if(i > 0 and b - t[i] != 1):
        ans = t[i] + 1
    t.append(b)
    i += 1
print(ans)
