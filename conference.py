n = int(input())
s = []
for _ in range(n):
    s.append(int(input()))
m = int(input())
e = []
for _ in range(m):
    e.append(int(input()))
for i in range(m-1):
    if(e[i] > e[i+1]):
        temp, temp1 = e[i], s[i]
        e[i], s[i] = e[i+1], s[i+1]
        e[i+1], s[i+1] = temp, temp1

count = 1
ans = e[0]

for i in range(n-1):
    if(ans <= s[i+1]):
        ans = e[i+1]
        count += 1
print(count)
