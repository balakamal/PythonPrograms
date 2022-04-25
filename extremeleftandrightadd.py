from math import ceil
s = input()
l = [int(i) for i in s]
res = ''
j = len(l) - 1
for i in range(ceil(len(l)/2)):
    print(i, j, res)
    if(i != j):
        res += str(l[i]+l[j])
    else:
        res += str(l[i])
    j -= 1
print(res)
