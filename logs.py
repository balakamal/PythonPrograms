n = int(input())
logs = {}
for _ in range(n):
    s = input().split(" ")
    if("sign-in" in s):
        logs[int(s[0])] = [int(s[1])]
    if("sign-out" in s):
        logs[int(s[0])].append(int(s[1]))
max_spin = int(input())
print(logs)
keys = list(logs.keys())
print(keys)
res = []
for i in keys:
    if(len(logs[i]) > 1 and logs[i][1]-logs[i][0] <= max_spin):
        res.append(i)
res.sort()
ans = [str(i) for i in res]
print(ans)
