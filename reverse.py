s = input().split(" ")
for i in s:
    if(not i.isalpha()):
        s.remove(i)
i = -1
for _ in range(len(s)):
    print(s[i], end=" ")
    i -= 1
