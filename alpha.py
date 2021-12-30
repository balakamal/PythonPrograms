alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = list(map(int, input()))
print(sum(n))
while sum(n) > 26:
    r = sum(n)
    n = list(map(int, str(r)))

print(alpha[sum(n)-1])
