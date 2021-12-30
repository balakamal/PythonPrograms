n = int(input())
lines = []
for _ in range(n):
    lines.append(input())
t = 0
s = 0
for i in lines:
    if(i.startswith('# ')):
        s = 0
        t += 1
        print(str(t)+". " + i[2:])

    if(i.startswith("## ")):
        s += 1
        print(str(t) + "." + str(s) + ". " + i[3:])
