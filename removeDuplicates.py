n = int(input())
l = []
res = ''
for _ in range(n):
    s = input()
    if s not in l:
        l.append(s)
        res += s + ' '
print(res[:-1])
