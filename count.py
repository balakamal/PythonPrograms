from typing import Counter
n = int(input())
s = []
for _ in range(n):
    s.append(int(input()))

cnt = Counter(s)
keys = list(cnt.keys())
values = list(cnt.values())
for i in range(len(values)-1):
    if(values[i] < values[i+1]):
        temp, temp1 = values[i], keys[i]
        values[i], keys[i] = values[i+1], keys[i+1]
        values[i+1], keys[i+1] = temp, temp1
i, j = 0, -1

while(True):
    if(keys[i] > keys[j]):
        print(values[i]-values[j])
        break
    else:
        i += 1
    if(i == n):
        print(0)
        break
