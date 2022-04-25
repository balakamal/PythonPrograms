n = int(input())
sum = 0
for _ in range(n):
    sum += float(input())
f = sum/n
c = 5*((f - 32)/9)
print(round(c, 2))
